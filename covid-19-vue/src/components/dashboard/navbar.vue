<template>
  <nav class="text-center p-3 fixed w-full bg-white border-b-4 border-theme">
    <div class="flex mr-3 text-white items-center justify-center">
      <div class="flex w-full items-center justify-between">
        <div class="mr-5 font-bold text-3xl text-theme">
            <h1>Kazung Visualizer</h1>
        </div>
        <div class="flex jusitfy-between mr-9">
            <button @click="Logout()" class="text-theme mr-7">Logout</button>
            <div class="rounded-full bg-theme h-11 w-11 flex items-center justify-center..."></div>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import firebase from 'firebase'

export default ({
  setup() {
    const Logout = () => {
      firebase.auth().signOut().catch(err => {
        console.log(err)
      })
    }
    return {
      Logout
    }
  },
})
</script>
