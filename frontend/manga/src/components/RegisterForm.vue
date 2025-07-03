<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/useAuthStore'
  
defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:modelValue', 'open-login'])

const openLogin = () => {
  closeModal()
  emit('open-login')
}

const closeModal = () => {
  emit('update:modelValue', false)
}

const authStore = useAuthStore()

const email = ref('')
const username = ref('')
const password = ref('')
const re_password = ref('')

const onSubmit = async () => {
  try {
    await authStore.register(email.value, username.value, password.value, re_password.value)
  } catch {
    alert(authStore.error)
  }
  openLogin()
}
</script>

<template>
  <div>
    <div v-if="modelValue" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <button class="btn-close" @click="closeModal">&times;</button>
        <h2>Регистрация</h2>
  
        <form @submit.prevent="onSubmit" class="login-form">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="email" 
            type="email"
            placeholder="Введите email"
            required
          />

          <label for="username">Логин</label>
          <input
            id="username"
            v-model="username"
            type="text"
            placeholder="Введите логин"
            required
          />

          <label for="password">Пароль</label>
          <input
            id="password"
            v-model="password"
            type="password"
            placeholder="Введите пароль"
            required
          />

          <label for="re_password">Подтверждение пароля</label>
          <input
            id="re_password"
            v-model="re_password"
            type="password"
            placeholder="Введите пароль"
            required
          />
          <button type="submit" class="btn-submit">Войти</button>
        </form>
        <div class="bottom-text">
          <p>Уже есть аккаунт?</p>
          <a href="#" @click.prevent="openLogin">Войти</a>
        </div>
      </div>
    </div>
  </div>
</template>
  
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
    background: #212121;
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
    color: #f2f2f2;
  }
  
  /* Форма */
  .login-form label {
    display: block;
    margin-bottom: 6px;
    font-weight: 600;
    color: #f2f2f2;
  }
  
  .login-form input {
    width: 100%;
    padding: 10px 12px;
    margin-bottom: 18px;
    border: 1px solid #52525b;
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box;
    transition: border-color 0.3s;
  }
  
  .login-form input:focus {
    border-color: #D81F26;
    outline: none;
  }
  
  /* Кнопка отправки */
  .btn-submit {
    width: 100%;
    padding: 10px;
    background-color: #D81F26;
    border: none;
    border-radius: 4px;
    color: white;
    font-weight: 700;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
.btn-submit:hover {
  background-color: #fa030b;
}

.bottom-text {
  display: grid;
  grid-template-columns: 3fr 1fr;
  margin-top: 10px;
}

a {
  text-decoration: underline;
  color: #D81F26;
}
</style>
  