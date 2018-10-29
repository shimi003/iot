from django.shortcuts import render
from django.http import HttpResponse
from temp.models import Meas as meas 

# Create your views here.
def index(request):
    max_pos = len(meas.objects.values_list('date')) - 1
    _date = meas.objects.values_list('date')[max_pos][0]
    _time = meas.objects.values_list('time')[max_pos][0]
    _temp = meas.objects.values_list('temp')[max_pos][0]
    _pres = meas.objects.values_list('pres')[max_pos][0]
    _hum =  meas.objects.values_list('hum')[max_pos][0]
    ret = {}
    ret['_date'] = _date
    ret['_time'] = _time
    ret['_temp'] = _temp
    ret['_pres'] = _pres
    ret['_hum']  = _hum

    return HttpResponse(str(ret))


 
