<template>
  <nav class="text-center p-3 fixed w-full">
    <div class="flex mr-3 text-white items-center justify-center">
      <div class="flex 2xl:w-3/5 xl:w-3/5 lg:w-4/6 md:w-full sm:w-full justify-between">
        <div class="mr-3">
          <h1 class="text-3xl font-bold">Kazung Visualizer</h1>
        </div>
        <div class="ml-3">
          <button class="mr-3 bg-transparent hover:bg-blue-700 text-white font-semibold hover:text-white py-2 px-4 border border-white hover:border-transparent rounded">
            <router-link to="login">Login</router-link>
          </button>
          <button class="bg-transparent hover:bg-blue-700 text-white font-semibold hover:text-white py-2 px-4 border border-white hover:border-transparent rounded">
            <router-link to="register">Register</router-link>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
}
</script>
