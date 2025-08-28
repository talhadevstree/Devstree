#Write comprehensive unit tests for a calculator class using unittest

import unittest 
class Calculator:
    def add (self , a ,b):
        return a + b
    def sub (self , a ,b):
        return a - b
    def mul (self , a ,b):
        return a * b
    def div (self , a ,b):
        return a / b
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc =  Calculator()
        
    def test_add(self):
        self.assertEqual(self.calc.add(4,7),11)
    def test_sub(self):
        self.assertEqual(self.calc.sub(10,7),3)
    def test_mul(self):
        self.assertEqual(self.calc.mul(7,7),49)
    def test_div(self):
        self.assertEqual(self.calc.div(10,2),5)
    
        
if __name__ == "__main__":
    unittest.main()