from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PersonalInfoSerializer, RiskScoreResultSerializer
from api.models import RiskScoreResult
import api.rules

@api_view(["POST"], )
def calculate_risk(request):
    serializer = PersonalInfoSerializer(data=request.data)
    
    serializer.is_valid(raise_exception=True)
    
    personalInfo = serializer.create(serializer.validated_data)
    
    risk = api.rules.calculate_risk_rules([
        api.rules.user_risk_questions,
        api.rules.user_has_no_income_or_vehicle_or_house, 
        api.rules.user_age_is_over_60,
        api.rules.user_age_is_under_30, 
        api.rules.user_age_is_between_30_and_40, 
        api.rules.user_income_is_above_200k,
        api.rules.user_house_is_mortgaged,
        api.rules.user_has_dependents,
        api.rules.user_is_married,
        api.rules.user_vehicle_was_produced_in_the_last_five_years], personalInfo)
    
    riskSerializer = RiskScoreResultSerializer(RiskScoreResult(risk))
    
    return Response(riskSerializer.data)
