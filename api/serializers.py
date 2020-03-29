from rest_framework import serializers
from api.models import PersonalInfo, House, Vehicle, HouseOwnershipStatusChoice, MaritalStatusChoice
import datetime

class HouseSerializer(serializers.Serializer):
    ownership_status = serializers.ChoiceField(HouseOwnershipStatusChoice, required=True)
    
    def create(self, validated_data):
        return House(**validated_data)

class VehicleSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=True, min_value=1900, max_value=datetime.datetime.now().year)
    
    def create(self, validated_data):
        return Vehicle(**validated_data)

class PersonalInfoSerializer(serializers.Serializer):
    age = serializers.IntegerField(required=True, min_value=0, max_value=120)
    dependents = serializers.IntegerField(required=True, min_value=0)
    house = HouseSerializer(required=False, allow_null=True)
    income = serializers.IntegerField(required=True, min_value=0)
    marital_status = serializers.ChoiceField(MaritalStatusChoice, required=True)
    risk_questions = serializers.ListField(required=True, min_length=3, max_length=3)
    vehicle = VehicleSerializer(required=False, allow_null=True)
    
    def create(self, validated_data):
        info = PersonalInfo(**validated_data)
        house_data = validated_data.pop('house')
        vehicle_data = validated_data.pop('vehicle')
        if house_data is not None:
            info.house = House(**house_data)
            
        if vehicle_data is not None:
            info.vehicle = Vehicle(**vehicle_data)
        
        return info
    
class RiskScoreResultSerializer(serializers.Serializer):
    auto = serializers.CharField()
    disability = serializers.CharField()
    home = serializers.CharField()
    life = serializers.CharField()
    