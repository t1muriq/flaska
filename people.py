# people.py
from flask import abort # импорт функции abort из Flask

from datetime import datetime

# функция, возвращающая текущее время в заданном формате
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        # использование abort() помогает отправить сообщение об ошибке
        # когда тело запроса не содержит фамилию или когда персонаж с такой
        # фамилией уже существует.
        abort(
            406,
            f"Person with last name {lname} already exists",
        )

# словарь со значениями Персонажей
PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

# сервер запускает эту функцию при вызове /api/people
def read_all():
    return list(PEOPLE.values())