<script setup>
import { onMounted } from 'vue'

import { useFilterStore } from '@/stores/useFilterStore'
import { genreApi } from '@/api/generalApi'


const genresStore = useFilterStore(genreApi, 'genres')

onMounted(() => {
    genresStore.loadAllFilter()
})
</script>

<template>
  <div v-if="genresStore.loading">Загрузка жанров...</div>
  <div v-else>
    Жанры: {{ genresStore.titleSelectors }}
  </div>

</template>