# class
class memberOfClub(object):
    # all the properties of the object
    def __init__(self, name, gender, yearBornIn, age, yearsParticipated, section):
        self.name = name
        self.gender = gender
        self.yearBornIn = yearBornIn
        self.age = age
        self.yearsParticipated = yearsParticipated
        self.section = section

    # functions
    def presentInfo(self):
        print(f"This person's name is {self.name}")
        print('''This person's a ''' + str(self.gender))
        print('This person was born in ' + str(self.yearBornIn) + ' and is ' + str(self.age) + ' years old')
        print('This person has participated in this club for ' + str(self.yearsParticipated) + ' years')
        print('This person is in the section of ' + str(self.section))
    def calculateAge(self):
        ageOfPerson = 2021 - self.yearBornIn
        print('The age of this person is ' + str(ageOfPerson))
    def credit(self):
        if self.yearsParticipated >= 3:
            print('This person gets a lot of credit')
        elif self.yearsParticipated == 2:
            print('This person gets some credit')
        else:
            print('This person gets very less credit')

# objects
Janet = memberOfClub('Janet', 'female', 2008, 13, 3, 'sports')
Agnes = memberOfClub('Agnes', 'female', 2019, 11, 1, 'art')
Della = memberOfClub('Della', 'female', 2007, 14, 4, 'english')
Jonas = memberOfClub('Jonas', 'male', 2009, 12, 2, 'sports')

# using functions and objects
Janet.presentInfo()
Janet.calculateAge()
Janet.credit()