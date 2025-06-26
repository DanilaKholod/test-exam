from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Dict
from enum import Enum

app = FastAPI()

class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"

class Student(BaseModel):
    first_name: str
    last_name: str
    group: str
    email: EmailStr
    status: StatusEnum

students: Dict[int, dict] = {}
student_id_counter = 1

@app.get("/students")
def get_all_students():
    return students

@app.get("/students/active")
def get_active_students():
    return {sid: s for sid, s in students.items() if s["status"] == StatusEnum.active}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

@app.post("/students")
def create_student(student: Student):
    global student_id_counter
    students[student_id_counter] = student.model_dump()
    student_id_counter += 1
    return {"message": "Student created", "id": student_id_counter - 1}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted"}
