#    Анастасия Сергеева, 24-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post (configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_url_order = f"{configuration.BASE_URL}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_url_order)
    return response

# Тест
def test_order_creation():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Тест пройден. Заказ создан. Номер трека:", track_number)

# Получение данных заказа по треку
    order_response = get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа: ")
    print(order_data)