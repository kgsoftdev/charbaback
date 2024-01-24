from rest_framework import serializers
from charbamodel.models import Charba, CharbaUpdate
from users.models import User
from reklama.models import Reklama
from suvai.models import Suvai, Suvaichy


class CharbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charba
        fields = '__all__'


class UserRegisterSerialyzer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'avatar', 'role_user', 'user_location']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class CharbaUpdateSerialyzer(serializers.ModelSerializer):
    class Meta:
        model = CharbaUpdate
        fields = '__all__'


class ReklamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = '__all__'


class SuvaiSerialyzer(serializers.ModelSerializer):
    class Meta:
        model = Suvai
        fields = '__all__'


class SuvaichySerialyzer(serializers.ModelSerializer):
    class Meta:
        model = Suvaichy
        fields = '__all__'