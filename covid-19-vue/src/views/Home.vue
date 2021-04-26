<template>
  <navbar/>
  <div class="flex justify-center items-center h-screen bg-theme">
    <main>
      <div class="text-4xl text-white">
        <h1 class="text-center">Your visualizer for swedish <b>COVID-19</b> stats</h1>
      </div>
    </main>
  </div>
</template>

<script>

//Navbar
import navbar from '@/components/layout/navbar.vue'

export default {
  name: 'Home',
  components: {
    navbar
  }
}
</script>
