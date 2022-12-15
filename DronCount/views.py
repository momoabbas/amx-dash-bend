from django.shortcuts import render
from django.conf import settings
#from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.db.models import Q
from rest_framework import viewsets, status
import jwt
from django.conf import settings
from .humanDetection import *
from .mapDetails import *
# import geopy
import datetime
import pandas as pd
import calendar
# import geolocation
#
# cord1=(52.2222222)
# print(geolocation(cord1))

#
class Human_APIView(APIView):

    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        annotation_name = data.get('annotation_name')
        video=data.get('video')

        if annotation_name=="human":
            data=CountDetails.objects.create(annotation_name=annotation_name,video=video)
            return Response(Tracker())

        else:
            return Response("no human")

#
# class Maps_APIView(APIView):
#
#     def post(self, request):
#         data = request.data
#         # application_id=data.get('application_id')
#         lng = data.get('lng')
#         lat = data.get('lat')
#         isActive=data.get('isActive')
#         if data:
#         # data=GMap.objects.create(latitude=latitude,longitude=longitude)
#             return Response(fig)
#         else:
#             return Response("no data")


class Add_Drone_APIView(APIView):
    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        aircraft_type = data.get('aircraft_type')
        connection_id = data.get('connection_id')
        UIN = data.get('UIN')
        model_name=data.get('model_name')
        purchase_year=data.get('purchase_year')
        time_in_service=data.get('time_in_service')
        Next_maintainance=data.get('Next_maintainance')




        if data:

            regcreate = Drone.objects.create(aircraft_type=aircraft_type,
            connection_id=connection_id,model_name=model_name,purchase_year=purchase_year,
            UIN=UIN,time_in_service=time_in_service,Next_maintainance=Next_maintainance)
            return Response("Data For Application, Added Sucessfully")

        else:
            return Response("Data Required For Application")

    def get(self, request):

        id =self.request.query_params.get('id')
        if id:
            appdata = Drone.objects.filter(id=id).values()
            return Response(appdata)
        else:

            appdata = Drone.objects.all().values()
            return Response(appdata)

    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Drone.objects.filter(id=id).update(aircraft_type=data.get('aircraft_type'),
            connection_id= data.get('connection_id'),
             UIN=data.get('UIN'),
             model_name=data.get('model_name'),
              purchase_year=data.get('purchase_year'),
               time_in_service=data.get('time_in_service'),
                 Next_maintainance=data.get('Next_maintainance') )

            if data:
                    return Response("Data For Application, Added Sucessfully")
            else:
                # response={'message':"Invalid id"}
                # return Response(response, status=status.HTTP_400_BAD_REQUEST)
                return Response("Data Required For Application")


        else:
            # return JsonResponse({'message': 'Id Required.'})
            return Response("ID Required For Application")


    # CheckAuth(request)





class Log_APIView(APIView):


    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        logData = data.get('logData')

        if data:

            regcreate = Log.objects.create(logData=logData)

            return Response("Data For Application, Added Sucessfully")

        else:
            return Response("Data Required For Application")


    def get(self, request):

        appdata = Log.objects.all().values()
        return Response(appdata)



class VideoList_APIView(APIView):
    # def post(self, request):
    #     data = request.data
    #     # application_id=data.get('application_id')
    #     video = data.get('video')
    #
    #     if data:
    #
    #         regcreate = CountDetails.objects.create(video=video)
    #
    #         return Response("Data For Application, Added Sucessfully")
    #
    #     else:
    #         return Response("Data Required For Application")


    def get(self, request):

        appdata = CountDetails.objects.values_list('video')
        # appd=


        return Response(appdata)


#
# #will it count day wise like number of dront are flying now?
class DroneCount_APIView(APIView):

    def get(self, request):

        # appdata = CountDetails.objects.values_list('video')
        drone_count=Drone.objects.values_list('connection_id').count()
        print(drone_count)
        # appd=


        return Response(drone_count)


import datetime

# using now() to get current time
class DroneAvgAge_APIView(APIView):

    def get(self, request):
        # age=[]
        # current_time = datetime.datetime.now()
        # current_time=current_time.format(current_time)
        # print("CURRENT TIME",current_time)
        drone_count=Drone.objects.values_list('purchase_year')
        drone_count=list(drone_count)
        print("HHHHHHHHHHHHHHHHHHHHHHHHH",drone_count)
        # age=current_time-drone_count
        # print(age)
        # data_s = Drone.objects.values_list('purchase_year')
        # print("PRRRRRRRRRRRRRR",data_s)
        # date_s=list(data_s)
        # print("TYPPPPPPPPPPPPPPPEEEEEEEEEEEEEEE",type(data_s))
        # print("PROOOOOOOOOOOOOOOOOOOO",data_s)
        # dateList = []
        #
        # for i in data_s:
        #     if purchase_year == str(i['purchase_year'].date()):
        #         dateList.append(str(i['purchase_year'].date()))
        # return Response({'message': len(dateList)})

        # purchase_year=datetime.purchase_year.year
        # # purchase_year=datetime.year
        # print("PURCHASE YEAR",purchase_year)


        # appdata = CountDetails.objects.values_list('video')
        # drone_count=Drone.objects.values_list('purchase_year').count()
        # print("DRONE TOTAL COUNT",drone_count)
        #
        # print(type(drone_count))
        # dronedata=Drone.objects.values_list('purchase_year',flat=True)
        # dronedata=list(dronedata)
        # # dronedata =Drone.objects.aggregate(sum('purchase_year'))
        # print("DRONE TOTAL VALUE",dronedata)
        # print(type(dronedata))
        #
        #
        # avgAge=dronedata/drone_count
        # print(avgAge)
        # # appd=

        # return Response( sum('purchase_year') / len('purchase_year'))
        # return Response(avgAge)
        return Response(age)




