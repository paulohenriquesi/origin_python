from api.tests.ruletestcase import RulesTestCase
from api.rules import user_age_is_over_60, INELEGIBLE_VALUE

class UserAgeIsOver60RuleTest(RulesTestCase):
    def test_when_user_age_is_over_60_should_set_life_and_disability_score_inelegible(self):
        info = self.create_info(age=61)
        
        risk = user_age_is_over_60(info, self.empty_risk())
        
        self.assert_risk_values(risk, life=INELEGIBLE_VALUE, disability=INELEGIBLE_VALUE)
        
    def test_when_user_age_is_60_should_not_change_score(self):
        info = self.create_info(age=60)
        
        risk = user_age_is_over_60(info, self.empty_risk())
        
        self.assert_risk_values(risk)