from dataclasses import dataclass

from dacite import MissingValueError, WrongTypeError, from_dict


@dataclass
class Child:
    number: int
    text: str


@dataclass
class Parent:
    number: int
    text: str
    child: Child


def instantiate(d):
    try:
        p = from_dict(Parent, d)
        print(p)
    except MissingValueError as e:
        print(f"Missing value. field: {e.field_path}")
    except WrongTypeError as e:
        print(f"Wrong type. field: {e.field_path}, value: {e.value}")


ok = {
    "number": 111,
    "text": "ttt",
    "child": {"number": 222, "text": "xxx"},
}

missing_value = {
    "number": 111,
    "child": {"number": 222, "text": "xxx"},
}

wrong_type = {
    "number": "ttt",
    "text": "ttt",
    "child": {"number": 222, "text": "xxx"},
}

for d in [ok, missing_value, wrong_type]:
    instantiate(d)
