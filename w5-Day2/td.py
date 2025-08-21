import unittest 

class Test(unittest.TestCase):
    def test_reverse(self):
        utils = StringUtils()
        self.assertEqual(utils.reverse("hello"), "olleh")
    def test_pali(self):
        utils = StringUtils()
        self.assertTrue(utils.pali("heh"))
        self.assertFalse(utils.pali("hello"))
    

class StringUtils:
    def reverse(self , text:str) -> str:
        return text[::-1]
    
    def pali(self ,text:str) -> bool:
        return text == text[::-1]
    
if __name__ == "__main__":
    unittest.main()
    
