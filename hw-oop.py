class Student:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.average_grades = float()

  def add_finished_courses(self, course_name):
      self.finished_courses.append(course_name)
      if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)

  def add_courses_in_progress(self, course_name):
      self.courses_in_progress.append(course_name)

  def rate_lec(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
            (course in self.courses_in_progress or course in self.finished_courses):
        if course in lecturer.grades:
           lecturer.grades[course] += [grade]
        else:
           lecturer.grades[course] = [grade]
    else:
          return 'Ошибка'

  def __len__(self):
      return len(self.grades)

  def __lt__(self, other):
      if not isinstance(other, Student):
          print('Не студент!')
          return
      return self.average_grades < other.average_grades

  def __str__(self):
      grades_count = 0
      for k in self.grades:
          grades_count += len(self.grades[k])
      self.average_grades = sum(map(sum, self.grades.values())) / grades_count
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average_grades,2)}\n" \
           f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"


class Mentor:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

  def add_courses_attached(self, course_name):
      self.courses_attached.append(course_name)


class Lecturer(Mentor):

  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}
    self.average_grades = float()

  def __len__(self):
      return len(self.__grades)

  def average_grade(self):
    s = 0
    for grade in self.grades:
        s += grade
    return s/len(grades)

  def __str__(self):
      grades_count = 0
      for k in self.grades:
          grades_count += len(self.grades[k])
      self.average_grades = sum(map(sum, self.grades.values())) / grades_count
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average_grades,2)}"

  def __lt__(self, other):
      if not isinstance(other, Lecturer):
          print('Не лектор!')
          return
      return self.average_grades < other.average_grades


class Reviewer(Mentor):
    def __init__(self, name, surname):
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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


Mickey_Mouse = Student('Mickey', 'Mouse')
Lilo_Pelekai = Student('Lilo', 'Pelekai')
Hulk = Student('', 'Hulk')

Heinz_Doofenshmirtz = Lecturer('Heinz', 'Doofenshmirtz')
Lola_Bunny = Lecturer('Lola', 'Bunny')
Scrooge_McDuck = Lecturer ('Scrooge', 'McDuck')

Scooby_Doo = Reviewer('Scooby', 'Doo')
Velma_Dinkley  = Reviewer('Velma ', 'Dinkley')
Gumball_Watterson = Reviewer('Gumball', 'Watterson')

Mickey_Mouse.add_finished_courses('Math')
Mickey_Mouse.add_finished_courses('Computer_Science')
Lilo_Pelekai.add_finished_courses('Math')
Lilo_Pelekai.add_finished_courses('Computer_Science')
Hulk.add_finished_courses('Math')
Hulk.add_finished_courses('Computer_Science')

Mickey_Mouse.add_courses_in_progress("Physics")
Lilo_Pelekai.add_courses_in_progress("Physics")
Hulk.add_courses_in_progress("Physics")

Heinz_Doofenshmirtz.add_courses_attached('Math')
Lola_Bunny.add_courses_attached('Physics')
Scrooge_McDuck.add_courses_attached('Computer_Science')

Scooby_Doo.add_courses_attached('Math')
Velma_Dinkley.add_courses_attached('Physics')
Gumball_Watterson.add_courses_attached('Computer_Science')

Scooby_Doo.rate_hw(Mickey_Mouse, "Math", 10)
Scooby_Doo.rate_hw(Mickey_Mouse, "Math", 8)
Scooby_Doo.rate_hw(Mickey_Mouse, "Math", 7)
Scooby_Doo.rate_hw(Lilo_Pelekai, "Math", 2)
Scooby_Doo.rate_hw(Lilo_Pelekai, "Math", 6)
Scooby_Doo.rate_hw(Lilo_Pelekai, "Math", 5)
Scooby_Doo.rate_hw(Hulk, "Math", 10)
Scooby_Doo.rate_hw(Hulk, "Math", 3)
Scooby_Doo.rate_hw(Hulk, "Math", 10)

Velma_Dinkley.rate_hw(Mickey_Mouse, "Physics", 6)
Velma_Dinkley.rate_hw(Mickey_Mouse, "Physics", 6)
Velma_Dinkley.rate_hw(Lilo_Pelekai, "Physics", 3)
Velma_Dinkley.rate_hw(Lilo_Pelekai, "Physics", 3)
Velma_Dinkley.rate_hw(Hulk, "Physics", 10)
Velma_Dinkley.rate_hw(Hulk, "Physics", 3)

