from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_all_students_empty():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == {}

def test_create_student_success():
    student_data = {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "group": "CS-101",
        "email": "ivanov@example.com",
        "is_active": True
    }
    response = client.post("/students", json=student_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["message"] == "Student created"

def test_create_student_invalid_data():
    # Missing required fields
    response = client.post("/students", json={"first_name": "NoLastName"})
    assert response.status_code == 422

def test_get_all_students_nonempty():
    # Add a student first
    student_data = {
        "first_name": "Petr",
        "last_name": "Petrov",
        "group": "CS-102",
        "email": "petrov@example.com",
        "is_active": False
    }
    post_response = client.post("/students", json=student_data)
    student_id = post_response.json()["id"]

    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()
    assert str(student_id) in map(str, students.keys())

def test_get_active_students():
    # Add active and inactive students
    client.post("/students", json={
        "first_name": "Anna",
        "last_name": "Smirnova",
        "group": "CS-103",
        "email": "anna@example.com",
        "is_active": True
    })
    client.post("/students", json={
        "first_name": "Oleg",
        "last_name": "Sidorov",
        "group": "CS-104",
        "email": "oleg@example.com",
        "is_active": False
    })
    response = client.get("/students/active")
    assert response.status_code == 200
    active_students = response.json()
    for student in active_students.values():
        assert student["is_active"] is True

def test_get_student_success():
    student_data = {
        "first_name": "Maria",
        "last_name": "Kuznetsova",
        "group": "CS-105",
        "email": "maria@example.com",
        "is_active": True
    }
    post_response = client.post("/students", json=student_data)
    student_id = post_response.json()["id"]

    get_response = client.get(f"/students/{student_id}")
    assert get_response.status_code == 200
    student = get_response.json()
    assert student["first_name"] == "Maria"
    assert student["email"] == "maria@example.com"

def test_get_student_not_found():
    response = client.get("/students/9999")
    assert response.status_code == 404

def test_delete_student_success():
    student_data = {
        "first_name": "Sergey",
        "last_name": "Sergeev",
        "group": "CS-106",
        "email": "sergey@example.com",
        "is_active": False
    }
    post_response = client.post("/students", json=student_data)
    student_id = post_response.json()["id"]

    delete_response = client.delete(f"/students/{student_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Student deleted"

def test_delete_student_not_found():
    response = client.delete("/students/9999")
    assert response.status_code == 404
