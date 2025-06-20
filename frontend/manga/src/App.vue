<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <main>
    <header>
      <div class="container">

        <div class="logo">
          <RouterLink to="/">Home</RouterLink>
        </div>

        <nav class="main-nav">
          <span><RouterLink to="/catalog">Каталог</RouterLink></span>
          <span><a href="#">Топы</a></span>
        </nav>
          
        <a href="/login" class="btn btn-login">Войти/Зарегистрироваться</a>
      </div>
    </header>

    <div>
      
    </div>
  
  <RouterView />
  </main>
</template>

<style scoped>
header {
  background-color: black;
  padding:15px;
  width: 100%;
}

.container {
  max-width: auto;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}

.main-nav {
  display: flex;
  flex-direction: row;
}

.main-nav span {
  margin-right: 10px;
  padding: 5px;
  border-radius: 5px;
  background-color: dimgrey;
}
</style>
