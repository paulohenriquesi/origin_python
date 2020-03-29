from api.tests.ruletestcase import RulesTestCase
from api.rules import user_is_married
from api.models import MaritalStatusChoice

class UserIsMarriedRuleTest(RulesTestCase):
    def test_when_user_is_married_should_change_life_and_disability_score(self):
        info = self.create_info(marital_status=MaritalStatusChoice.MARRIED)
        
        risk = user_is_married(info, self.empty_risk())
        
        self.assert_risk_values(risk, life=1, disability=-1)
        
    def test_when_user_is_single_should_not_change_score(self):
        info = self.create_info(marital_status=MaritalStatusChoice.SINGLE)
        
        risk = user_is_married(info, self.empty_risk())
        
        self.assert_risk_values(risk)