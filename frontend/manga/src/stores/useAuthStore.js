import { defineStore } from "pinia"
import {ref, computed} from 'vue'
import router from "@/router"
import axios from "axios"

const BASE_API_URL = 'http://127.0.0.1:8000/'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(JSON.parse(localStorage.getItem('user')) || null)
    const accessToken = ref(localStorage.getItem('accessToken') || null)
    const refreshToken = ref(localStorage.getItem('refreshToken') || null)
    const loading = ref(false)
    const error = ref(null)
    
    const isAuthenticated = computed(() => {
        return !!accessToken.value
    })

    const api = axios.create({
        baseURL: `${BASE_API_URL}auth/`
    })

    //добавляем access token в заголовки
    api.interceptors.request.use(config => {
        if (accessToken.value) {
            config.headers.Authorization = `Bearer ${accessToken.value}`
        }
        return config
    })

    //обработка ошибок 401 - обновление токена
    api.interceptors.response.use(
        response => response,
        async errorResponse => {
            const originalRequest = errorResponse.config

            if (
                errorResponse.response?.status === 401 &&
                refreshToken.value &&
                !originalRequest._retry
            ) {
                originalRequest._retry = true
                try {
                    await refreshAccessToken()
                    originalRequest.headers.Authorization = `Bearer ${accessToken.value}`
                    return api(originalRequest)
                } catch(e) {
                    logout()
                    return Promise.reject(e)
                }
            }
            return Promise.reject(errorResponse)
        }
    )

    async function login(email, password) {
        loading.value =true
        error.value = null
        try {
            const response = await api.post('jwt/create/', {email, password})

            accessToken.value = response.data.access
            refreshToken.value = response.data.refresh

            localStorage.setItem('accessToken', accessToken.value)
            localStorage.setItem('refreshToken', refreshToken.value)
            
            //получение информации о пользователе
            const userResponse = await api.get('users/me/', {
                headers: {
                    Authorization: `Bearer ${accessToken.value}`
                }
            })
            user.value = userResponse.data
            localStorage.setItem('user', JSON.stringify(user.value))

            router.push('/')
        } catch (e) {
            error.value = 'Неверный логин или пароль'
            throw e
        } finally {
            loading.value = false
        }
    }

    async function logout() {
        user.value = null
        accessToken.value = null
        refreshToken.value = null
        localStorage.removeItem('user')
        localStorage.removeItem('accessToken')
        localStorage.removeItem('refreshToken')
        router.push('/')
    }

    async function refreshAccessToken() {
        try {
            const response = await api.post('jwt/refresh/', {
                refresh: refreshToken.value
            })
            accessToken.value = response.data.access
            localStorage.setItem('accessToken', accessToken.value)

            if(response.data.refresh) {
                refreshToken.value = response.data.refresh
                localStorage.setItem('refreshToken', refreshToken.value)
            }
        } catch (e) {
            logout()
            throw e
        }
    }

    async function register({email, username, password, re_password}) {
        loading.value = true
        error.value = null

        try {
            await api.post('users/', {
                email,
                username,
                password,
                re_password
            })
        } catch (e) {
            if (e.response && e.response.data) {
                error.value = e.response.data.detail || JSON.stringify(e.response.data)
            } else {
                error.value = 'Ошибка регистрации'
            }
            throw e
        } finally {
            loading.value = false
        }
    }
    return {
        user,
        accessToken,
        refreshToken,
        isAuthenticated,
        loading,
        error,
        login,
        register,
        logout,
        refreshAccessToken,
        api,
    }
})