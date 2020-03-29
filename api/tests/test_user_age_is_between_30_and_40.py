from api.tests.ruletestcase import RulesTestCase
from api.rules import user_age_is_between_30_and_40

class UserAgeIsBetween30And40Test(RulesTestCase):
    def test_when_user_age_is_Between_30_and_40_should_change_all_scores(self):
        info = self.create_info(age=35)
        
        risk = user_age_is_between_30_and_40(info, self.empty_risk())
        
        self.assert_risk_values(risk, life=-1, auto=-1, disability=-1, home=-1)
        
    def test_when_user_age_under_30_shold_not_change_score(self):
        info = self.create_info(age=29)
        
        risk = user_age_is_between_30_and_40(info, self.empty_risk())
        
        self.assert_risk_values(risk)
        
    def test_when_user_age_is_over_40_shold_not_change_score(self):
        info = self.create_info(age=41)
        
        risk = user_age_is_between_30_and_40(info, self.empty_risk())
        
        self.assert_risk_values(risk)