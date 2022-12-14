from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import *





app_name = 'DronCount'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('addDrone/', Add_Drone_APIView.as_view(), name="DRONE"),
    # path('human/', Human_APIView.as_view(), name="HUMAN"),
    path('log/', Log_APIView.as_view(), name="LOGREVIEW"),
    # path('videoList/', VideoList_APIView.as_view(), name="VIDEOLIST"),
    path('maps/',Map_APIView.as_view(), name="MAPS"),
    path('countDrone/',DroneCount_APIView.as_view(), name="DRONECOUNT"),
    path('droneAvgAge/',DroneAvgAge_APIView.as_view(), name="DRONEAVGAGE"),
    path('totalannot/',TotalAnnot_APIView.as_view(), name="TOTALANNOTAION"),
    path('monthflight/',MonthFlights_APIView.as_view(), name="MONTHFLIGHTS"),
    path('annotationlist/',Annotationlist_APIView.as_view(), name="ANNOTAIONLIST"),




    # path


    # path('login/', LoginAPIView.as_view(), name='LOGIN'),

    ]
