from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse, JsonResponse
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
import datetime


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
        # purchase_day=data.get('purchase_day')
        # purchase_month=data.get('purchase_month')



        if data:

            # today_date = datetime.date.today()
            # print(today_date)



            regcreate = Drone.objects.create(aircraft_type=aircraft_type,
            connection_id=connection_id,model_name=model_name,purchase_year=purchase_year,UIN=UIN,time_in_service=time_in_service,Next_maintainance=Next_maintainance)

            # purchase_day=purchase_day,
            # purchase_month=purchase_month,

            return Response("Data For Application, Added Sucessfully")

        else:
            return Response("Data Required For Application")

    def get(self, request):

        id =self.request.query_params.get('id')
        if id:
            appdata = Drone.objects.filter(id=id).values()
            purchase_year = purchase_year.strftime("%d/%m/%Y")
            print (purchase_year)
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

from django.utils import timezone
import datetime
from datetime import timedelta
from datetime import date
from dateutil.parser import parse
# using now() to get current time
from django.db.models import Avg
# from django.db.models import Avg, Extra
from operator import truediv
from django.db.models.functions import ExtractYear

class DroneAvgAge_APIView(APIView):

    def get(self, request):
        ageL=[]
        total = 0

        # a=[2]
        # current_month = timezone.now()
        # current_year=current_month.year
        #
        # todays_date=datetime.datetime.strptime(str(current_year), "%Y")
        # ageL.append(todays_date)
        # age=ageL/a
        # print("YYYYYYYYYYYYYYYYYyy",type(todays_date),todays_date)
        #
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa",type(ageL),ageL)



        current_date = datetime.date.today()
        print("CURRENT DATEEEEEEEEEEEEEEEEE",current_date)


        filtered_data=Drone.objects.values_list('purchase_year')

        filtered_data_count=Drone.objects.values_list('purchase_year').count()

        print("PURCHASE YEARRRRRRRRRRRRRRRR",filtered_data)
        print("PURCHASE YEAR COUNTTTTTTTTTTTT",filtered_data_count)

        # filtered_data=filtered_data.isoformat()

        filtered_data=tuple(filtered_data)
        print("CURRENT DATE AFTER FILTERRRRRRRRRRR",filtered_data)
        # filtered_data=filtered_data.isoformat()

        # print(filtered_data)
        # month=filtered_data[0][0]
        for inner_tuple in filtered_data:
            filtered = inner_tuple[0]
            filtered=filtered.date()
            age=current_date-filtered
            print()
            print("AAAAAAAAGGGGGGGGGGGEEEEEEEEEEE",age)
            filtered=datetime.datetime.strptime(str(filtered), "%Y-%m-%d")

            print("ONE BY ONE DATEEEEEEEEEEEEEEEE",filtered)



            # age=current_date-filtered

            ageL.append(age)
            print("=========================",type(ageL),ageL)

            def sum_numbers(ageL):
                for number in ageL:
                    total += number
                return total
            print("TTTTTTTTTTTTTTTTTTT",total)


            # print("sum",sum)


            # def Average(ageL):
            #     return sum(ageL) / len(ageL)
            #
            # # Driver Code
            # # lst = [15, 9, 55, 41, 35, 20, 62, 49]
            # average = Average(ageL)
            #
            # # Printing average of the list
            # print("Average of the list =", round(average, 2))


            # print("AGEEEEEEEEEEEEEEEEEEEEEE",age)

        # avg_age=age/filtered_data_count
        # def Average(lst):
        #     return sum(lst) / len(lst)
    # avg_age = list(map(truediv, age, filtered_data_count))
    # num = 5
        # new_List = [i/filtered_data_count for i in age]
        # print(new_List)
        # print("AVERAGE AGE OF DRONEEEEEEEEEEEEEEE",avg_age)
        return Response({"current date": current_date,
                     "purchase_year": filtered_data,
                     "filtered_data_count":filtered_data_count,
                     "filtered":filtered,
                     "ageL":ageL,
                     "total":total
                     },)
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        # current_time = datetime.date.now()
        # year=current_time.month
        # print(year)
        # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",type(year))
        # # current_time=current_time.format(current_time)
        # print("CURRENT TIME",current_time)
        #{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{UNCMNT}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        drone_count=Drone.objects.all().values('purchase_year')
        current_month = timezone.now()
        current_year=current_month.year

        todays_date=datetime.datetime.strptime(str(current_year), "%Y")
        print("YYYYYYYYYYYYYYYYYyy",type(todays_date),todays_date)
        return Response()

        # print("+++++++++++++++++",type(drone_count),drone_count)
        # for i in drone_count:
        #     drone_purchase_date=i['purchase_year'].date()
        #     drone_date=datetime.datetime.strptime(str(drone_purchase_date), "%Y-%m-%d")
        #     # age_in_days=todays_date-drone_date
        #     # age_in_years=age_in_days/365
        #
        #     # print(age_in_days)
        #     print(drone_date)

        #{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{UNCMNT}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
            #---------------------------------------------------------------
            # average_age = Drone.objects.all().aggregate(Avg('age'))
            # print(average_age)
            #---------------------------------------------------------------#
        # age=drone_count-cuurent_date

        # drone_count=list(drone_count)
        #
        # listToStr = ' '.join(map(str, drone_count))
        #
        # print("ttttttttttttttttttttt",listToStr)
        # for i in listToStr:

