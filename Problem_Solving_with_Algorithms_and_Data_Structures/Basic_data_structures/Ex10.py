from L_queue import Queue
nums = [123, 434, 525, 436, 7567, 234, 867]

def sort_raz(nums):
	main = Queue()
	d = {}
	for i in nums:
		main.enqueue(i)

	for j in range(10):
		while not main.isEmpty():
			if main.items % 10 == j:
				d[j] = k
			main.dequeue()

print(sort_raz(nums))
