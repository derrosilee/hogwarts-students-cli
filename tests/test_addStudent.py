import pytest
from student import Student

def test_add_student(monkeypatch):
    inputs = iter(["John", "Doe", "1234", "Jane Doe", "Gryffindor", "Male", "10"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('student.get_int', lambda _: int(next(inputs)))
    monkeypatch.setattr('student.get_house', lambda _: next(inputs))

    student = Student.add_student()
    assert student.first_name.capitalize() == "John"
    assert student.last_name.capitalize() == "Doe"
    assert student.admission_number == 1234
    assert student.guardian_name.title() == "Jane Doe"
    assert student.house.capitalize() == "Gryffindor"
    assert student.sex.capitalize() == "Male"
    assert student.grade == 10