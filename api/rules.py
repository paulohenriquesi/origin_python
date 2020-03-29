from api.models import RiskScore, HouseOwnershipStatusChoice, MaritalStatusChoice
from datetime import datetime

INELEGIBLE_VALUE = 1000
        
def calculate_risk_rules(rules, info):
    result = RiskScore(0, 0, 0, 0)
    
    for rule in rules:
        rule(info, result)
    
    return result
    
def user_risk_questions(info, result):
    apply_over_all_scores(result, sum(info.risk_questions))
    return result
    
def user_has_no_income_or_vehicle_or_house(info, result):
    if info.income == 0:
        result.disability += INELEGIBLE_VALUE
    
    if info.vehicle is None:
        result.auto += INELEGIBLE_VALUE
    
    if info.house is None:
        result.home += INELEGIBLE_VALUE
        
    return result

def user_age_is_over_60(info, result):
    if info.age > 60:
        result.disability += INELEGIBLE_VALUE
        result.life += INELEGIBLE_VALUE
    
    return result

def user_age_is_under_30(info, result):
    return apply_over_all_if_true(lambda i: i.age < 30, info, result, -2)

def user_age_is_between_30_and_40(info, result):
    return apply_over_all_if_true(lambda i: 30 <= i.age <= 40, info, result, -1)

def user_income_is_above_200k(info, result):
    return apply_over_all_if_true(lambda i: 30 <= i.income > 200000, info, result, -1)

def user_house_is_mortgaged(info, result):
    if info.house is not None and info.house.ownership_status == HouseOwnershipStatusChoice.MORTGAGED:
        result.home += 1
        result.disability += 1
        
    return result

def user_has_dependents(info, result):
    if info.dependents > 0:
        result.life += 1
        result.disability += 1
        
    return result

def user_is_married(info, result):
    if info.marital_status == MaritalStatusChoice.MARRIED:
        result.life += 1
        result.disability -= 1
        
    return result

def user_vehicle_was_produced_in_the_last_five_years(info, result):
    year = datetime.now().year
    
    if info.vehicle is not None and year - info.vehicle.year <= 5:
        result.auto += 1
        
    return result
  
def apply_over_all_scores(result, increment):
    result.auto += increment
    result.life += increment
    result.home += increment
    result.disability += increment
        
    return result 
        
def apply_over_all_if_true(condition, info, result, increment):
    if condition(info):
        apply_over_all_scores(result, increment)
        
    return result