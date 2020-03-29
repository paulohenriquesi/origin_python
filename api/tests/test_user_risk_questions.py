from api.tests.ruletestcase import RulesTestCase
from api.rules import user_risk_questions

class UserRiskQuestionsTest(RulesTestCase):
    def test_when_all_true_should_change_all_scores(self):
        info = self.create_info(risk_questions=[1, 1, 1])
        
        risk = user_risk_questions(info, self.empty_risk())
        
        self.assert_risk_values(risk, life=3, auto=3, disability=3, home=3)