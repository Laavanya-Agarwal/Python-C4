class atm(object):
    def __init__(self, user, gender, yearBornIn, accountBalance):
        self.user = user
        self.gender = gender
        self.yearBornIn = yearBornIn
        self.accountBalance = accountBalance

    # functions
    def presentInfo(self):
        print(f"This person's name is {self.user}")
        print(str(self.user) + ' is a ' + str(self.gender))
        print(str(self.user) + ' was born in ' + str(self.yearBornIn))
    def calculateAge(self):
        ageOfPerson = 2016 - self.yearBornIn
        print('''This person's age is ''' + str(ageOfPerson))
    def balance(self):
        if self.gender == 'female'
            print(str(self.user) + ' has ' + str(self.accountBalance) + ' rupees in her bank account')
        if self.gender == 'male'
            print(str(self.user) + ' has ' + str(self.accountBalance) + ' rupees in his bank account')
    

# objects
Eleanor = characters('Eleanor', 'female', 1982, 90000)
Heidi = characters('Heidi', 'female', 1985, 40000)
Will = characters('Will', 'male', 1990, 30420)
Jackson = characters('Jackson', 'male', 2000, 20398)

# combining functions and objects
Eleanor.presentInfo()
Eleanor.calculateAge()
Eleanor.balance()