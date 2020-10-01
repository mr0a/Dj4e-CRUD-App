#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    num_visits = request.session.get('num_visits', 0) + 1
    resp = HttpResponse("<h1>view count="+str(num_visits)+"</h1>")
    resp.set_cookie('dj4e_cookie', '0ad5292c', max_age=1000)
    request.session['num_visits'] = num_visits
    if num_visits>4: del(request.session['num_visits'])
    return resp