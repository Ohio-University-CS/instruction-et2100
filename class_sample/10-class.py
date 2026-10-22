# # use the concept of class to define university
# # where each university have different name, different rank, and different major
# # create 3 university, and set its value to different thing
# # than compare which university have highest rank

# class University():
#     name = ""
#     rank = -1
#     major = []

# university_list = []

# university_1 = University()
# university_list.append(university_1)
# university_2 = University()
# university_list.append(university_2)
# university_3 = University()
# university_list.append(university_3)

# university_1.name = "ou"
# university_2.name = "osu"
# university_3.name = "nyu"

# university_1.rank = 102
# university_2.rank = 101
# university_3.rank = 83

# university_1.major = ["aa", "bb", "cc"]
# university_2.major = ["2a", "b3b", "cc"]
# university_3.major = ["a2a", "bb", "cc2"]

# for university in university_list:
#     print(university.name)


# class University():
#     def __init__(self, _name, _rank, _major):
#         self.name = _name
#         self.rank = _rank
#         self.major = _rank

#     def rank_up(self, _rank):
#         self.rank = self.rank + _rank
#         print(self.rank)

# university_1 = University("ou", 12, ["x", "xas", "sd"])
# university_2 = University("osu", 2, ["x", "xas", "sd"])
# university_3 = University("nyu", 1, ["x", "xas", "sd"])

# print(university_1.name)
# university_1.rank_up(3)
# print(university_1.rank)



# # def xxxx():
# class Student():
#     name = "test"
#     grade = 3

#     def get_info(self):
#         print(self.name, self.grade)

# student_1 = Student()
# student_2 = Student()

# student_1.name = "shawn"
# student_2.grade = 10

# student_1.get_info()
# student_2.get_info()

# print(student_1.name, student_1.grade)
# print(student_2.name, student_2.grade)





# a = 1
# b = 3

# c = a + b
# print (c)


# def add(_a, _b):
#     c = _a + _b
#     print(c)

# a = 1
# b = 3

# add()

# class Test():
#     a = 1
#     b = 3

#     def add(self):
#         c = self.a + self.b
#         print(c)

# test = Test()
# test.add()

# test1 = Test()


# use the class concept to create monster, 
# where each monster have name, attack point, defense point, current hp, max hp
# create a function call heal, 
# where each time calling the heal, it will heal its hp by whatever the value pass to function
# make monster default hp is 0
# write a logic to heal up a monster to max hp

# class Monster():
#     def __init__(self, _name, _atk, _deff, _max_hp):
#         self.name = _name
#         self.atk = _atk
#         self.deff = _deff
#         self.cur_hp = 0
#         self.max_hp = _max_hp

#     def heal(self, _hp):
#         if(self.cur_hp < self.max_hp):
#             self.cur_hp = self.cur_hp + _hp
        
#         if(self.cur_hp > self.max_hp):
#             self.cur_hp = self.max_hp


# monster_1 = Monster("aa", 10, 2, 10)
# while (monster_1.cur_hp < monster_1.max_hp):
#     heal_hp = int(input("Enter HP you want to heal: "))
#     monster_1.heal(heal_hp)

# print("You Monster is all heal up with current and max hp: ", monster_1.cur_hp, monster_1.max_hp)




# class University():
#     def __init__(self, _name, _rank, _major):
#         self.name = _name
#         self.rank = _rank
#         self.major = _rank

#     def rank_up(self, _rank):
#         self.rank = self.rank + _rank
#         print(self.rank)

# university_1 = University("ou", 12, ["x", "xas", "sd"])
# university_2 = University("osu", 2, ["x", "xas", "sd"])
# university_3 = University("nyu", 1, ["x", "xas", "sd"])

# print(university_1.name)
# university_1.rank_up(3)
# print(university_1.rank)


# class Dog():
#     def __init__(self, _name):
#         self.name = _name

#     def speak(self):
#         print(self.name, "says Woof!")


# dog_1 = Dog("aa")
# dog_2 = Dog("bb")

# dog_1.speak()
# dog_2.speak()




# create a class call human, with name, and salary, 
# and human have a function call "make_money"
# create another 2 class, "student", "teacher"
# then make student and teacher call make_money 
# where student make +1 dollar
# teacher make +2 dollar

class Human:
    def __init__(self, _name):
        self.name = _name
        self.salary = 0

    def make_money(self):
        print("Lets make some money")

class Student(Human):
    def make_money(self):
        self.salary = self.salary + 1

class Teacher(Human):
    def make_money(self):
            self.salary = self.salary + 2


teacher = Teacher("aa")
student = Student("bb")

teacher.make_money()
student.make_money()

print(teacher.salary, student.salary)



# class Animal: # parent class 
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def test():
#         print("ss")
# class Cat(Animal):
#     # def speak():
#     #     print("says Meow!")
#     def speak(self, a):
#         print("says Meow!")
# dog1 = Dog("Buddy")
# cat1 = Cat("Luna")
# dog1.speak()
# cat1.speak()
# cat1.speak("a")