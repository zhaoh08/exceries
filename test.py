#from function import *
import requests

r=requests.get('https://docs.pytest.org/en/latest/monkeypatch.html')
r.text





# class Calculator:
    # def sum(self, a, b):
        # return a + b

        

# from unittest import TestCase
# from main import Calculator

# class TestCalculator(TestCase):
    # def setUp(self):
        # self.calc = Calculator()

    # def test_sum(self):
        # answer = self.calc.sum(2, 4)
        # self.assertEqual(answer, 6)

        
# from unittest import TestCase
# from unittest.mock import patch

# class TestCalculator(TestCase):
    # @patch('main.Calculator.sum', return_value=9)
    # def test_sum(self, sum):
        # self.assertEqual(sum(2,3), 9)



        
# def awesome_function ():

    # print 'what a calculation'
    # return 42

# def download_text_from_web

    # print('Download somthing'):
    # returen 'Text from the web'

# def countWords(text):
    # return len(text)

    
# def do_text_analysis():
    # text = download_text_from_web(text)
    # word_cout = countWords(text)
    # return word_count