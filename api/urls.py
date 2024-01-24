from django.urls import path, include
from rest_framework import routers
from api.views import (CharbaAPIView,
                       CharbaUpdateView,
                       UserRegisterView,
                       ReclamaView,
                       apiview,
                       SuvaiView,
                        SuvaichyView
                       )

router = routers.DefaultRouter()
router.register('charba-list', CharbaAPIView)
router.register('charba-update', CharbaUpdateView)
router.register('user_register', UserRegisterView)
router.register('reklama', ReclamaView)
router.register('suvai', SuvaiView)
router.register('suvaichy', SuvaichyView)


urlpatterns = [
    path('view', apiview, name='api'),
    path('', include(router.urls)),
]
