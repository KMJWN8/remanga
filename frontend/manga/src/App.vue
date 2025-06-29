<script setup>
import { onMounted } from 'vue'

import { useTitleStore } from '@/stores/useTitleStore'

const titleStore = useTitleStore()

onMounted(() => {
  titleStore.loadTitles()
})

</script>

<template>
  <main>
    <header>
        <div class="logo">
          <router-link to="/">
            <img src="@/assets/logo.svg" alt="logo" class="logo">
          </router-link>
        </div>

        <div class="header-nav">
          <router-link :to="{name: 'catalog'}">Каталог</router-link>
          <router-link :to="{name: 'filters'}">Фильтры</router-link> 
          <a href="#">Топы</a>   
        </div>
          
        <a href="#" class="btn btn-login">Войти/Зарегистрироваться</a>
    </header>

    <div class="container">
      <router-view/>
    </div>

  </main>
</template>

<style>
header {
  background-color: #212121;
  padding:15px;
  width: 100%;
  max-width: 100%;
  margin-bottom: 20px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.header-nav a{
  margin-right: 10px;
  padding: 7px;
  border-radius: 35px;
  background-color: dimgrey;
}

.container {
  margin: 0px 20px 20px 20px;
}

.logo {
  width: 30px;
  height: 30px;
}
</style>
