# Базовый класс с общими методами

import requests

BASE_URL = "https://petstore.swagger.io/v2"

class BaseUserTest:
    # Создание пользователя
    def create_user(self, user_data):
        return requests.post(f"{BASE_URL}/user", json=user_data)
        
    # Получение пользователя по имени
    def get_user(self, username):
        return requests.get(f"{BASE_URL}/user/{username}")
        
    # Обновление данных пользователя
    def update_user(self, username, updated_data):
        return requests.put(f"{BASE_URL}/user/{username}", json=updated_data)
        
    # Удаление пользователя
    def delete_user(self, username):
        return requests.delete(f"{BASE_URL}/user/{username}")
        
    # Логин пользователя (возвращает токен сессии)
    def login_user(self, username, password):
        return requests.get(f"{BASE_URL}/user/login", params={"username": username, "password": password})
        
    # Выход пользователя из системы
    def logout_user(self):
        return requests.get(f"{BASE_URL}/user/logout")
