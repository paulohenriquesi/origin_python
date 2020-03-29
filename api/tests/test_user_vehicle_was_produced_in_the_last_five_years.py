from api.tests.ruletestcase import RulesTestCase
from api.rules import user_vehicle_was_produced_in_the_last_five_years
from api.models import Vehicle
from datetime import datetime

class UserIncomeIsOver200kRuleTest(RulesTestCase):
    def test_when_user_vehicle_was_produced_in_the_last_five_years_should_change_auto_score(self):
        vehicle_year = datetime.now().year - 3
        info = self.create_info(vehicle=Vehicle(vehicle_year))
        
        risk = user_vehicle_was_produced_in_the_last_five_years(info, self.empty_risk())
        
        self.assert_risk_values(risk, auto=1)
        
    def test_when_user_vehicle_was_not_produced_in_the_last_five_years_should_not_change_score(self):
        vehicle_year = datetime.now().year - 6
        info = self.create_info(vehicle=Vehicle(vehicle_year))
        
        risk = user_vehicle_was_produced_in_the_last_five_years(info, self.empty_risk())
        
        self.assert_risk_values(risk)