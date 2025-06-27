import { defineStore } from 'pinia'

import { useFilterLogic } from '@/composables/useFilterLogic'

export const useTitleStore = defineStore('filter', () => {
  const { titleSelectors, selector, loading, error, loadAllFilter, loadFilterById } = useFilterLogic()

  return {
    titleSelectors,
    selector,
    loading,
    error,
    loadAllFilter,
    loadFilterById,
  }
})