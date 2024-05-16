import unittest
from survey import AnonymouseSurvey

class TestAnonSurvey(unittest.TestCase):
    def test_store_single_resp(self):
        question = "what languages you speak?"
        survey = AnonymouseSurvey(question)
        survey.store_response("Japanese")
        self.assertIn("Japanese", survey.responses)

if __name__ == '__main__':
    unittest.main()
