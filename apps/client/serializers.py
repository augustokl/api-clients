from rest_framework import serializers
from client.models import Client
from client.validators import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'CPF inválido'})
        if not valid_number(data['rg'], 9):
            raise serializers.ValidationError(
                {'rg': 'RG precisa ter 9 digitos'})
        if not valid_celphone(data['celphone']):
            raise serializers.ValidationError(
                {'celphone': 'Celular precisa ter 11 digitos e o padrão: 00 00000-0000'})
        if not valid_string(data['name']):
            raise serializers.ValidationError(
                {'name': 'Não incluca números'})

        return data
