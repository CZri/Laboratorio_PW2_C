from rest_framework import routers
from django.urls import path,include
from .views import ViewStudent,ViewGroup
from rest_framework.documentation import include_docs_urls
router=routers.DefaultRouter()

router.register( r'Student',ViewStudent,'studiante')
router.register(r'grupo',ViewGroup,'grupos')
urlpatterns=[
     path('Api/v1/', include(router.urls)),
     #path('docs',include_docs_urls(title='Documentacion de la API')),
]
