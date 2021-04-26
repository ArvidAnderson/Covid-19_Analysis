<template>
  <div class="flex h-screen bg-gray-200">
    <sidebar />

    <div class="flex-1 flex flex-col overflow-hidden">
      <div>
        <navbar/>
      </div>
      <div class="mt-20 mr-5 ml-5 mb-20">
        <router-view/>
      </div>
    </div>
  </div>
</template>
<script>
import sidebar from '../dashboard/sidebar.vue'
import navbar from '../dashboard/navbar.vue'

export default {
  components: {
    sidebar,
    navbar
  }
}
</script>