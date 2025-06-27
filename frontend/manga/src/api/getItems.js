import { apiClient } from '.'

export function createApiResource(basePath) {
  return {
    async getAll(params) {
      const response = await apiClient.get(basePath, { params })
      return response.data
    },
    async getById(id) {
      const response = await apiClient.get(`${basePath}${id}/`)
      return response.data
    },
  }
}