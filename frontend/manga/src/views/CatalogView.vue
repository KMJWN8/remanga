<script setup>
import FilterArea from '@/components/FilterArea.vue'
import TitleCardsList from '@/components/TitleCardsList.vue'

</script>

<template>
 <div>
  <h1>Каталог тайтлов</h1>
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
</style>

