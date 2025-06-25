from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from datetime import datetime, UTC

app = FastAPI()

# Модель данных
class Sensor(BaseModel):
    name: str
    location: str
    temperature: float
    humidity: float

# Хранилище данных
sensors: Dict[int, dict] = {}
sensor_id_counter = 1

# Получить статус сервера
@app.get("/status")
def get_status():
    return {"status": "online"}

# Получить список всех датчиков
@app.get("/sensors")
def get_all_sensors():
    return sensors

# Получить данные одного датчика по ID
@app.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: int):
    if sensor_id not in sensors:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensors[sensor_id]

# Добавить новый датчик
@app.post("/sensors")
def create_sensor(sensor: Sensor):
    global sensor_id_counter
    sensor_data = sensor.model_dump()
    sensor_data["timestamp"] = datetime.now(UTC).isoformat()
    sensors[sensor_id_counter] = sensor_data
    sensor_id_counter += 1
    return {"message": "Sensor created", "id": sensor_id_counter - 1}

# Удалить датчик
@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int):
    if sensor_id not in sensors:
        raise HTTPException(status_code=404, detail="Sensor not found")
    del sensors[sensor_id]
    return {"message": "Sensor deleted"}
