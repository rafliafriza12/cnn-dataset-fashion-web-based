<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import CurveSVG from './components/svg/CurveSVG.vue'
</script>

<template>
  <div class="relative z-0 flex flex-col lg:flex-row items-center w-screen h-screen justify-center">
    <div class="absolute z-[-1] scale-[2.5] rotate-y-[180deg] left-[41vw]">
      <CurveSVG />
    </div>
    <header>
      <img alt="Vue logo" class="logo" src="@/assets/logo/logo.png" width="150" height="150" />

      <div class="wrapper">
        <HelloWorld msg="Team 1" />

        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">Try Model</RouterLink>
        </nav>
      </div>
    </header>

    <div class="w-[90%] lg:w-[40%]">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
