class PeopleUniversity():

	def __init__(self, name, position):
		self.name = name
		self.position = postion

	def TimetableClasses(self):
		pass

	def WorkingDay(self):
		pass

	def AveragePerformance(self):
		pass


class Management(PeopleUniversity):

	def __init__(self, name, position):
        PeopleUniversity.__init__(self, name, position)

    def DistributionFunds(self):
    	pass

    def ScheduleDefinition(self):
    	pass

    def OrgnizationEvents(self):
    	pass


class Teacher(PeopleUniversity):

	def __init__(self, name, position):
        PeopleUniversity.__init__(self, name, position)

    def StudentAchievement(self):
    	pass

    def Salary(self):
    	pass


class Student(PeopleUniversity):

	def __init__(self, name, position):
        PeopleUniversity.__init__(self, name, position)

    def Homework(self):
    	pass

    def Scholarship(self):
    	pass