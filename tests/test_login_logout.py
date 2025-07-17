# Тесты логина и логаута
from src.test_base import BaseUserTest


class TestLoginLogout(BaseUserTest):

    def test_login_logout_success(self, fake_user_data):
        # Выводим, какие данные отправляем
        print("Создание пользователя с данными:", fake_user_data)

        # Создаем пользователя
        create_response = self.create_user(fake_user_data)
        print("Статус-код ответа на создание:", create_response.status_code)
        print("Ответ сервера на создание (JSON):", create_response.json())

        # Логинимся
        login_response = self.login_user(fake_user_data["username"], fake_user_data["password"])
        print("Статус-код ответа на логин:", login_response.status_code)
        print("Ответ сервера на логин (текст):", login_response.text)
        assert login_response.status_code == 200
        assert "logged in user session" in login_response.text

        # Логаут
        logout_response = self.logout_user()
        print("Статус-код ответа на логаут:", logout_response.status_code)
        print("Ответ сервера на логаут (текст):", logout_response.text)
        assert logout_response.status_code == 200
