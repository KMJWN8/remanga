<script setup>
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'

import { useTitleStore } from '@/stores/useTitleStore'

const route = useRoute()

const titleStore = useTitleStore()

const titleId = route.params.id

onMounted(() => {
    titleStore.loadTitleById(titleId)
})

const { title } = storeToRefs(titleStore)

console.log(title)
</script>

<template>
  <div v-if="title">
    <h1>{{ title.name }}</h1>
    <p>Тип: {{ title.type.name }}</p>
    <p>Год выпуска: {{ title.year_released }}</p>
  </div>

  <div v-else>
    <p>Манга не найдена.</p>
  </div>
</template>

<style scoped>
    
</style>