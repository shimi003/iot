from django.shortcuts import render
from django.http import HttpResponse
from temp.models import Meas as meas

# Create your views here.

def index(request):

    dates_list = meas.objects.values_list('date', flat=True).order_by('-date').distinct()
    dates = [entry0 for entry0 in dates_list]
    _date = dates[0]

    label_list = meas.objects.values_list('time', flat=True).filter(date=_date)    
    temp_list = meas.objects.values_list('temp', flat=True).filter(date=_date)    
    hum_list = meas.objects.values_list('hum', flat=True).filter(date=_date)    
    label = [entry1 for entry1 in label_list]
    temp = [entry2 for entry2 in temp_list]
    hum = [entry3 for entry3 in hum_list]
    context = {'dates': dates, 'date': _date, 'times': label, 'temp': temp, 'hum': hum} 
    return render(request, 'temp_view.html', context)


def date(request, ymd):
    try:
        ret = ymd.split('/')

        if len(ret) != 3:
            return HttpResponse('') 

        else:
            year = int(ret[0])
            month = int(ret[1])
            day = int(ret[2])

            if ((year < 1900) | (2100 < year)) | \
               ((month < 1) | (12 < month)) | \
               ((day < 1) | (31 < day)):
                return HttpResponse('')

            else:
                candidate = "{0:04}/{1:02}/{2:02}".format(year,month,day)
                dates_list = meas.objects.values_list('date', flat=True).order_by('-date').distinct()
                dates = [entry0 for entry0 in dates_list]
                _date = '' 
                if candidate in dates:
                    _date = candidate
                else: 
                    _date = dates[0]

                label_list = meas.objects.values_list('time', flat=True).filter(date=_date)
                temp_list = meas.objects.values_list('temp', flat=True).filter(date=_date)
                hum_list = meas.objects.values_list('hum', flat=True).filter(date=_date)
                label = [entry1 for entry1 in label_list]
                temp = [entry2 for entry2 in temp_list]
                hum = [entry3 for entry3 in hum_list]
                context = {'dates': dates, 'date': _date, 'times': label, 'temp': temp, 'hum': hum}
                return render(request, 'temp_view.html', context)    

    except:     
        index(request)


