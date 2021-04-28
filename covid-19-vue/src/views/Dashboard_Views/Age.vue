<template>
  <div>
    <div class="mt-5 w-full">
      <div class="bg-white p-3 mb-5">
        <h1 class="text-2xl">Age Groups</h1>
      </div>
      <div>
        <!-- Grid -->
        <div class="text-white grid w-full 2xl:grid-cols-5 xl:grid-cols-5 lg:grid-cols-4 md:grid-cols-2 sm:grid-cols-2 xs:grid-cols-1 gap-2">
          <!--Age 0-9-->
          <div class="bg-blue-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>0-9</h1>
            </div>
            <div>
              <h1>
                Total Cases: {{ agegroups[0]['Total_Cases']}}
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 10-19-->
          <div class="bg-green-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>10-19</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 20-29-->
          <div class="bg-yellow-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>20-29</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 30-39-->
          <div class="bg-purple-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>30-39</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 40-49-->
          <div class="bg-red-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>40-49</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 50-59-->
          <div class="bg-pink-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>50-59</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 60-69-->
          <div class="bg-indigo-600 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>60-69</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 70-79-->
          <div class="bg-purple-400 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>70-79</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 80-89-->
          <div class="bg-red-400 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>80-89</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
          <!--Age 90+-->
          <div class="bg-blue-400 p-4 rounded-xl">
            <div class="text-3xl text-left">
              <h1>90+</h1>
            </div>
            <div>
              <h1>
                Total Cases:
              </h1>
              <h1>
                Total ICU:
              </h1>
              <h1>
                Total Deaths:
              </h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref } from 'vue'
export default {
  setup() {
    const agegroups = ref([])
    const FetchData = async () => {
      const response = await fetch(`http://localhost:3000/age/`)
      const data = await response.json()
      agegroups.value = data
    }

    FetchData()
    return {
      agegroups
    }

  }
}
</script>

