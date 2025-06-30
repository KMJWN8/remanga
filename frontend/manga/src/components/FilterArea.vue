<script setup>
import { useFilterStore } from '@/stores/useFilterStore'
import { useTitleStore } from '@/stores/useTitleStore'
import { ref, onMounted, computed } from 'vue'
import MultiSelect from 'primevue/multiselect'

import { 
  genreApi, 
  categoryApi, 
  ageRatingApi, 
  statusApi, 
  typeApi 
  } from '@/api/generalApi'

const titleStore = useTitleStore()

const stores = {
  genres: useFilterStore(genreApi, 'genres'),
  categories: useFilterStore(categoryApi, 'categories'),
  ageRatings: useFilterStore(ageRatingApi, 'age_ratings'),
  statuses: useFilterStore(statusApi, 'statuses'),
  types: useFilterStore(typeApi, 'types')
}

onMounted(() => {
  Object.values(stores).forEach(store => store.loadAllFilter())
})

const filterOptions = computed(() => ({
  genres: filterCompute('genres'),
  categories: filterCompute('categories'),
  ageRatings: filterCompute('ageRatings'),
  statuses: filterCompute('statuses'),
  types: filterCompute('types')
}))

const filterCompute = (filter) => {
  return stores[filter].titleSelectors.map(item => ({
    name: item.name,
    code: String(item.id)
  })) || []
}

const selectedFilters = ref({
  genres: [],
  categories: [],
  ageRatings: [],
  statuses: [],
  types: []
})

const handleFilters = () => {
  const filters = {}

  if (selectedFilters.value.genres.length) {
    filters.genres = selectedFilters.value.genres
  }
  if (selectedFilters.value.categories.length) {
    filters.categories = selectedFilters.value.categories
  }
  if (selectedFilters.value.ageRatings.length) {
  filters.age_ratings = selectedFilters.value.ageRatings
  }
  if (selectedFilters.value.statuses.length) {
    filters.statuses = selectedFilters.value.statuses
  }
  if (selectedFilters.value.types.length) {
    filters.types = selectedFilters.value.types
  }

  titleStore.loadTitles(filters)
}

const resetFilters = () => {
  selectedFilters.value.genres = []
  selectedFilters.value.categories = []
  selectedFilters.value.ageRatings = []
  selectedFilters.value.statuses = []
  selectedFilters.value.types = []

  titleStore.loadTitles()
}

const hasActiveFilters = computed(() => {
  return (  
    selectedFilters.value.genres.length ||
    selectedFilters.value.categories.length ||
    selectedFilters.value.ageRatings.length ||
    selectedFilters.value.statuses.length ||
    selectedFilters.value.types.length
  )
})
</script>

<template>
  <div class="filter-container">
    <strong>Жанры</strong>
    <MultiSelect 
    v-model="selectedFilters.genres" 
    showClear 
    :options="filterOptions.genres" 
    optionLabel="name" 
    filter 
    placeholder="Выберите" 
    class="multiselect" />

    <strong>Категории</strong>
    <MultiSelect 
    v-model="selectedFilters.categories" 
    showClear 
    :options="filterOptions.categories" 
    optionLabel="name" 
    filter 
    placeholder="Выберите" 
    class="multiselect" />

    <strong>Типы</strong>
    <MultiSelect 
    v-model="selectedFilters.types" 
    showClear 
    :options="filterOptions.types" 
    optionLabel="name" 
    filter 
    placeholder="Выберите" 
    class="multiselect" /> 

    <strong>Статус</strong>
    <MultiSelect 
    v-model="selectedFilters.statuses" 
    showClear 
    :options="filterOptions.statuses" 
    optionLabel="name" 
    filter 
    placeholder="Выберите" 
    class="multiselect" /> 

    <strong>Возрастное ограничение</strong>
    <MultiSelect 
    v-model="selectedFilters.ageRatings" 
    showClear 
    :options="filterOptions.ageRatings" 
    optionLabel="name" 
    filter 
    placeholder="Выберите" 
    class="multiselect" />

    <button @click="handleFilters" class="btn-handle">Применить</button>
    <button v-if="hasActiveFilters" @click="resetFilters" class="btn-reset">Сбросить</button>
  </div>
</template>

<style>
.filter-container {
  display: flex;
  flex-direction: column;
  background-color: #212121;
  border-radius: 15px;
  height: max-content;
  padding: 15px;
}

.multiselect {
  margin-top: 10px;
  margin-bottom: 15px;
}
</style>