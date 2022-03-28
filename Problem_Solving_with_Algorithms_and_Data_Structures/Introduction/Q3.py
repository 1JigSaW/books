class Computer:

	def __init__(self, cpu, ram, hdd, gpu):
		self.cpu = cpu
		self.ram = ram
		self.hdd = hdd
		self.gpu = gpu

	def ON(self):
		pass

	def OFF(self):
		pass


class Laptop(Computer):

	def __init__(self, cpu, ram, hdd, gpu, screen, battery):
		Computer.__init__(self, cpu, ram, hdd, gpu)
		self.screen = screen
		self.battery = battery

	def WorkingHours(self):
		pass


class SmartPhone(Laptop):

	def __init__(self, cpu, ram, hdd, gpu, screen, battery):
		Laptop.__init__(self, cpu, ram, hdd, gpu, screen, battery)

class Server(Computer):

	def __init__(self, cpu, ram, hdd, gpu, screen, battery):
		Computer.__init__(self, cpu, ram, hdd, gpu)