# Python program to convert a list
# to string using list comprehension

# s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# using list comprehension

        # dr_m=[drone_count.month]
        # dr_y=[drone_count.year]
        # dr_y=

        #######################################################
            # print("mmmmmmmmmmmmmmmmmmmmmmmmmm",drone_count)
            # td = datetime.datetime.now() - parse(i[1])
            # print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHh",td.days)
        #####################################################

        # print("mmmmmmmmmmmmmmmmmmmmmmmmmm",dr_m)
        # print("mmmmmmmmmmmmmmmmmmmmmmmmmm",dr_y)

        # drone_count=list(drone_count)
        # print("PURCHASE YEAR FROM DRONE MODEL",drone_count)
        # print(drone_count[5])
        # e = drone_count
        # Dr=[i[0] for i in e]
        # print("PURCHASE DATE AFTER CONVERTING INTO LIST",Dr)

        # print("ddddddddddd",type(drone_count))
#######################################################
        # drone_date=datetime.date.today()
        # print("TYPE OF CURRENT DATE",type(drone_date))
        # # date_list=list(drone_date.timetuple())
        # # print("===============",date_list)
        # # dateD=date(date_list).isoformat()
        # # print("===============",dateD)
        #
        # cr_month=[drone_date.month]
        # cr_year=[drone_date.year]
        #
        # print("TODAYS DATE",drone_date)
        # print("TODAYS YEAR",cr_year)
        # print("TODAYS MONTH",cr_month)
###########################################################




        # e = drone_count
        # Dr=[i[0] for i in e]
        #
        # # drone_date=drone_count.date()
        #
        #
        # print("ddddddddddd",type(drone_count))


        # if
        # age=[]
        # for i in age:

        #
        # return Response(avg_age)

        # print(datetime.time.timetuple[7])
        # print("LLLLLLLLLLHHHHHHHHHHHHHHHHHHHHHHHHH",drone_count)
        # tup = drone_count

# result list initialization
        # result = []
        #
        # for t in tup:
        #     for x in t:
        #         result.append(x)
        #
        # # printing output
        # print("lllllllllllllllllllllllllllllllllllllllll",result)
#
# # result list initialization
#         result = []
#
#         for t in tup:
#             for x in t:
#                 result.append(x)
#
#         # printing output
#         print(result)
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
        # return Response("okkkk")
import datetime
from django.db.models.functions import Extract
import pandas as pd
import calendar

