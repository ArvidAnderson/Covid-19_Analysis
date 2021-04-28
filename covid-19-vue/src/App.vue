<template>
    <fullpage_layout v-if="layout == 1"></fullpage_layout>
    <dashboard_layout v-if="layout == 2"></dashboard_layout>
</template>
<script>

import fullpage_layout from '@/components/layout/fullpage_layout.vue'
import dashboard_layout from '@/components/layout/dashboard_layout.vue'
import { useRouter, useRoute } from "vue-router"
import { onBeforeMount, computed } from 'vue'
import firebase from 'firebase'

export default ({
  components: {
    dashboard_layout,
    fullpage_layout
  },
  setup() {
    const { currentRoute } = useRouter();
    const layout = computed(
      () => `${currentRoute.value.meta.layout}`
    );

    const router = useRouter();
    const route = useRoute();
    onBeforeMount(() => {
      firebase.auth().onAuthStateChanged((user) => {
        if (!user) {
          router.replace('/')
        } else if (route.path == "/") {
          router.replace('/dashboard/home')
        }
      });
    });
    return {
      layout,
    };
  },
})
</script>