class TotalAnnot_APIView(APIView):

    def get(self, request):

        # appdata = CountDetails.objects.values_list('video')
        drone_count=CountDetails.objects.values_list('annotation_name').count()

        # dronedata=Drone.objects.values_list('purchase_year')
        # avgAge=dronedata/dronedata
        # print(avgAge)
        # appd=

        # return Response( int(sum('purchase_year')) / int(len('purchase_year')))
        return Response(drone_count)



class MonthFlights_APIView(APIView):

    def get(self, request):
        if is_month ==True:
                    d = pd.Timestamp(date)
                    num=current_time.month
                    m=calendar.month_name[num]
                    if int(d.month) == num:
                        tempDaysDictorMonth['month'] = m
                        tempDaysDictorMonth['count'] = Drone.objects.filter(created_timestamp=num).count()
                        tempDaysorMonth.append(tempDaysDictorMonth)
                        tempDaysDictorMonth = {}
                    else:
                        for j in range(d.day, order_obj['ordered_time'].date().day + 1)[:5]:  #server
                        # for j in range(d.month, order_obj['ordered_time__month']+1)[:5]: #local
                                s=calendar.month_name[j]
                                tempDaysDictorMonth['month'] = s
                                tempDaysDictorMonth['count'] = Drone.objects.filter(created_timestamp=d.month).count()
                                tempDaysorMonth.append(tempDaysDictorMonth)
                                tempDaysDictorMonth = {}
        else:
            print("jhsajhd")
            return Response(tempDaysorMonth)


class Annotationlist_APIView(APIView):

    def get(self, request):

        # appdata = CountDetails.objects.values_list('video')
        totalannotation=CountDetails.objects.values_list('annotation_name')

        # dronedata=Drone.objects.values_list('purchase_year')
        # avgAge=dronedata/dronedata
        # print(avgAge)
        # appd=

        # return Response( int(sum('purchase_year')) / int(len('purchase_year')))
        return Response(totalannotation)


class Map_APIView(APIView):
    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        lng = data.get('lng')
        lat=data.get('lat')
        isActive=data.get('isActive')

        if data:

            regcreate = GMap.objects.create(lng=lng,lat=lat,isActive=isActive)

            return Response("Data For Application, Added Sucessfully")

        else:
            return Response("Data Required For Application")

    def get(self,request):
        appdata = GMap.objects.all().values()
        return Response(appdata)

# class Map_APIView(APIView):
#     def post(self, request):
#         #total flight for the day
#         #x= date
#         #y=total flight number
#
#
#
# class Map_APIView(APIView):
#     def post(self, request):




import cv2
import numpy as np

class VideoStream_APIView(APIView):
    def get(self, request):


        class LiveStream():
        # Create a VideoCapture object and read from input file
        # If the input is the camera, pass 0 instead of the video file name
        # ipadd=
            cap = cv2.VideoCapture(0)

            # Check if camera opened successfully
            if (cap.isOpened()== False):
              print("Error opening video stream or file")

            # Read until video is completed
            while(cap.isOpened()):
              # Capture frame-by-frame
              ret, frame = cap.read()
              if ret == True:

                # Display the resulting frame
                cv2.imshow('Frame',frame)

                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                  break

              # Break the loop
              else:
                break

            # When everything done, release the video capture object
            cap.release()

            # Closes all the frames
            cv2.destroyAllWindows()

        return Response(LiveStream())


#daywise flight#

#how to get last flight time?
#if i try to get it by last date, what if that drone is flying today , database will store today's data.
# class FlightDaywise_APIView(APIView):
#
#     def get(self, request):
#
#         # appdata = CountDetails.objects.values_list('video')
#         totalannotation=Drone.objects.values_list('annotation_name')
#
#         # dronedata=Drone.objects.values_list('purchase_year')
#         # avgAge=dronedata/dronedata
#         # print(avgAge)
#         # appd=
#
#         # return Response( int(sum('purchase_year')) / int(len('purchase_year')))
#         # return Response(totalannotation)
