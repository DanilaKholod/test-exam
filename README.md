# test-exam

## Описание

REST API сервер для управления студентами на FastAPI.

### Эндпоинты

- `GET /students` — получить список всех студентов
- `GET /students/active` — получить только активных студентов
- `GET /students/{id}` — получить информацию о студенте по ID
- `POST /students` — добавить нового студента
- `DELETE /students/{id}` — удалить студента

## Запуск через Docker

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

## Тестирование

1. **Выполните тесты внутри контейнера:**
   ```sh
   docker-compose run --rm app pytest test.py
   ```

   Или, если контейнер уже запущен:
   ```sh
   docker exec -it test-exam-app-1 pytest test.py
   ```

## Структура проекта

- `api.py` — основной код FastAPI приложения
- `test.py` — тесты для API
- `requirements.txt` — зависимости Python
- `Dockerfile` — сборка образа приложения
- `docker-compose.yml` — запуск приложения в контейнере