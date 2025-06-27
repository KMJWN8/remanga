import { ref } from 'vue'


export function useFilterLogic(filterApi) {
  const titleSelectors = ref([])
  const selector = ref(null)
  const loading = ref(false)
  const error = ref(null)

  async function loadAllFilter(filters = {}) {
    loading.value = true
    error.value = null
    try {
      const data = await filterApi.getAll(filters)
      titleSelectors.value = data
    } catch (err) {
      error.value = err.message || 'Ошибка загрузки'
    } finally {
      loading.value = false
    }
  }

  async function loadFilterById(id) {
    loading.value = true
    error.value = null
    try {
      const data = await filterApi.getById(id)
      selector.value = data
    } catch (err) {
      error.value = err.message || 'Ошибка загрузки'
    } finally {
      loading.value = false
    }
    
  }

  return {
    titleSelectors,
    selector,
    loading,
    error,
    loadAllFilter,
    loadFilterById,
  }
}