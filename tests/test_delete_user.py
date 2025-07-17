# Тесты удаления пользователя
from src.test_base import BaseUserTest


class TestDeleteUser(BaseUserTest):

    def test_delete_user_success(self, fake_user_data):
        # Выводим, какие данные отправляем
        print("Создание пользователя с данными:", fake_user_data)

        # Отправляем запрос на создание
        create_response = self.create_user(fake_user_data)

        # Выводим статус и JSON-ответ от сервера
        print("Статус-код ответа на создание:", create_response.status_code)
        print("Ответ сервера на создание (JSON):", create_response.json())

        # Проверка успешного создания
        assert create_response.status_code == 200

        # Отправляем запрос на удаление
        delete_response = self.delete_user(fake_user_data["username"])

        # Выводим статус и JSON-ответ от сервера
        print("Статус-код ответа на удаление:", delete_response.status_code)
        print("Ответ сервера на удаление (JSON):", delete_response.json())

        # Проверка успешного удаления
        assert delete_response.status_code == 200
