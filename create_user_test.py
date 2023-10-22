# Алиса Быстрова, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request
def create_order():
    current_body = data.order_body.copy()
    current_body["firstName"] = "Alicefox"
    track_num = sender_stand_request.post_new_order(current_body)
    return str(track_num.json()["track"])
def positive_assert():
    track_num = create_order()
    current_params = data.params_get.copy()
    current_params["t"] = track_num
    response = sender_stand_request.get_order(current_params)
    assert response.status_code == 200

def test_order():
    positive_assert()