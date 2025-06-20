<script setup>

</script>

<template>
    <div class="card">
        <img 
          src="@/assets/tmp_pics/m_dom.jpg" 
          alt="Милый дом"
        >
        <span>Type, year of release</span>
        <p>Name</p>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    max-width: 200px;
    margin: 16px auto;
}

.card img {
    display: block;
    width: 100%;
    max-width: 200px;
    height: auto;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 12px;
    background: #f2f2f2;
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