Gumball_Watterson.rate_hw(Mickey_Mouse, "Computer_Science", 10)
Gumball_Watterson.rate_hw(Mickey_Mouse, "Computer_Science", 10)
Gumball_Watterson.rate_hw(Mickey_Mouse, "Computer_Science", 10)
Gumball_Watterson.rate_hw(Mickey_Mouse, "Computer_Science", 10)
Gumball_Watterson.rate_hw(Lilo_Pelekai, "Computer_Science", 2)
Gumball_Watterson.rate_hw(Lilo_Pelekai, "Computer_Science", 3)
Gumball_Watterson.rate_hw(Lilo_Pelekai, "Computer_Science", 4)
Gumball_Watterson.rate_hw(Lilo_Pelekai, "Computer_Science", 5)
Gumball_Watterson.rate_hw(Hulk, "Computer_Science", 10)
Gumball_Watterson.rate_hw(Hulk, "Computer_Science", 3)
Gumball_Watterson.rate_hw(Hulk, "Computer_Science", 10)
Gumball_Watterson.rate_hw(Hulk, "Computer_Science", 3)

Mickey_Mouse.rate_lec(Heinz_Doofenshmirtz, "Math", 9)
Mickey_Mouse.rate_lec(Lola_Bunny, 'Physics', 9)
Mickey_Mouse.rate_lec(Scrooge_McDuck, "Computer_Science", 9)
Lilo_Pelekai.rate_lec(Heinz_Doofenshmirtz, "Math", 3)
Lilo_Pelekai.rate_lec(Lola_Bunny, 'Physics', 3)
Lilo_Pelekai.rate_lec(Scrooge_McDuck, "Computer_Science", 3)
Hulk.rate_lec(Heinz_Doofenshmirtz, "Math", 10)
Hulk.rate_lec(Lola_Bunny, 'Physics', 3)
Hulk.rate_lec(Scrooge_McDuck, "Computer_Science",6 )

students =[Mickey_Mouse, Lilo_Pelekai, Hulk ]
lectors = [Heinz_Doofenshmirtz, Lola_Bunny, Scrooge_McDuck]

print(f'Сравнение студентов по успеваемости:'
        f' {Mickey_Mouse.name} {Mickey_Mouse.surname} < {Lilo_Pelekai.name} {Lilo_Pelekai.surname} = '
        f'{Mickey_Mouse < Lilo_Pelekai} ')
print()
print(f'Сравнение лекторов по оценкам за лекции:'
        f' {Heinz_Doofenshmirtz.name} {Heinz_Doofenshmirtz.surname} < {Scrooge_McDuck.name} {Scrooge_McDuck.surname} = '
        f'{Heinz_Doofenshmirtz < Scrooge_McDuck} ')
print()


print(Mickey_Mouse,"\n")
print(Lilo_Pelekai, "\n")
print(Hulk, "\n")
print(Heinz_Doofenshmirtz, "\n")
print(Lola_Bunny, "\n")
print(Scrooge_McDuck, "\n")
print(Scooby_Doo, "\n")
print(Velma_Dinkley, "\n")
print(Gumball_Watterson, "\n")

def students_average_on_course(students, course_name):
    sum_of_students = 0
    count = 0
    for student in students:
        if student.courses_in_progress == [course_name]:
            for grade in student.grades[course_name]:
                sum_of_students += grade
                count +=1
        if student.finished_courses == [course_name]:
            for grade in student.grades[course_name]:
                sum_of_students += grade
                count +=1
    return sum_of_students / count

print(f"Средняя оценка за домашние задания по всем студентам по предмету")
print(round(students_average_on_course(students,"Physics"),2))

def lectors_average_on_course(lectors, course_name):
    sum_of_marks = 0
    count = 0
    for lector in lectors:
        if lector.courses_attached == [course_name]:
            for grade in lector.grades[course_name]:
                sum_of_marks += grade
                count += 1
    return sum_of_marks / count

print(f"Средняя оценка за лекции")
print(round(lectors_average_on_course(lectors,"Physics"),2))