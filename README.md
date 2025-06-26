# 2 Вариант: Система управления студентами

## 📘 Описание

REST API-сервер на FastAPI для управления студентами. Позволяет добавлять новых студентов, получать списки всех и только активных студентов, получать информацию по ID, а также удалять студентов.

---

## 🚀 Эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/students` | Получить список всех студентов |
| GET | `/students/active` | Получить список активных студентов |
| GET | `/students/{id}` | Получить информацию о студенте по ID |
| POST | `/students` | Добавить нового студента |
| DELETE | `/students/{id}` | Удалить студента по ID |

---

## 🧾 Формат данных студента

```json
{
  "first_name": "Ivan",
  "last_name": "Ivanov",
  "group": "М24-Ш04",
  "email": "ivan@example.com",
  "is_active": true
}
```

## 🐳 Запуск через Docker

1. **Склонируйте репозиторий:**
   ```sh
   git clone <адрес-репозитория>
   cd test-exam
   ```

2. **Постройте и запустите контейнеры:**
   ```sh
   docker-compose up --build
   ```

3. **API будет доступен по адресу:**  
   [http://localhost:8000](http://localhost:8000)

4. **Документация Swagger:**  
   [http://localhost:8000/docs](http://localhost:8000/docs)

## 🐳 Тестирование в Docker

1. **Выполните тесты внутри контейнера:**
   ```sh
   docker-compose run --rm app pytest test.py
   ```

   Или, если контейнер уже запущен:
   ```sh
   docker exec -it test-exam-app-1 pytest test.py
   ```

## ⚙️ Установка и запуск без Docker

1. **Склонируйте репозиторий:**
   ```sh
   git clone <адрес-репозитория>
   cd test-exam
   ```

2. **Постройте и запустите контейнеры:**
   ```sh
   python -m venv venv
   source venv/bin/activate     
   ```

3. **Установите зависимости:**
   ```sh
   pip install -r requirements.txt    
   ```

4. **Запустите сервер:**
   ```sh
   uvicorn api:app --reload   
   ```

5. **API будет доступен по адресу:**  
   [http://localhost:8000](http://localhost:8000)

6. **Документация Swagger:**  
   [http://localhost:8000/docs](http://localhost:8000/docs)

## ✅ Тестирование

1. **С Docker:**
   ```sh
   docker-compose run --rm app pytest test.py
   ```

   Или, если контейнер уже запущен:
   ```sh
   docker exec -it test-exam-app-1 pytest test.py
   ```

2. **Без Docker:**
   ```sh
   pytest test.py
   ```

## Структура проекта

- `api.py` — основной код FastAPI приложения
- `test.py` — тесты для API
- `requirements.txt` — зависимости Python
- `Dockerfile` — сборка образа приложения
- `docker-compose.yml` — запуск приложения в контейнере