from api.tests.ruletestcase import RulesTestCase
from api.rules import user_income_is_above_200k, INELEGIBLE_VALUE

class UserIncomeIsOver200kRuleTest(RulesTestCase):
    def test_when_user_income_is_over_200k_should_change_all_score(self):
        info = self.create_info(income=210000)
        
        risk = user_income_is_above_200k(info, self.empty_risk())
        
        self.assert_risk_values(risk, -1, -1, -1, -1)
        
    def test_when_user_income_is_200k_not_change_score(self):
        info = self.create_info(age=200000)
        
        risk = user_income_is_above_200k(info, self.empty_risk())
        
        self.assert_risk_values(risk)