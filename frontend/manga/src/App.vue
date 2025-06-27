<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useTitleStore } from '@/stores/useTitleStore'

const titleStore = useTitleStore()

onMounted(() => {
  titleStore.loadTitles()
})

</script>

<template>
  <main>
    <header>
      <div class="header-container">

        <div class="logo">
          <RouterLink to="/">Home</RouterLink>
        </div>

        <nav class="header-nav">
          <span><RouterLink to="/catalog">Каталог</RouterLink></span>
          <span><a href="#">Топы</a></span>
        </nav>
          
        <a href="#" class="btn btn-login">Войти/Зарегистрироваться</a>
      </div>
    </header>

    <div>
         <RouterView />
    </div>

  </main>
</template>

<style>
* {
  margin: 0;
  padding: 0;
}

main {
    font-family: 'Newsreader', sans-serif;
}

header {
  background-color: black;
  padding:15px;
  width: 100%;
}

.header-container {
  max-width: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}

.header-nav {
  display: flex;
  flex-direction: row;
}

.header-nav span {
  margin-right: 10px;
  padding: 5px;
  border-radius: 5px;
  background-color: dimgrey;
}
</style>
