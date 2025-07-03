<script setup>
import { onMounted, ref } from 'vue'

import { useTitleStore } from '@/stores/useTitleStore'
import { useAuthStore } from './stores/useAuthStore'
import { storeToRefs } from 'pinia'

import LoginForm from '@/components/ LoginForm.vue'
import RegisterForm from './components/RegisterForm.vue'


const titleStore = useTitleStore()
const authStore = useAuthStore()

const { isAuthenticated, user } = storeToRefs(authStore)

const logout = () => {
  authStore.logout()
}

onMounted(() => {
  titleStore.loadTitles()
})

const showLoginModal = ref(false)
const showRegisterModal = ref(false)

const openLoginModal = () => {
  showRegisterModal.value = false
  showLoginModal.value = true
}

const openRegisterModal = () => {
  showLoginModal.value = false
  showRegisterModal.value = true
}

</script>

<template>
  <main>
    <header>
      <div class="main-header-container">
        <div class="logo">
          <router-link to="/">
            <img src="@/assets/logo.svg" alt="logo" class="logo">
          </router-link>
        </div>

        <div class="header-nav">
          <router-link :to="{name: 'catalog'}">Каталог</router-link>
          <a href="#">Топы</a>   
        </div>

        <div v-if="isAuthenticated" class="auth-container">
          <p>{{ user.username }}</p>
          <a @click="logout" class="link">Выйти</a>
        </div>

        <a v-else @click="openLoginModal" class="link">Войти</a>
      </div>
    </header>

    <div class="container">
      <router-view/>
      <LoginForm 
        v-model="showLoginModal" 
        @open-register="openRegisterModal" 
      />
      <RegisterForm 
        v-model="showRegisterModal" 
        @open-login="openLoginModal"
      />
    </div>

  </main>
</template>

<style>
header {
  background-color: #212121;
  width: 100%;
  max-width: 100%;
  margin-bottom: 20px;
  position: sticky;
  top: 0;
}

.main-header-container {
  display: grid;
  grid-template-columns: 0.25fr 1fr 1fr;
  align-items: center;
  padding:15px;
  width: 80%;
  margin: 0 auto;
}

.header-nav {
  display: flex;
  gap: 20px;
}

.header-nav a{ 
  padding: 7px;
  border-radius: 35px;
  background-color: dimgrey;
}

.container {
  margin: 0 auto;
  width: 80%;
  overflow: visible;
}

.logo {
  width: 30px;
  height: 30px;
}

.link {
  justify-self: end;
  cursor: pointer;
}

.auth-container {
  display: flex;
  gap: 10px;
  justify-self: end;
}
</style>
