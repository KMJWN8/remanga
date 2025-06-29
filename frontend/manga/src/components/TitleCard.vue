<script setup>

defineProps({
    manga: {
        type: Object,
        required: true
    }
})

</script>

<template>
  <router-link :to="{name: 'titleDetail', params: {id: manga.id}}">
    <div class="card">
      <img src="@/assets/tmp_pics/2.webp" alt="Милый дом">
      <span>{{ manga.type.name }} {{ manga.year_released }}</span>
      <p>{{ manga.name }}</p>
    </div>
  </router-link>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    max-width: 180px;
    margin: 10px auto;
}

.card img {
    width: 100%;
    max-height: 250px;
    height: auto;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 5px;
}

.card p {
    margin: 4px 0;
    color: #f2f2f2;
    font-size: 14px;
    text-align: start;
}

.card span {
    margin: 4px 0;
    color: darkgrey;
    font-size: 12px;
    text-align: start;
}
</style>