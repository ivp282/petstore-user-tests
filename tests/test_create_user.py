# Тесты создания пользователя
from src.test_base import BaseUserTest


class TestCreateUser(BaseUserTest):

    def test_create_user_success(self, fake_user_data):
        # Выводим, какие данные отправляем
        print("Создание пользователя с данными:", fake_user_data)

        # Отправляем запрос
        response = self.create_user(fake_user_data)

        # Выводим статус и JSON-ответ от сервера
        print("Статус-код ответа на создание:", response.status_code)
        print("Ответ сервера на создание (JSON):", response.json())

        # Проверки
        assert response.status_code == 200 or response.status_code == 201
        assert response.json()["message"] == str(fake_user_data["id"])
