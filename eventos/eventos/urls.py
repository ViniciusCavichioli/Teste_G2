from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from lpc_evento.views import *
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)
router.register(r'FrequenciaDia', FrequenciaDiaViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
