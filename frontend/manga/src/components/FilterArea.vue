<script setup>
import { ref } from 'vue'
import MultiSelect from 'primevue/multiselect'

const selectedCities = ref();
const cities = ref([
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
])
</script>

<template>
 <div> 
    <div class="card flex justify-center multiselect">
      <MultiSelect 
        v-model="selectedCities" 
        showClear 
        :options="cities" 
        optionLabel="name" 
        filter 
        placeholder="Select Cities" 
        :maxSelectedLabels="3" 
        class="w-full md:w-80" />
   </div>
 </div>
</template>

<style>
    
</style>