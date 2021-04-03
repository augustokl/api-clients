from rest_framework import serializers
from client.models import Client
from client.validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not valid_number(data['cpf'], 11):
            raise serializers.ValidationError(
                {'cpf': 'CPF precisa ter 11 digitos'})
        if not valid_number(data['rg'], 9):
            raise serializers.ValidationError(
                {'rg': 'CPF precisa ter 11 digitos'})
        if not valid_number(data['celphone'], 9):
            raise serializers.ValidationError(
                {'celphone': 'Celular precisa ter 11 digitos'})
        if not valid_number(data['name'], 9):
            raise serializers.ValidationError(
                {'name': 'Não incluca números'})

        return data
