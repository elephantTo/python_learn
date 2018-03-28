#! /usr/bin/python

def PrintFibonacciSequence(myNum,endPoint):
	global lastNum
	if myNum >= endPoint:
                print fibonacciSequence
		return
	if myNum == 0:
		print fibonacciSequence
		myNum = 2
                lastNum = 1
	fibonacciSequence.append(myNum + lastNum) 
        lastNum = myNum
        PrintFibonacciSequence(fibonacciSequence[len(fibonacciSequence) - 1],endPoint)
if __name__ == "__main__":
	global fibonacciSequence
	fibonacciSequence = [0,1,1,2]
	PrintFibonacciSequence(0,10000)
