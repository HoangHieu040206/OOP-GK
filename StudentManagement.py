import json

class Student:
    def __init__(self, name, student_id, age, gender, email, address, major):
        self._name = name
        self._student_id = student_id
        self._age = age
        self._gender = gender
        self._email = email
        self._address = address
        self._major = major

    @property
    def name(self): return self._name
    @name.setter
    def name(self, value): self._name = value

    @property
    def student_id(self): return self._student_id
    @student_id.setter
    def student_id(self, value): self._student_id = value

    @property
    def age(self): return self._age
    @age.setter
    def age(self, value): self._age = value

    @property
    def gender(self): return self._gender
    @gender.setter
    def gender(self, value): self._gender = value

    @property
    def email(self): return self._email
    @email.setter
    def email(self, value): self._email = value

    @property
    def address(self): return self._address
    @address.setter
    def address(self, value): self._address = value

    @property
    def major(self): return self._major
    @major.setter
    def major(self, value): self._major = value

    def to_dict(self):
        return {
            "type": "Student",
            "name": self.name,
            "student_id": self.student_id,
            "age": self.age,
            "gender": self.gender,
            "email": self.email,
            "address": self.address,
            "major": self.major
        }

    def __str__(self):
        return (
            f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\n"
            f"ID: {self.student_id}\nMajor: {self.major}\nEmail: {self.email}\nAddress: {self.address}"
        )


class FirstYear(Student):
    def __init__(self, name, student_id, age, gender, email, address, major, school, point):
        super().__init__(name, student_id, age, gender, email, address, major)
        self.school = school
        self.point = point

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "FirstYear",
            "school": self.school,
            "point": self.point
        })
        return data

    def __str__(self):
        return super().__str__() + f"\nSchool: {self.school}\nPoint: {self.point}"


class SecondYear(Student):
    def __init__(self, name, student_id, age, gender, email, address, major, gpa, scholarship):
        super().__init__(name, student_id, age, gender, email, address, major)
        self.gpa = gpa
        self.scholarship = scholarship

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "SecondYear",
            "gpa": self.gpa,
            "scholarship": self.scholarship
        })
        return data

    def __str__(self):
        return super().__str__() + f"\nGPA: {self.gpa}\nScholarship: {self.scholarship}"


class ThirdYear(Student):
    def __init__(self, name, student_id, age, gender, email, address, major, gpa, scholarship, company):
        super().__init__(name, student_id, age, gender, email, address, major)
        self.gpa = gpa
        self.scholarship = scholarship
        self.company = company

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "ThirdYear",
            "gpa": self.gpa,
            "scholarship": self.scholarship,
            "company": self.company
        })
        return data

    def __str__(self):
        return super().__str__() + (
            f"\nGPA: {self.gpa}\nScholarship: {self.scholarship}\nCompany: {self.company}"
        )


class FourthYear(Student):
    def __init__(self, name, student_id, age, gender, email, address, major, gpa, scholarship, company, project):
        super().__init__(name, student_id, age, gender, email, address, major)
        self.gpa = gpa
        self.scholarship = scholarship
        self.company = company
        self.project = project

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "FourthYear",
            "gpa": self.gpa,
            "scholarship": self.scholarship,
            "company": self.company,
            "project": self.project
        })
        return data

    def __str__(self):
        return super().__str__() + (
            f"\nGPA: {self.gpa}\nScholarship: {self.scholarship}\n"
            f"Company: {self.company}\nProject: {self.project}"
        )


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            raise ValueError("Student ID already exists.")
        self.students.append(student)

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def get_all_students(self):
        return self.students

    def save_to_file(self, filename="students.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def load_from_file(self, filename="students.json"):
        self.students.clear()
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    student_type = item.get("type")
                    common = (
                        item["name"], item["student_id"], item["age"],
                        item["gender"], item["email"], item["address"], item["major"]
                    )
                    if student_type == "FirstYear":
                        s = FirstYear(*common, item["school"], item["point"])
                    elif student_type == "SecondYear":
                        s = SecondYear(*common, item["gpa"], item["scholarship"])
                    elif student_type == "ThirdYear":
                        s = ThirdYear(*common, item["gpa"], item["scholarship"], item["company"])
                    elif student_type == "FourthYear":
                        s = FourthYear(*common, item["gpa"], item["scholarship"], item["company"], item["project"])
                    else:
                        s = Student(*common)
                    self.students.append(s)
        except FileNotFoundError:
            pass
