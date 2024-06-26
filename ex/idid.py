from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person(name='John', age=30)
print(p.name)  # John
print(p.age)   # 30
