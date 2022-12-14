if is_month ==True:
            d = pd.Timestamp(date)
            num=current_time.month
            m=calendar.month_name[num]
            if int(d.month) == num:
                tempDaysDictorMonth['month'] = m
                tempDaysDictorMonth['count'] = BookingDetail.objects.filter(ordered_time__month=num).count()
                tempDaysorMonth.append(tempDaysDictorMonth)
                tempDaysDictorMonth = {}
            else:
                for j in range(d.day, order_obj['ordered_time'].date().day + 1)[:5]:  #server
                # for j in range(d.month, order_obj['ordered_time__month']+1)[:5]: #local
                        s=calendar.month_name[j]
                        tempDaysDictorMonth['month'] = s
                        tempDaysDictorMonth['count'] = BookingDetail.objects.filter(ordered_time__month=d.month).count()
                        tempDaysorMonth.append(tempDaysDictorMonth)
                        tempDaysDictorMonth = {}
        else:
                print("jhsajhd")
        return Response(tempDaysorMonth)
