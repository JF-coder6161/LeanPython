import unittest
from survey import AnonymousSurvey

"""
unittest中的常用断言方法
assertEqual(a,b)    核实：a == b
assertNotEqual(a,b) 核实：a != b
assertTrue(x)       核实x为True
assertFalse(x)      核实x为False
assertIn(item,list) 核实item在list中
assertNotIn(item,list) 核实item不在list中
"""

class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Spanish']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            
            
