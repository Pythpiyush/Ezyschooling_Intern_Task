from rest_framework import serializers
from .models import Piz_Mod


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piz_Mod
        fields = '__all__'