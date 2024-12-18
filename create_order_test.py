# Анастасия Сергеева, 24-я когорта — Финальный проект. Инженер по тестированию плюс

from sender_stand_request import create_order, get_order
import data

# Тест на создание нового заказа его получение
def test_order_creation():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    order_response = get_order(track_number)

# Проверка: код ответа равен 200
    assert order_response.status_code == 200, f"Ошибка при получении заказа: {order_response.status_code}"



