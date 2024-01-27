import pytest

from salary import generate_salary_report, Employee


def test_salary():
    bartek = Employee("Bartosz", 100, 40)
    report = generate_salary_report([bartek])
    assert type(report) is dict     #assert isinstance(report, dict)
    assert report == {
        "Bartosz": {
            "salary": 4000,
            "hours_worked": 40
        },
        "total_expenses": 4000.0
    }


def test_not_employees():
    with pytest.raises(ValueError):
        generate_salary_report([])


def test_name_not_string():
    employee = Employee(12, "100", 40)
    with pytest.raises(ValueError):
        generate_salary_report([employee])


def test_hours():
    employee = Employee("Bartosz", -1, 0)
    with pytest.raises(ValueError):
        generate_salary_report([employee])


def test_hours_overtime():
    employee = Employee("Bartosz", 40, 50)
    generate_salary_report([employee])

