from django.db import models
from enum import Enum

class HouseOwnershipStatusChoice(models.TextChoices):
    OWNED = "owned",
    MORTGAGED = "mortgaged"
    
class MaritalStatusChoice(models.TextChoices):
    MARRIED = "married"
    SINGLE = "single"
    
class ScoreChoice(models.TextChoices):
    ECONOMIC = "economic"
    REGULAR = "regular"
    RESPONSIBLE = "responsible"
    INELEGIBLE = "inelegible"
    
class Vehicle:
    def __init__(self, year):
        self.year = year
    
class House:
    def __init__(self, ownership_status):
        self.ownership_status = ownership_status

class PersonalInfo:
    def __init__(self, age, dependents, house, income, marital_status, risk_questions, vehicle):
        self.age = age
        self.dependents = dependents
        self.house = house
        self.income = income
        self.marital_status = marital_status
        self.risk_questions = risk_questions
        self.vehicle = vehicle
        
class RiskScore:
    def __init__(self, auto, disability, home, life):
        self.auto = auto
        self.disability = disability
        self.home = home
        self.life = life
        
class RiskScoreResult:
    def __init__(self, score):
        self.auto = self.__map(score.auto)
        self.disability = self.__map(score.disability)
        self.home = self.__map(score.home)
        self.life = self.__map(score.life)
        
    def __map(self, value):
        if value <= 0:
            return ScoreChoice.ECONOMIC
        elif value <= 2:
            return ScoreChoice.REGULAR
        elif value == 3:
            return ScoreChoice.RESPONSIBLE
        else:
            return ScoreChoice.INELEGIBLE
    