from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_status_success():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "online"}

def test_get_status_wrong_url():
    response = client.get("/invalid_status")
    assert response.status_code == 404

def test_post_sensor_success():
    sensor_data = {
        "name": "TempSensor1",
        "location": "Greenhouse 1",
        "temperature": 23.5,
        "humidity": 45.0
    }
    response = client.post("/sensors", json=sensor_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_post_sensor_invalid_data():
    response = client.post("/sensors", json={"name": "BrokenSensor"})
    assert response.status_code == 422

def test_get_all_sensors_success():
    response = client.get("/sensors")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_all_sensors_wrong_method():
    response = client.post("/sensors")  # без тела — ошибка
    assert response.status_code in [422, 405]

def test_get_sensor_success():
    # Сначала создаём датчик
    sensor_data = {
        "name": "HumiditySensor",
        "location": "Zone A",
        "temperature": 22.1,
        "humidity": 50.2
    }
    post_response = client.post("/sensors", json=sensor_data)
    sensor_id = post_response.json()["id"]

    # Теперь получаем его
    get_response = client.get(f"/sensors/{sensor_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "HumiditySensor"

def test_get_sensor_not_found():
    response = client.get("/sensors/9999")
    assert response.status_code == 404

def test_delete_sensor_success():
    # Сначала создаём датчик
    sensor_data = {
        "name": "DeleteSensor",
        "location": "Zone X",
        "temperature": 25.0,
        "humidity": 40.0
    }
    post_response = client.post("/sensors", json=sensor_data)
    sensor_id = post_response.json()["id"]

    # Удаляем
    delete_response = client.delete(f"/sensors/{sensor_id}")
    assert delete_response.status_code == 200

def test_delete_sensor_not_found():
    response = client.delete("/sensors/9999")
    assert response.status_code == 404