#
# class MonthFlight_APIView(APIView):
#     def get(self,request):
#
#         # data = request.data
#         # date = data['date']
#         # month=data['month']
#         # is_days = data['is_days']
#         # is_month = data['is_month']
#         current_time = datetime.datetime.now()
#         print("current_time===>", current_time.day)
#
#         # tempDaysorMonth = []
#         # tempDaysDictorMonth = {}
#         # order_obj = BookingDetail.objects.all().values('ordered_time_day','ordered_time_month').last() #local
#         order_obj = Drone.objects.all().values('purchase_year').latest('id') #server
#         # if is_days ==True:
#         d = pd.Timestamp(date)
#         print("==<>>",d.date())
#         if int(d.day) == current_time.day:
#             tempDaysDictorMonth['day'] = current_time.day
#             tempDaysDictorMonth['count'] = BookingDetail.objects.filter(ordered_time__date=date).count()
#             tempDaysorMonth.append(tempDaysDictorMonth)
#             tempDaysDictorMonth = {}
#         #     else:
#         #         size = len(date)
#         #         for j in range(d.day, order_obj['ordered_time'].date().day + 1)[:5]:  #server
#         #         # for j in range(d.day, order_obj['ordered_time__day']+1)[:5]: #local
#         #             replacement = str(j)
#         #             dt_text = date.replace(date[size - 2:], replacement)
#         #             tempDaysDictorMonth['day'] = j
#         #             tempDaysDictorMonth['count'] = BookingDetail.objects.filter(ordered_time__date=dt_text).count()
#         #             tempDaysorMonth.append(tempDaysDictorMonth)
#         #             tempDaysDictorMonth = {}
#         # if is_month ==True:
#         #     d = pd.Timestamp(date)
#         #     num=current_time.month
#         #     m=calendar.month_name[num]
#         #     if int(d.month) == num:
#         #         tempDaysDictorMonth['month'] = m
#         #         tempDaysDictorMonth['count'] = BookingDetail.objects.filter(ordered_time__month=num).count()
#         #         tempDaysorMonth.append(tempDaysDictorMonth)
#         #         tempDaysDictorMonth = {}
#         #     else:
#         #         for j in range(d.day, order_obj['ordered_time'].date().day + 1)[:5]:  #server
#         #         # for j in range(d.month, order_obj['ordered_time__month']+1)[:5]: #local
#         #                 s=calendar.month_name[j]
#         #                 tempDaysDictorMonth['month'] = s
#         #                 tempDaysDictorMonth['count'] = BookingDetail.objects.filter(ordered_time__month=d.month).count()
#         #                 tempDaysorMonth.append(tempDaysDictorMonth)
#         #                 tempDaysDictorMonth = {}
#         # else:
#         #         print("jhsajhd")
#         return Response(tempDaysorMonth)
#

        # return response()

from django.utils import timezone
import datetime
class MonthFlight_APIView(APIView):

    def get(self, request):
        count=0
# Extract the current month from the system date
        current_month = timezone.now().month
        # current_month=current_month.isoformat()
        # current_month=current_month.isoformat()
        print("aaaaaaaaaaaaaaaaaaaaaaaaaa",current_month)



        # Filter the data to only include entries from the current month
        # filtered_data = Drone.objects.filter(created_timestamp=current_month)
        filtered_data=Drone.objects.values_list('created_timestamp')
        # filtered_data=filtered_data.isoformat()

        filtered_data=tuple(filtered_data)
        # filtered_data=filtered_data.isoformat()

        # print(filtered_data)
        # month=filtered_data[0][0]
        for inner_tuple in filtered_data:
            filtered = inner_tuple[0]
            filtered=filtered.month
            print(filtered)
            # count=Drone.objects.filter(filtered=current_month).count()
            if filtered==current_month:
                count+=1
                print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCC",count)
        # month=month.month
        # month = filtered_data[0].month
        # print("mmmmmmmmmmmmmmmmmmmm",month)
        print("ssssssssssssssssssssssssss",filtered_data)
        print()
        # Count the number of entries in the filtered data
        # count = filtered_data.count()

        return Response(count)


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



# class MonthFlights_APIView(APIView):
#
#     def get(self, request):
#         # if is_month ==True:
#         d = pd.Timestamp(date)
#         num=current_time.month
#         m=calendar.month_name[num]
#         if int(d.month) == num:
#             tempDaysDictorMonth['month'] = m
#             tempDaysDictorMonth['count'] = Drone.objects.filter(created_timestamp=num).count()
#             tempDaysorMonth.append(tempDaysDictorMonth)
#             tempDaysDictorMonth = {}
#         #             else:
#         #                 for j in range(d.day, order_obj['ordered_time'].date().day + 1)[:5]:  #server
#         #                 # for j in range(d.month, order_obj['ordered_time__month']+1)[:5]: #local
#         #                         s=calendar.month_name[j]
#         #                         tempDaysDictorMonth['month'] = s
#         #                         tempDaysDictorMonth['count'] = Drone.objects.filter(created_timestamp=d.month).count()
#         #                         tempDaysorMonth.append(tempDaysDictorMonth)
#         #                         tempDaysDictorMonth = {}
#         # else:
#         print("jhsajhd")
#         return Response(tempDaysorMonth)
#

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
        drone_id=data.get('drone_id')

        if data:
            if drone_id:
                regcreate = GMap.objects.create(lng=lng,lat=lat,isActive=isActive)

                return Response("Data For Application, Added Sucessfully")

            else:
                return Response("ID Required For Application")
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
