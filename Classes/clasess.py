class SimpleGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades)/len(grades)


book = SimpleGradeBook()
book.add_student('Marcin')
book.report_grade('Marcin', 6)
book.report_grade('Marcin', 5)
book.report_grade('Marcin', 3)
print(book.average_grade('Marcin'))

# p.156