import random

def getRandom(num, low=None, high=None):
	if low != None and high != None:
		return [random.randint(low, high) for i in range(num)]
	return [random.randint(0, 100) for i in range(num)]