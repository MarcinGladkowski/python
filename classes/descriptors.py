from weakref import WeakKeyDictionary

"""
* Sometimes better descriptor will be better than @property decorator
* WeakKeyDictionary prevent to memory leaks
"""


class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('The grade have to be between 0 and 100')
        self._grade = value


class Exam:
    def __init__(self):
        self._writing_grade = Grade()
        self._math_grade = Grade()
        self._science_grade = Grade()

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('The grade have to be between 0 and 100')


galileo = Homework()
galileo.grade = 95


class Grade:
    """
    This class implementing descriptor
    """
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        # once time - not in each class to check this value!
        if not (0 <= value <= 100):
            raise ValueError('The grade have to be between 0 and 100')
        self._values[instance] = value


first_exam = Exam()
"""
Exam.__dict__['writing_grade'].__set__(exam, 40)
Exam.__dict__['writing_grade'].__get__(exam, Exam)
"""
first_exam.writing_grade = 82

second_exam = Exam()
second_exam.writing_grade = 20

print(first_exam.writing_grade)
