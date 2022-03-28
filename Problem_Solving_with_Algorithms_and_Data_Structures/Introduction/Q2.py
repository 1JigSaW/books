class BankAccount():

	def __init__(self, balance):
		self.balance = balance

	def TakeOff(self):
		pass

	def Put(self):
		pass

	def Check(self):
		pass


class Deposit(BankAccount):

	def __init__(self, balance, time, percent):
		BankAccount.__init__(self, balance)
		self.time = time
		self.percent = percent

	def Time(self):
		pass


class Saving(Deposit):

	def __init__(self, balance):
		BankAccount.__init__(self, balance)


class ImpersonalMetal(Deposit):

	def __init__(self, balance):
		BankAccount.__init__(self, balance)