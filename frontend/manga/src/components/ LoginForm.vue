<template>
    <div>
      <!-- Кнопка для открытия модального окна -->
      <button @click="showModal = true" class="btn-open">Войти</button>
  
      <!-- Модальное окно -->
      <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
        <div class="modal">
          <button class="btn-close" @click="closeModal">&times;</button>
          <h2>Вход в аккаунт</h2>
  
          <form @submit.prevent="onSubmit" class="login-form">
            <label for="username">Логин</label>
            <input
              id="username"
              v-model="form.username"
              type="text"
              placeholder="Введите логин"
              required
            />
  
            <label for="password">Пароль</label>
            <input
              id="password"
              v-model="form.password"
              type="password"
              placeholder="Введите пароль"
              required
            />
  
            <button type="submit" class="btn-submit">Войти</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive, ref } from 'vue'
  
  const showModal = ref(false)
  
  const form = reactive({
    username: '',
    password: '',
  })
  
  function closeModal() {
    showModal.value = false
  }
  
  function onSubmit() {
    alert(`Логин: ${form.username}\nПароль: ${form.password}`)
    // Здесь добавьте логику аутентификации
    closeModal()
  }
  </script>
  
  <style scoped>
  /* Кнопка открытия */
  .btn-open {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  
  /* Оверлей модального окна */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  /* Само модальное окно */
  .modal {
    background: white;
    padding: 30px 40px;
    border-radius: 8px;
    width: 320px;
    position: relative;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
  
  /* Кнопка закрытия */
  .btn-close {
    position: absolute;
    top: 10px;
    right: 15px;
    border: none;
    background: transparent;
    font-size: 24px;
    cursor: pointer;
  }
  
  /* Заголовок */
  .modal h2 {
    margin-bottom: 20px;
    text-align: center;
    color: #333;
  }
  
  /* Форма */
  .login-form label {
    display: block;
    margin-bottom: 6px;
    font-weight: 600;
    color: #555;
  }
  
  .login-form input {
    width: 100%;
    padding: 10px 12px;
    margin-bottom: 18px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box;
    transition: border-color 0.3s;
  }
  
  .login-form input:focus {
    border-color: #007bff;
    outline: none;
  }
  
  /* Кнопка отправки */
  .btn-submit {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    border: none;
    border-radius: 4px;
    color: white;
    font-weight: 700;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .btn-submit:hover {
    background-color: #0056b3;
  }
  </style>
  