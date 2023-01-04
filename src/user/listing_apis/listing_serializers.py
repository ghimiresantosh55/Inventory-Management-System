from src.user_group.models import CustomGroup
from rest_framework import serializers
class GroupsCustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomGroup
        fields = ['id', 'name']