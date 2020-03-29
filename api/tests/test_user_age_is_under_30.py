from api.tests.ruletestcase import RulesTestCase
from api.rules import user_age_is_under_30

class UserAgeIsUnder30RuleTest(RulesTestCase):
    def test_when_user_age_is_under_30_should_change_all_scores(self):
        info = self.create_info(age=29)
        
        risk = user_age_is_under_30(info, self.empty_risk())
        
        self.assert_risk_values(risk, life=-2, auto=-2, disability=-2, home=-2)
        
    def test_when_user_age_is_30_should_not_change_score(self):
        info = self.create_info(age=30)
        
        risk = user_age_is_under_30(info, self.empty_risk())
        
        self.assert_risk_values(risk)