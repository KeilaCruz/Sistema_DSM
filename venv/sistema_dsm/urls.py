from django.urls import path, include
from rest_framework import routers
from sistema_dsm import views

router = routers.DefaultRouter()
router.register(r'pacientes',views.PacienteView,'pacientes')

urlpatterns = [
    path("api/v1/",include(router.urls))
]