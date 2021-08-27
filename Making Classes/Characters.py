class characters(object):
    def __init__(self, user, gender, yearBornIn):
        self.user = user
        self.gender = gender
        self.yearBornIn = yearBornIn

    # functions
    def presentInfo(self):
        print(f"This person's name is {self.user}")
        print(str(self.user) + ' is a ' + str(self.gender))
        print(str(self.user) + ' was born in ' + str(self.yearBornIn))
    def calculateAge(self):
        ageOfPerson = 2016 - self.yearBornIn
        print('''This person's age is ''' + str(ageOfPerson))

# objects
Eleanor = characters('Eleanor', 'female', 1982)
Chidi = characters('Chidi', 'male', 1983)
Jason = characters('Jason', 'male', 2007)
Tahani = characters('Tahani', 'female', 1986)

# using functions and objects
Eleanor.presentInfo()
Eleanor.calculateAge()
