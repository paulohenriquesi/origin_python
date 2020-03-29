from unittest import TestCase
from api.models import PersonalInfo, House, Vehicle, RiskScore, MaritalStatusChoice, HouseOwnershipStatusChoice

class RulesTestCase(TestCase):      
    def assert_risk_values(self, risk, home = 0, life = 0, auto = 0, disability = 0):
        self.assertEqual(risk.home, home)
        self.assertEqual(risk.life, life)
        self.assertEqual(risk.auto, auto)
        self.assertEqual(risk.disability, disability)
        
    def create_info(self,
                    age=29, 
                    dependents=2,
                    house=House(HouseOwnershipStatusChoice.OWNED), 
                    income=190000, 
                    marital_status=MaritalStatusChoice.MARRIED, 
                    risk_questions=[0, 1, 0], 
                    vehicle=Vehicle(2013)):
        return PersonalInfo(age, dependents, house, income, marital_status, risk_questions, vehicle)
    
    def empty_risk(self):
        return RiskScore(0, 0, 0, 0)