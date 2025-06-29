import { defineStore } from 'pinia'
import { useFilterLogic } from '@/composables/useFilterLogic'

export const useFilterStore = (filterApi, filterType) => {
  return defineStore(`filter-${filterType}`, () => {

  const { 
    titleSelectors, 
    selector, 
    loading, 
    error, 
    loadAllFilter, 
    loadFilterById 
  } = useFilterLogic(filterApi)

  return {
    titleSelectors,
    selector,
    loading,
    error,
    loadAllFilter,
    loadFilterById,
  }
 })()
}
