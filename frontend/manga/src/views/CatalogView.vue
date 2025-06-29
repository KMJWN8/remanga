<script setup>
import FilterArea from '@/components/FilterArea.vue'
import TitleCardsList from '@/components/TitleCardsList.vue'

</script>

<template>
 <div> 
  <div class="top-wrapper">
    <h1>Каталог тайтлов</h1>
    <div class="search-box">
      <input type="search" class="search-input" placeholder="Поиск по названию">
      <i class="pi pi-search"></i>
    </div>
  </div>
  <div class="catalog-wrapper">
   <TitleCardsList />
   <FilterArea />
  </div>
 </div>
</template>

<style scoped>
.catalog-wrapper {
  display: grid;
  grid-template-columns: 80% 20%;
}

.top-wrapper {
  display: grid;
  grid-template-columns: 2fr 1fr;
  width: 70%;
}

.search-box {
  position: relative;
  width: 100%;
}

.search-input {
  padding: 10px 10px 10px 35px;
  font-size: medium;
  border-radius: 10px;
  border: 1px solid #52525b;
  width: 100%;
  box-sizing: border-box;
}

.search-box .pi {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #6c757d;
  pointer-events: none;
  font-size: 1rem;
}
</style>

