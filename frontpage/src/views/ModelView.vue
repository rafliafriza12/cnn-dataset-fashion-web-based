<template>
  <div class="w-full flex flex-col items-center gap-10">
    <h1 class="font-bold text-4xl">Try Our CNN <span class="green">Model</span></h1>
    <div class="w-full p-10 bg-[#EBEBEB]/10 rounded-2xl backdrop-blur-[2px] flex flex-col gap-5">
      <!-- Image upload area -->
      <div class="flex items-center justify-center w-full">
        <label
          for="dropzone-file"
          class="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer bg-gray-700 border-gray-600 hover:border-gray-500 hover:bg-gray-600"
        >
          <div
            v-if="imageData && !showCamera"
            class="w-full h-full flex items-center justify-center"
          >
            <img
              :src="imageData"
              alt="Uploaded preview"
              class="max-h-full max-w-full object-contain"
            />
          </div>
          <div
            v-else-if="showCamera"
            class="flex flex-col items-center justify-center w-full h-full"
          >
            <video ref="videoElement" autoplay class="min-h-full w-full rounded-lg"></video>
          </div>
          <div v-else class="flex flex-col items-center justify-center pt-5 pb-6">
            <svg
              class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 16"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
              />
            </svg>
            <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
              <span class="font-semibold">Click to upload</span>
            </p>
            <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG</p>
          </div>
          <input
            id="dropzone-file"
            type="file"
            class="hidden"
            accept="image/*"
            @change="handleFileUpload"
          />
        </label>
      </div>

      <!-- Action buttons -->
      <div class="w-full flex items-center justify-between">
        <div class="flex items-center gap-5">
          <button
            v-if="showCamera"
            @click="captureImage"
            class="py-2 px-4 bg-gray-700 font-medium rounded-lg cursor-pointer"
          >
            Capture Photo
          </button>
          <label
            v-else
            for="dropzone-file"
            class="py-2 px-4 bg-gray-700 font-medium rounded-lg cursor-pointer"
          >
            Upload File
          </label>

          <button
            v-if="showCamera"
            @click="closeCamera"
            class="py-2 px-4 bg-gray-700 font-medium rounded-lg cursor-pointer"
          >
            Cancel
          </button>
          <button
            v-else
            @click="openCamera"
            class="py-2 px-4 bg-gray-700 font-medium rounded-lg cursor-pointer"
          >
            Open Camera
          </button>
        </div>
        <button
          v-if="!showCamera && imageData"
          @click="handleSubmit"
          :disabled="isLoading"
          class="py-2 px-4 button-green font-semibold text-black rounded-lg cursor-pointer"
        >
          <div>Submit</div>
        </button>
      </div>

      <!-- Prediction display -->
      <div class="w-full flex flex-col mt-3 h-36 gap-5">
        <h1 class="font-semibold text-2xl">Prediction</h1>
        <div class="flex w-full flex-col gap-3">
          <h1 v-if="isFirstLook">You haven't uploaded an image yet</h1>
          <div v-if="isLoading">Processing image...</div>
          <div v-else>
            <div v-if="responseData !== null">
              <p>Class: {{ responseData.class_label }}</p>
              <p>Confidence: {{ responseData.confidence.toFixed(2) }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onUnmounted } from 'vue'

// State variables
const isFirstLook = ref(true)
const imageData = ref(null)
const imageDataForm = ref(null)
const showCamera = ref(false)
const videoElement = ref(null)
const stream = ref(null)
const responseData = ref(null)
const isLoading = ref(false)

const dataURLToFile = (dataurl, filename) => {
  const arr = dataurl.split(',')
  const mime = arr[0].match(/:(.*?);/)[1]
  const bstr = atob(arr[1])
  let n = bstr.length
  const u8arr = new Uint8Array(n)
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n)
  }
  return new File([u8arr], filename, { type: mime })
}

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  imageDataForm.value = event.target.files[0]
  if (file && file.type.match('image.*')) {
    const reader = new FileReader()
    reader.onload = (e) => {
      imageData.value = e.target.result
      isFirstLook.value = false
    }
    reader.readAsDataURL(file)
  }
}

const openCamera = async () => {
  try {
    stream.value = await navigator.mediaDevices.getUserMedia({ video: true })
    showCamera.value = true

    setTimeout(() => {
      if (videoElement.value) {
        videoElement.value.srcObject = stream.value
      }
    }, 100)
  } catch (err) {
    console.error('Error accessing camera:', err)
    alert("Could not access the camera. Please ensure you've granted permission.")
  }
}

const captureImage = () => {
  if (videoElement.value) {
    const canvas = document.createElement('canvas')
    canvas.width = videoElement.value.videoWidth
    canvas.height = videoElement.value.videoHeight

    const ctx = canvas.getContext('2d')
    ctx.drawImage(videoElement.value, 0, 0, canvas.width, canvas.height)

    imageData.value = canvas.toDataURL('image/png')
    imageDataForm.value = dataURLToFile(imageData.value, 'image-from-camera.png')
    isFirstLook.value = false
    closeCamera()
  }
}

const closeCamera = () => {
  if (stream.value) {
    stream.value.getTracks().forEach((track) => track.stop())
    stream.value = null
  }
  showCamera.value = false
}

const handleSubmit = async () => {
  try {
    isLoading.value = true
    const form = new FormData()
    form.append('image', imageDataForm.value)

    const res = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      body: form,
    })

    const response = await res.json()
    if (response.status === 200) {
      responseData.value = response.data
    }
  } catch (error) {
    console.log(error)
  } finally {
    isLoading.value = false
  }
}

onUnmounted(() => {
  closeCamera()
})
</script>

<style scoped>
.green {
  color: #42b883;
}

.button-green {
  background-color: #42b883;
}
</style>
