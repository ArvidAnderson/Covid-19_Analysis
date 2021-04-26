<template>
  <div class="flex">
      <div class="flex-col bg-theme pl-2 pr-2">
          <div class="flex h-screen items-center text-white">
            <ul>
                <li class="flex text-2xl mb-3"
                :class="[$route.name === 'Dashboard Home' ? activeClass : inactiveClass]">
                    <router-link to="/dashboard/home">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                        </svg>
                    </router-link>
                </li>
                <li class="flex text-2xl mb-3"
                :class="[$route.name === 'Dashboard Map' ? activeClass : inactiveClass]">
                    <router-link to="/dashboard/map">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" fill="white" viewBox="0 0 24 24" stroke="white">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                        </svg>
                    </router-link>
                </li>
                <li class="flex text-2xl"
                :class="[$route.name === 'Age' ? activeClass : inactiveClass]">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" fill="white" viewBox="0 0 24 24" stroke="white">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                    </svg>
                </li>
            </ul>
          </div>
      </div>
  </div>
</template>
<script>
import { ref } from 'vue'

export default ({
    setup() {
        const activeClass = ref(
        "opacity-50"
        );
        const inactiveClass = ref(
        ""
        );
        return {
            activeClass,
            inactiveClass
        }
    },
})
</script>
