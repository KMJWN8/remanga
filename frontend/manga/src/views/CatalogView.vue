<script setup>

import FilterArea from '@/components/FilterArea.vue'

import TitleCardsList from '@/components/TitleCardsList.vue'

</script>

<template>
 <div class="card-and-filter-cointainer">
  <h1>Каталог тайтлов</h1>
  <div class="wrapper">
   <TitleCardsList />
   <FilterArea class="filter-area"/>
  </div>
 </div>
</template>

<style scoped>
.card-and-filter-cointainer {
  margin: 20px;
}

.wrapper {
  display: grid;
  grid-template-columns: 80% 20%;
}

.filter-area {
  margin-left: 50px;
}
</style>

