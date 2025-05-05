<template>
  <div class="flex justify-center items-center w-full h-full bg-transparent">
    <svg
      ref="svgRef"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 844 644"
      fill="none"
      class="w-full max-w-2xl"
    >
      <!-- Input Lines -->
      <g>
        <!-- Line 1 -->
        <path
          d="M843.505 284.659L752.638 284.659C718.596 284.659 684.866 280.049 653.251 271.077L598.822 255.629L0.675021 1.00011"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 284.659L752.638 284.659C718.596 284.659 684.866 280.049 653.251 271.077L598.822 255.629L0.675021 1.00011"
            stroke="url(#glow_gradient_1)"
            stroke-width="1.2"
            mask="url(#glow_mask_1)"
            class="svg-path"
          />
          <defs>
            <mask id="glow_mask_1">
              <path
                d="M843.505 284.659L752.638 284.659C718.596 284.659 684.866 280.049 653.251 271.077L598.822 255.629L0.675021 1.00011"
                fill="black"
              />
              <circle
                :cx="glowPositions['path-0']?.x || 0"
                :cy="glowPositions['path-0']?.y || 0"
                r="15"
                fill="white"
              >
                <animate attributeName="r" values="10;15;10" dur="2s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_1"
              :cx="glowPositions['path-0']?.x || 0"
              :cy="glowPositions['path-0']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#639BFF" stop-opacity="1" />
              <stop offset="100%" stop-color="#639BFF" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Line 2 -->
      <g>
        <path
          d="M843.505 298.181L724.342 297.36C708.881 297.36 693.45 296.409 678.22 294.518L598.822 284.659C592.82 284.659 200.538 190.002 0.675028 164.892"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 298.181L724.342 297.36C708.881 297.36 693.45 296.409 678.22 294.518L598.822 284.659C592.82 284.659 200.538 190.002 0.675028 164.892"
            stroke="url(#glow_gradient_2)"
            stroke-width="1.2"
            mask="url(#glow_mask_2)"
            class="svg-path"
          />
          <defs>
            <mask id="glow_mask_2">
              <path
                d="M843.505 298.181L724.342 297.36C708.881 297.36 693.45 296.409 678.22 294.518L598.822 284.659C592.82 284.659 200.538 190.002 0.675028 164.892"
                fill="black"
              />
              <circle
                :cx="glowPositions['path-1']?.x || 0"
                :cy="glowPositions['path-1']?.y || 0"
                r="15"
                fill="white"
              >
                <animate attributeName="r" values="10;15;10" dur="2.5s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_2"
              :cx="glowPositions['path-1']?.x || 0"
              :cy="glowPositions['path-1']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#639BFF" stop-opacity="1" />
              <stop offset="100%" stop-color="#639BFF" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Line 3 -->
      <g>
        <path
          d="M843.505 311.703L701.108 310.061L598.822 305.136L0.675049 256.071"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 311.703L701.108 310.061L598.822 305.136L0.675049 256.071"
            stroke="url(#glow_gradient_3)"
            stroke-width="1.2"
            mask="url(#glow_mask_3)"
            class="svg-path"
          />
          <defs>
            <mask id="glow_mask_3">
              <path
                d="M843.505 311.703L701.108 310.061L598.822 305.136L0.675049 256.071"
                fill="black"
              />
              <circle
                :cx="glowPositions['path-2']?.x || 0"
                :cy="glowPositions['path-2']?.y || 0"
                r="15"
                fill="white"
              >
                <animate attributeName="r" values="10;15;10" dur="2.8s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_3"
              :cx="glowPositions['path-2']?.x || 0"
              :cy="glowPositions['path-2']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#639BFF" stop-opacity="1" />
              <stop offset="100%" stop-color="#639BFF" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Line 4 - Center Line -->
      <g>
        <path
          d="M843.505 325.224L598.822 326.002L0.675049 321.858"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 325.224L598.822 326.002L0.675049 321.858"
            stroke="url(#glow_gradient_4)"
            stroke-width="1.2"
            mask="url(#glow_mask_4)"
            class="svg-path center-line"
          />
          <defs>
            <mask id="glow_mask_4">
              <path d="M843.505 325.224L598.822 326.002L0.675049 321.858" fill="black" />
              <circle
                :cx="glowPositions['path-3']?.x || 0"
                :cy="glowPositions['path-3']?.y || 0"
                r="20"
                fill="white"
              >
                <animate attributeName="r" values="15;20;15" dur="2s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_4"
              :cx="glowPositions['path-3']?.x || 0"
              :cy="glowPositions['path-3']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#FF6EC7" stop-opacity="1" />
              <stop offset="100%" stop-color="#FF6EC7" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Line 5 -->
      <g>
        <path
          d="M843.505 338.746L701.108 340.388L598.822 345.442L0.675038 387.646"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 338.746L701.108 340.388L598.822 345.442L0.675038 387.646"
            stroke="url(#glow_gradient_5)"
            stroke-width="1.2"
            mask="url(#glow_mask_5)"
            class="svg-path"
          />
          <defs>
            <mask id="glow_mask_5">
              <path
                d="M843.505 338.746L701.108 340.388L598.822 345.442L0.675038 387.646"
                fill="black"
              />
              <circle
                :cx="glowPositions['path-4']?.x || 0"
                :cy="glowPositions['path-4']?.y || 0"
                r="15"
                fill="white"
              >
                <animate attributeName="r" values="10;15;10" dur="2.8s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_5"
              :cx="glowPositions['path-4']?.x || 0"
              :cy="glowPositions['path-4']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#639BFF" stop-opacity="1" />
              <stop offset="100%" stop-color="#639BFF" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Line 6 -->
      <g>
        <path
          d="M843.505 352.268L724.342 353.088C708.881 353.088 693.45 354.039 678.22 355.93L598.822 365.789L0.675067 478.825"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 352.268L724.342 353.088C708.881 353.088 693.45 354.039 678.22 355.93L598.822 365.789L0.675067 478.825"
            stroke="url(#glow_gradient_6)"
            stroke-width="1.2"
            mask="url(#glow_mask_6)"
            class="svg-path"
          />
          <defs>
            <mask id="glow_mask_6">
              <path
                d="M843.505 352.268L724.342 353.088C708.881 353.088 693.45 354.039 678.22 355.93L598.822 365.789L0.675067 478.825"
                fill="black"
              />
              <circle
                :cx="glowPositions['path-5']?.x || 0"
                :cy="glowPositions['path-5']?.y || 0"
                r="15"
                fill="white"
              >
                <animate attributeName="r" values="10;15;10" dur="2.5s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_6"
              :cx="glowPositions['path-5']?.x || 0"
              :cy="glowPositions['path-5']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#639BFF" stop-opacity="1" />
              <stop offset="100%" stop-color="#639BFF" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Line 7 -->
      <g>
        <path
          d="M843.505 365.789L752.638 365.789C718.596 365.789 684.866 370.399 653.251 379.372L598.822 394.82L0.675049 642.717"
          stroke="url(#base_gradient)"
          stroke-width="1.2"
          :style="{ opacity: 0.8 }"
        />
        <g>
          <path
            d="M843.505 365.789L752.638 365.789C718.596 365.789 684.866 370.399 653.251 379.372L598.822 394.82L0.675049 642.717"
            stroke="url(#glow_gradient_7)"
            stroke-width="1.2"
            mask="url(#glow_mask_7)"
            class="svg-path"
          />
          <defs>
            <mask id="glow_mask_7">
              <path
                d="M843.505 365.789L752.638 365.789C718.596 365.789 684.866 370.399 653.251 379.372L598.822 394.82L0.675049 642.717"
                fill="black"
              />
              <circle
                :cx="glowPositions['path-6']?.x || 0"
                :cy="glowPositions['path-6']?.y || 0"
                r="15"
                fill="white"
              >
                <animate attributeName="r" values="10;15;10" dur="2s" repeatCount="indefinite" />
              </circle>
            </mask>
            <radialGradient
              id="glow_gradient_7"
              :cx="glowPositions['path-6']?.x || 0"
              :cy="glowPositions['path-6']?.y || 0"
              r="80"
              gradientUnits="userSpaceOnUse"
            >
              <stop offset="0%" stop-color="#639BFF" stop-opacity="1" />
              <stop offset="100%" stop-color="#639BFF" stop-opacity="0" />
            </radialGradient>
          </defs>
        </g>
      </g>

      <!-- Output Line at the bottom -->
      <g class="mt-2">
        <path
          d="M843.463 600L245.316 604.143L0.633077 603.365"
          stroke="url(#glow_gradient_output)"
          stroke-width="1.2"
          mask="url(#glow_mask_output)"
          class="svg-path"
        />
        <defs>
          <mask id="glow_mask_output">
            <path d="M843.463 600L245.316 604.143L0.633077 603.365" fill="black" />
            <circle
              :cx="glowPositions['path-7']?.x || 0"
              :cy="glowPositions['path-7']?.y || 0"
              r="15"
              fill="white"
            >
              <animate attributeName="r" values="10;15;10" dur="2s" repeatCount="indefinite" />
            </circle>
          </mask>
          <radialGradient
            id="glow_gradient_output"
            :cx="glowPositions['path-7']?.x || 0"
            :cy="glowPositions['path-7']?.y || 0"
            r="80"
            gradientUnits="userSpaceOnUse"
          >
            <stop offset="0%" stop-color="#BD34FE" stop-opacity="1" />
            <stop offset="100%" stop-color="#BD34FE" stop-opacity="0" />
          </radialGradient>
        </defs>
      </g>

      <!-- Common Gradients -->
      <defs>
        <linearGradient
          id="base_gradient"
          x1="88.1032"
          y1="324.167"
          x2="843.505"
          y2="324.167"
          gradientUnits="userSpaceOnUse"
        >
          <stop offset="0" stop-color="#c6caff" stop-opacity="0" />
          <stop offset="0.2" stop-color="#c6caff" stop-opacity="0.1" />
          <stop offset="0.4" stop-color="white" stop-opacity="0.4" />
          <stop offset="0.6" stop-color="#c6caff" stop-opacity="0.2" />
          <stop offset="0.8" stop-color="#c6caff" stop-opacity="0.2" />
          <stop offset="0.9" stop-color="#c6caff" stop-opacity="0" />
        </linearGradient>

        <linearGradient id="output_gradient" gradientUnits="userSpaceOnUse">
          <stop offset="0.1" stop-color="#E0C8FF" stop-opacity="0" />
          <stop offset="0.4" stop-color="#E0C8FF" stop-opacity="0.4" />
          <stop offset="1" stop-color="#E0C8FF" stop-opacity="0" />
        </linearGradient>
      </defs>

      <!-- Central point with pulsing animation -->
      <circle cx="598.822" cy="326.002" r="8" fill="#FF6EC7" filter="url(#center_glow)">
        <animate attributeName="r" values="6;10;6" dur="1.5s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.7;1;0.7" dur="1.5s" repeatCount="indefinite" />
      </circle>

      <defs>
        <filter id="center_glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'GlowingNeonLines',
  data() {
    return {
      glowPositions: {},
      animationId: null,
    }
  },
  mounted() {
    this.initializeAnimation()
  },
  beforeUnmount() {
    if (this.animationId !== null) {
      cancelAnimationFrame(this.animationId)
    }
  },
  methods: {
    initializeAnimation() {
      const paths = document.querySelectorAll('.svg-path')
      const speeds = {}
      const positions = {}

      paths.forEach((path, index) => {
        const pathId = `path-${index}`
        speeds[pathId] = 0.002 + Math.random() * 0.003 // Kecepatan berbeda untuk setiap jalur
        positions[pathId] = Math.random() // Posisi awal acak pada jalur
      })

      const animate = () => {
        const newGlowPositions = {}

        paths.forEach((path, index) => {
          const pathId = `path-${index}`
          const pathElement = path

          // Update posisi
          positions[pathId] += speeds[pathId]
          if (positions[pathId] > 1) positions[pathId] = 0

          // Dapatkan posisi pada jalur berdasarkan persentase
          const point = pathElement.getPointAtLength(
            positions[pathId] * pathElement.getTotalLength(),
          )
          newGlowPositions[pathId] = { x: point.x, y: point.y }
        })

        this.glowPositions = newGlowPositions
        this.animationId = requestAnimationFrame(animate)
      }

      animate()
    },
  },
}
</script>

<style scoped>
/* Jika diperlukan, tambahkan CSS khusus di sini */
</style>
