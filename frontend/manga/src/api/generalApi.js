import { createApiResource } from "./getItems"


export const titleApi = createApiResource('/titles/')

export const genreApi = createApiResource('/genres/')

export const categoryApi = createApiResource('/categories/')

export const typeApi = createApiResource('/types/')

export const statusApi = createApiResource('/statuses/')

export const ageRatingApi = createApiResource('/age_ratings/')