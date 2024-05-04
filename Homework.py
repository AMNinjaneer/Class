#Task 1
class Person:
  def __init__(self, first_name, lastname, age):
    self.firstname = first_name
    self.lastname = lastname
    self.age = age
    self.assigned = False #may cause trouble if not attached to children inits
  def __repr__(self):
    return (self.firstname + " " + self.lastname )
  def type_int(variable): #ask if I should create something to verify that the user input an integer  or if I should just trust that it will be ok for simplicity sake
    return
  def Add():
    typep = input("Would you like to add a student or a teacher? \n Please type 'student' or 'teacher': ")
    if typep == "student":
      print("Great! What is their ...")
      first = input('First Name: ')
      last = input('Last Name: ')
      age = input('Age: ')
      year = input('Year: ')
      person = Student(year, first, last, age)
      print("Thank you:)")
      roster = person.students
      #roster = [a for a in dir(person) if not a.startswith('__') if type(a) == list] #let's assume this grabs the class/teacher roster, I want to see if it is possible to access the list of students/teachers in studen in this way
      roster.append(person)
      # print(roster)
      # print(person.__class__.__name__)
    elif typep == "teacher":
      print("Great! What is their ...")
      first = input('First Name: ')
      last = input('Last Name: ')
      age = input('Age: ')
      salary = input('Salary: ')
      subject = input('Subject: ')
      person = Teacher(salary, subject, first, last, age)
      print("Thank you:)")
      roster = person.teachers
      #roster = [a for a in dir(person) if not a.startswith('__')] #let's assume this grabs the class/teacher roster
      roster.append(person)
    else:
      print("I'm sorry that is not an option")
class Student(Person):
  _students = []
  def __init__(self, year, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.year = year
  # def Add_Student(self):
  #   Student.students.append(self)
class Teacher(Person):
  _teachers = []
  def __init__(self, salary, subject,*args, **kwargs):
    super().__init__(*args, **kwargs)
    self.salary = salary
    self.subject = subject
  # def Add_Teacher(self):
  #   Teacher.teachers.append(self)
class Classroom(Student, Teacher):
  def __init__(self, subject):
    self.subject = subject
    self.teacher = None
    self.class_size = 2
    self.students = []
  def fillroom(self):
    T = Teacher.teachers
    S = Student.students
    for teacher in T:
      if teacher.assigned == False:
        self.teacher = teacher
        teacher.assigned = True
    n = 0# counting the number of student in class
    counter = 0#counting the number of students gone through without assignment
    while n < self.class_size:
      print("The available students are :")
      for student in S:
        if student.assigned == False:
          print(student)
      name = input(f"Which student would you like to add to {self.teacher}'s {self.subject} class?: ")
      for student in S:
        if name == student.firstname and student.assigned == False:
          self.students.append(student)
          student.assigned = True
          n += 1
          continue
        counter += 1
      if counter >= len(S):
        print("Sorry that student doesn't exist. Please, try again.")
        counter = 0
  def ShowRoom(self):
    print(f"Welcome to {self.subject} class! Your teacher is {self.teacher}, who will take great care of you. And, you classmates are {self.students}")
choice = True
while choice:
  Person.Add()
  c = input("Would you like to continue adding people? \n Please enter 'y' for yes or 'n' for no: ")
  match c:
    case "y":
      pass
    case "n":
      choice = False

classroom_1 = Classroom("Math")
classroom_2 = Classroom("English")
classroom_3 = Classroom("Gym")
print(Student.students)

classroom_1.fillroom()
classroom_2.fillroom()
classroom_3.fillroom()
classroom_3.ShowRoom()