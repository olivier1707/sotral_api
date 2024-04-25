from rest_framework import serializers
from .models import *


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'


class LigneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ligne
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all_'


class TarifSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarif
        fields = '__all__'


class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = '__all__'


class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyager
        fields = '__all__'


# Pour la transaction
class TransactionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    tarif_price = serializers.IntegerField()
