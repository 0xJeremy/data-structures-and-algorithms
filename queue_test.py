from queue import Queue
from utils import getRandom

def testEmpty():
	q = Queue()
	testData = getRandom(10)
	for item in testData:
		q.pushBack(item)
	q.empty()
	assert q.size() == 0

def testSize():
	q = Queue()
	testData = getRandom(100)
	for i in range(len(testData)):
		assert q.size() == i
		q.pushBack(testData[i])

def testBack():
	q = Queue()
	testData = getRandom(1000)
	for item in testData:
		q.pushBack(item)
	for i in range(len(testData)):
		assert q.popFront() == testData[i]

def testFront():
	q = Queue()
	testData = getRandom(1000)
	assert q.front() == None
	for item in testData:
		q.pushBack(item)
		assert q.front() == testData[0]

def testPushBack():
	q = Queue()
	testData = getRandom(1000)
	for item in testData:
		q.pushBack(item)
	for i in range(len(testData)):
		assert q.popFront() == testData[i]

def testPopFront():
	q = Queue()
	testData = getRandom(1000)
	for item in testData:
		q.pushBack(item)
	for i in range(len(testData)):
		assert q.popFront() == testData[i]

def testEQ():
	q1, q2 = Queue(), Queue()
	testData = getRandom(1000)
	for item in testData:
		q1.pushBack(item)
		assert q1 != q2
		q2.pushBack(item)
		assert q1 == q1
	q1.empty()
	assert q1 != q2
		

def main():
	testEmpty()
	testSize()
	testBack()
	testFront()
	testPushBack()
	testPopFront()
	testEQ()

if __name__ == '__main__':
	main()
