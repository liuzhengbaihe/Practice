from collections import deque

def student(name, homeworks):
    for homework in homeworks.items():
        yield(name, homework[0], homework[1])

class Teacher(object):

    def __init__(self, students):
        self.students = deque(students)

    def handle(self):

