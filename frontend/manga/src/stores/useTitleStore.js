import { ref } from 'vue'
import { defineStore } from 'pinia'

import { titleApi } from '@/api/generalApi'

export const useTitleStore = defineStore('title', () => {
  const titles = ref([])
  const title= ref(null)
  const loading = ref(false)
  const error = ref(null)

  async function loadTitleById(id) {
    loading.value = true
    error.value = null
    try {
      const data = await titleApi.getById(id)
      title.value = data
    }
    catch (err) {
      error.value = err.message || "Ошибка загрузки тайтла"
    }
    finally {
      loading.value = false
    }
  }

  async function loadTitles(filters = {}) {
    loading.value = true
    error.value = null
    try {
      const data = await titleApi.getAll(filters)
      titles.value = data
    } catch (err) {
      error.value = err.message || 'Ошибка загрузки тайтлов'
    } finally {
      loading.value = false
    }
  }

  return {
    titles,
    title,
    loading,
    error,
    loadTitles,
    loadTitleById,
  }
})