class characters(object):
    def __init__(self, user, cardNum, pinNum, gender, yearBornIn):
        self.user = user
        self.cardNum = cardNum
        self.pinNum = pinNum
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
Eleanor = characters('Eleanor', 1001, 4444, 'female', 1982)
Chidi = characters('Chidi', 1002, 5555, 'male', 1983)
Jason = characters('Jason', 1003, 3001, 'male', 2007)
Tahani = characters('Tahani', 1004, 2735, 'female', 1986)

# using functions and objects
Eleanor.presentInfo()
Eleanor.calculateAge()
