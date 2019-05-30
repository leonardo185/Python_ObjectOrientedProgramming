class student:
    def __init__(self):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def set_student_info(self, student_id, marks,age):
        self.__student_id = student_id
        self.__marks = marks
        self.__age = age

    def validate_age(self):
        if(self.__age > 20):
            return True
        else:
            return False

    def validate_marks(self):
        if(self.__marks >= 0 and self.__marks <=100):
            return True
        else:
            return False

    def check_qualification():
        if(validate_age() and validate_marks()):
            if(self.__marks > 65):
                return True
            else:
                return False
        else:
            return False

    def get_student_info(self):
        print(self.__student_id)
        print(self.__marks)
        print(self.__age)
