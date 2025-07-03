<script setup>
import TitleCard from './TitleCard.vue'
import LoaderIcon from '@/components/LoaderIcon.vue'

import { useTitleStore } from '@/stores/useTitleStore'
import { storeToRefs } from 'pinia'

const titleStore = useTitleStore()

const { loading, error, titles } = storeToRefs(titleStore)

</script>

<template>
  <div>
    <div v-if="loading">
      <LoaderIcon />
    </div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else class="title-list">
      <TitleCard
          v-for="title in titles" :key="title.id"
          :manga="title"    
      />
    </div>
  </div>
</template>

<style scoped>
.title-list {
    display: grid;
    grid-template-columns: repeat(5, 20%);
}
</style>