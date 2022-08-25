# used in tutorial_31 dan tutorial_33

class Student:
    #initialize function (constructor)
    def __init__(self, name, major, gpa, is_on_probation):
        # self di sini mirip seperti this di java
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # fungsi di class di python harus dikasih self
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    
