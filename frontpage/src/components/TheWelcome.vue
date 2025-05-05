<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'

const openReadmeInEditor = () => fetch('/__open-in-editor?file=README.md')
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Source Code</template>

    Our's
    <a
      class="green"
      href="https://github.com/rafliafriza12/cnn-dataset-fashion-web-based"
      target="_blank"
      rel="noopener"
      >source code</a
    >
    provides you with all information you need to get started.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Tooling</template>

    This project is a full-stack image classification web app using
    <a href="https://vite.dev/guide/features.html" class="green" target="_blank" rel="noopener"
      >Vue</a
    >
    for the frontend. and
    <a
      href="https://flask.palletsprojects.com/en/stable/"
      class="green"
      target="_blank"
      rel="noopener"
      >Flask</a
    >
    with a CNN model trained on Fashion MNIST for the backend to process and predict clothing
    categories from grayscale images.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Ecosystem</template>

    This project integrates
    <span class="green">Vue ecosystem tools</span> such as <span class="green">Pinia</span> for
    state management and <span class="green">Vue Router</span> for seamless navigation. Axios is
    used to handle <span class="green">HTTP requests</span> between the
    <span class="green">frontend</span> and <span class="green">Flask backend</span>. Image
    preprocessing and prediction are powered by
    <span class="green">TensorFlow, Keras, Pillow, and NumPy</span>.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Team</template>
    <span class="green">Rafli</span> Afriza Nugraha, Athar
    <span class="green">Rayyan</span> Muhammad, <span class="green">Glenn</span> Hakim, T
    <span class="green">farhan</span> syah, Al-Mahfuzh Fadhlur <span class="green">Rohman</span>
  </WelcomeItem>
</template>
