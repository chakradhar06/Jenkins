import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):
    # correct test case
    def test_fib1(self):
        result = Fibonacci(6)
        self.assertEqual(result, 13)
        
    # correct test case
    def test_fib2(self):
        result = Fibonacci(7)
        self.assertEqual(result, 21)
    
    # correct test case
    def test_fib3(self):
        result = Fibonacci(8)
        self.assertEqual(result, 34)
    
    # wrong test case
    def test_fib4(self):
        result = Fibonacci(9)
        self.assertEqual(result, 10)
    
    # wrong test case
    def test_fib5(self):
        result = Fibonacci(10)
        self.assertEqual(result, 2)
        
        
if __name__ == '__main__':
    unittest.main()
