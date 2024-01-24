from django.shortcuts import render
from charbamodel.models import Charba, CharbaUpdate
from suvai.models import Suvai, Suvaichy
from rest_framework.response import Response
from rest_framework import viewsets
from users.models import User
from reklama.models import Reklama
from .serialyzers import (CharbaSerializer,
                          UserRegisterSerialyzer,
                          CharbaUpdateSerialyzer,
                          ReklamaSerializer,
                          SuvaiSerialyzer,
                          SuvaichySerialyzer
                          )


def apiview(request):
    return Response("cdscs")


class CharbaAPIView(viewsets.ModelViewSet):
    queryset = Charba.objects.all()
    serializer_class = CharbaSerializer


class UserRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerialyzer


class CharbaUpdateView(viewsets.ModelViewSet):
    queryset = CharbaUpdate.objects.all()
    serializer_class = CharbaUpdateSerialyzer


class ReclamaView(viewsets.ModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer


class SuvaiView(viewsets.ModelViewSet):
    queryset = Suvai.objects.all()
    serializer_class = SuvaiSerialyzer


class SuvaichyView(viewsets.ModelViewSet):
    queryset = Suvaichy.objects.all()
    serializer_class = SuvaichySerialyzer
