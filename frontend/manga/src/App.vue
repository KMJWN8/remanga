<script setup>
import { onMounted, ref } from 'vue'

import { useTitleStore } from '@/stores/useTitleStore'
import LoginForm from '@/components/ LoginForm.vue'

const titleStore = useTitleStore()

onMounted(() => {
  titleStore.loadTitles()
})

const showModal = ref(false)

const openLoginModal = () => {
  showModal.value = true
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
          
        <button @click="openLoginModal" class="btn btn-login">Войти</button>
      </div>
    </header>

    <div class="container">
      <router-view/>
      <LoginForm v-model="showModal"></LoginForm>
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

.btn-login {
  justify-self: end;
}
</style>
