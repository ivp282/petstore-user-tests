# Тесты обновления пользователя
from src.test_base import BaseUserTest
from conftest import fake


class TestUpdateUser(BaseUserTest):

    def test_update_user_success(self, fake_user_data):
        # Выводим, какие данные отправляем
        print("Создание пользователя с данными:", fake_user_data)
        
        # Создаем пользователя
        create_response = self.create_user(fake_user_data)
        print("Статус-код ответа на создание:", create_response.status_code)
        print("Ответ сервера на создание (JSON):", create_response.json())

        # Обновляем все поля, кроме id и username
        updated_data = {
            "id": fake_user_data["id"],  # оставляем прежний id
            "username": fake_user_data["username"],  # оставляем прежний username
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(),
            "phone": fake.phone_number(),
            "userStatus": fake.random_int(min=0, max=1)
        }
        
        print("Отправка обновлённых данных:", updated_data)

        response = self.update_user(fake_user_data["username"], updated_data)
        # Выводим статус и JSON-ответ от сервера
        print("Статус-код ответа на обновление:", response.status_code)
        print("Ответ сервера на обновление (JSON):", response.json())
        assert response.status_code == 200
