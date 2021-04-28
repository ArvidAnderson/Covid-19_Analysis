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
                Total Cases: {{ age09cases }}
              </h1>
              <h1>
                Total ICU: {{ age09icu }}
              </h1>
              <h1>
                Total Deaths: {{ age09deaths }}
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
                Total Cases: {{ age1019cases }}
              </h1>
              <h1>
                Total ICU: {{ age1019icu }}
              </h1>
              <h1>
                Total Deaths: {{ age1019deaths }}
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
                Total Cases: {{ age2029.icu }}
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
import { ref, reactive, toRefs } from 'vue'
export default {
  setup() {
    //Age 0-9
    const age09cases = ref(null)
    const age09icu = ref(null)
    const age09deaths = ref(null)
    //Age 10-19
    const age1019cases = ref(null)
    const age1019icu = ref(null)
    const age1019deaths = ref(null)
    //Age 20-29
    const age2029 = reactive({
        cases: null,
        icu: null,
        deaths: null
    })
    const FetchData = async () => {
      const response = await fetch(`http://localhost:3000/age/`)
      const data = await response.json()
      age09cases.value = data[0]['Total_Cases']
      age09icu.value = data[0]['Total_ICU_Admissions']
      age09deaths.value = data[0]['Total_Deaths']
      age1019cases.value = data[1]['Total_Cases']
      age1019icu.value = data[1]['Total_ICU_Admissions']
      age1019deaths.value = data[1]['Total_Deaths']
      age2029.cases = data[2]['Total_Cases']
      age2029.icu = data[2]['Total_ICU_Admissions']
      age2029.deaths = data[1]['Total_Deaths']
    }

    FetchData()
    return {
      ...toRefs(age2029),
      age09cases,
      age09icu,
      age09deaths,
      age1019cases,
      age1019icu,
      age1019deaths
    }

  }
}
</script>

