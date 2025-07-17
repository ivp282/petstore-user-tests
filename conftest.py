# Фикстура для генерации случайных данных пользователя

import pytest
from faker import Faker

fake = Faker()

@pytest.fixture
def fake_user_data():
    return {
        "id": fake.random_int(min=1, max=999999),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number(),
        "userStatus": 1
    }