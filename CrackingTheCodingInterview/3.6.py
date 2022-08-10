class Shelter:

	def __init__(self):
		self.cats = []
		self.dogs = []

	def enqueue(self, category, age):
		if category == 'c':
			self.cats.append(age)
		elif category == 'd':
			self.dogs.append(age)
		else:
			print('c - cats, d - dogs')

	def dequeueAny(self):
		return max(self.cats + self.dogs)

	def dequeueDog(self):
		return max(self.dogs)

	def dequeueCat(self):
		return max(self.cats)


shelter = Shelter()
shelter.enqueue('c', 12)
shelter.enqueue('d', 22)
shelter.enqueue('c', 5)
print(shelter.dequeueAny())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
