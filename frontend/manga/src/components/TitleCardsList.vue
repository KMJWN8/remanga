<script setup>
import TitleCard from './TitleCard.vue'
</script>

<template>
    <div>
        
        <TitleCard 
          v-for="manga in mangaList"
          :key="manga.id"
          />    
    </div>
</template>

<style scoped>

</style>