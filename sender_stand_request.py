# Анастасия Сергеева, 24-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests

# Запрос на создание нового заказа
def create_order(body):
    return requests.post (configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body)

# Запрос на получение заказа по сохраненному треку
def get_order(track_number):
    url = f"{configuration.BASE_URL}/api/v1/orders/track?t={track_number}"
    response = requests.get(url)
    return response





