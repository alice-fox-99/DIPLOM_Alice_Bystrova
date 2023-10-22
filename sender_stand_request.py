# Алиса Быстрова, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


def get_order(parameter):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params=parameter)