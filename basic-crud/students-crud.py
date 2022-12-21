from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# mock DB
students_repo = {
    0: {
        "first_name": "bob",
        "last_name": "bobbin",
        "age": 30,
        "year": "1"
    },
    1: {
        "first_name": "mary",
        "last_name": "sue",
        "age": 25,
        "year": "2"
    }
}


class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    year: str


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"data": "student CRUD operations"}


# path parameter
@app.get("/students/{student_id}")
def students(student_id: int = Path(None, description="ID of the student", ge=0, lt=10)):
    if student_id in students_repo:
        return students_repo[student_id]

    return {"error": "Student not found"}


# query parameter
# foo = None makes it not required
@app.get("/get-student")
def get_student(name: Optional[str] = None, year: Optional[str] = None):
    for i in students_repo:
        if students_repo[i]["first_name"] == name or students_repo[i]["year"] == year:
            return students_repo[i]

    return {"data": "not found"}


@app.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student):
    if student_id in students_repo:
        return {"error": "Student already exists"}

    students_repo[student_id] = student

    return students_repo[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students_repo:
        return {"error": "Student does not exist."}

    if student.first_name != None:
        students_repo[student_id].first_name = student.first_name

    return students_repo[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_repo:
        return {"error": "Student does not exist"}

    del students_repo[student_id]

    return {"data": "Student delete successfully"}
