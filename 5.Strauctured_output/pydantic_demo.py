from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = "Salman"
    age : Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4, default=3, description='Decimal representation of cgpa')

new_student = {'age': 32, 'email': "abc@gmail.com", 'cgpa': 3.5}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])