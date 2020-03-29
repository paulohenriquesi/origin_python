from api.tests.ruletestcase import RulesTestCase
from api.models import HouseOwnershipStatusChoice, House
from api.rules import user_house_is_mortgaged

class UserHouseIsMortgagedRuletest(RulesTestCase):
    def test_when_user_house_is_mortgaged_should_change_home_and_disability_score(self):
        info = self.create_info(house=House(HouseOwnershipStatusChoice.MORTGAGED))
        
        risk = user_house_is_mortgaged(info, self.empty_risk())
        
        self.assert_risk_values(risk, home=1, disability=1)
        
    def test_when_user_house_is_owned_should_not_change_score(self):
        info = self.create_info(house=House(HouseOwnershipStatusChoice.OWNED))
        
        risk = user_house_is_mortgaged(info, self.empty_risk())
        
        self.assert_risk_values(risk)