'''
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Three" instead of the number 
and for the multiples of five print "Five". 
For numbers which are multiples of both three and five print "ThreeFive".
'''

import unittest

class TestMultiples(unittest.TestCase):
	def test_ismultiple(self, AO):

		testcase = [
			([92], [92]),
			([3], ['Three']),
			([5], ['Five']),
			([15], ['ThreeFive']),
		]
		
		for i in testcase:
			self.assertListEqual(AO.process_multiples_of(i[0]), i[1])

class ArithmeticOperations:
	def __init__(self):
		TM = TestMultiples()
		TM.test_ismultiple(self)
		
	def show(self, numbers):
		result_list = self.process_multiples_of(numbers)
		for result in result_list:
			print(result)

	def process_multiples_of(self, numbers):
	
		result_list = []
		
		for n in numbers:
			
			result = n
			
			if not n % 3 and not n % 5:
				result = 'ThreeFive'
		
			elif not n % 3:
				result = 'Three'
		
			elif not n % 5:
				result = 'Five'
			
			result_list.append(result)
			
		return result_list
			
if __name__ == "__main__":
	AO = ArithmeticOperations()
	AO.show(range(1, 101))
	