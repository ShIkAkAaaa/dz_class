class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
        self.courses_attached = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f"Имя : {self.name} \nФамилия : {self.surname}\nСредняя оценка за домашнее задание:{Student.average_rating(self)}\nКурсы в процессе изучения:{courses_in_progress_string}\nЗавершенные курсы:{finished_courses_string}"

    def average_rating(self):
        general_ball = 0
        for i in self.grades:
            general_ball += i
            average_score = general_ball / len(self.grades)
            return average_score

    def courses_studied(self):
        courses_studied = ''
        for i in self.finished_courses:
            courses_studied += i + ','
            return courses_studied

    def completed_courses(self):
        completed_courses = ''
        for i in self.finished_courses:
            completed_courses += i + ','
            return completed_courses


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя : {self.name} \nФамилия : {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        self.name = name
        self.surname = surname
        self.average_rating = float()
        self.courses_attached = []

    def average_rating(self):
        general_ball = 0
        for i in self.grades:
            general_ball += i
            average_score = general_ball / len(self.grades)
            return average_score

    def __str__(self):
        Lecturer.average_rating(self)
        return f"Имя : {self.name} \nФамилия : {self.surname}\nСредняя оценка за лекции: {Lecturer.average_rating(self)}"

    def __lt__(self, lector1):
        if not isinstance(lector1, Lecturer):
            print('Можно сравнивать только лекторов')
            return
        return self.average_rating > lector1.average_rating


# Лекторы
lec_soldatov = Lecturer('Виктор', 'Солдатов')
lec_pivenov = Lecturer('Семён', 'Пименов')
lec_soldatov.courses_attached += ['Python']
lec_pivenov.courses_attached += ['C++']

# Проверяющие
rev_clinkin = Reviewer('Егор', 'Клинкин')
rev_veshanov = Reviewer('Павел', 'Вешанов')
rev_clinkin.courses_attached += ['Python']
rev_clinkin.courses_attached += ['C++']
rev_clinkin.courses_attached += ['Python']
rev_veshanov.courses_attached += ['C++']

# Студенты
stud_ivanov = Student('Иванов', 'Петр', 'Мужчина')
stud_petrova = Student('Петрова', 'Вера', 'Женщина')
stud_ivanov.courses_in_progress += ['Python']
stud_petrova.courses_in_progress += ['C++']
stud_ivanov.finished_courses += ['Вводный курс']
stud_petrova.finished_courses += ['Вводный курс']

# Оценки для лекторов
stud_ivanov.rate_hw(lec_soldatov, 'Python', 10)
stud_ivanov.rate_hw(lec_soldatov, 'Python', 10)
stud_ivanov.rate_hw(lec_soldatov, 'Python', 10)

stud_ivanov.rate_hw(lec_pivenov, 'C++', 5)
stud_ivanov.rate_hw(lec_pivenov, 'C++', 7)
stud_ivanov.rate_hw(lec_pivenov, 'C++', 8)

stud_petrova.rate_hw(lec_soldatov, 'Python', 7)
stud_petrova.rate_hw(lec_soldatov, 'Python', 8)
stud_petrova.rate_hw(lec_soldatov, 'Python', 9)

stud_petrova.rate_hw(lec_pivenov, 'C++', 10)
stud_petrova.rate_hw(lec_pivenov, 'C++', 8)
stud_petrova.rate_hw(lec_pivenov, 'C++', 9)

# Оценки для студентов
rev_clinkin.rate_hw(stud_ivanov, 'Python', 8)
rev_clinkin.rate_hw(stud_ivanov, 'Python', 9)
rev_clinkin.rate_hw(stud_ivanov, 'Python', 10)

rev_clinkin.rate_hw(stud_petrova, 'Java', 8)
rev_clinkin.rate_hw(stud_petrova, 'Java', 7)
rev_clinkin.rate_hw(stud_petrova, 'Java', 9)

# Функция для подсчета оценки за д.з. по всем заданиям в рамках курса

student_list = [stud_ivanov, stud_petrova]


def stud_average_rating(stud_list, course_name):
    """Функция для подсчёта средней оценки за домашнее         задание по всем студентам в рамках конкретного курса       (в качестве аргументов принимаем список студентов и         название курса"""

    summa_all = 0
    total_number = 0
    for student in student_list:
        if student.courses_in_progress == [course_name]:
            summa_all += student.average_rating
            total_number += 1
    average_all = summa_all / total_number
    return average_all


# Функция для подсчёта средний оценки всех лекторов

lecturer_list = [lec_soldatov, lec_pivenov]


def lect_average_rating(lecturer_list, course_name):
    """Функция для подсчета средней оценки за лекции всех      лекторов в рамках курса (в качестве аргумента              принимает     список лекторов и название курса)"""

    summa_all = 0
    total_number = 0
    for lector in lecturer_list:
        if lector.courses_attached == [course_name]:
            summa_all += lector.average_rating
            total_number += 1
    average_all = summa_all / total_number
    return average_all

