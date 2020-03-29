from api.tests.ruletestcase import RulesTestCase
from api.rules import user_has_dependents

class UserHasDependentsRuleTest(RulesTestCase):
    def test_when_user_has_dependents_should_chage_disability_and_life_score(self):
        info = self.create_info(dependents=1)
        
        risk = user_has_dependents(info, self.empty_risk())
        
        self.assert_risk_values(risk, life=1, disability=1)
        
    def test_when_user_has_no_dependents_should_not_change_score(self):
        info = self.create_info(dependents=0)
        
        risk = user_has_dependents(info, self.empty_risk())
        
        self.assert_risk_values(risk)