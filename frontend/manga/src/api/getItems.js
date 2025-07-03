import { apiClient } from '.'
import qs from 'qs'

export function createApiResource(basePath) {
  return {
    async getAll(params) {
      const response = await apiClient.get(basePath, { 
        params: params,
        paramsSerializer: params =>  qs.stringify(params, {arrayFormat: 'repeat'})
      })
      return response.data
    },
    async getById(id) {
      const response = await apiClient.get(`${basePath}${id}/`)
      return response.data
    },
  }
}