from api.tests.ruletestcase import RulesTestCase
from api.rules import user_has_no_income_or_vehicle_or_house, INELEGIBLE_VALUE

class UserHasNoIncomeOrVehicleOrHouseTest(RulesTestCase):  
    def test_when_user_has_no_income_shold_be_ineligible_for_disablity(self):
        info = self.create_info(income=0)
        risk = user_has_no_income_or_vehicle_or_house(info, self.empty_risk())
        self.assert_risk_values(risk, disability=INELEGIBLE_VALUE)
        
    def test_when_user_has_no_house_shold_be_ineligible_for_home(self):
        info = self.create_info(house=None)
        risk = user_has_no_income_or_vehicle_or_house(info, self.empty_risk())
        self.assert_risk_values(risk, home=INELEGIBLE_VALUE)
        
    def test_when_user_has_no_vehicle_shold_be_ineligible_for_auto(self):
        info = self.create_info(vehicle=None)
        risk = user_has_no_income_or_vehicle_or_house(info, self.empty_risk())
        self.assert_risk_values(risk, auto=INELEGIBLE_VALUE)
        
    def test_when_user_have_auto_and_income_and_house_should_not_change_score(self):
        info = self.create_info()
        risk = user_has_no_income_or_vehicle_or_house(info, self.empty_risk())
        self.assert_risk_values(risk)