from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# welcome page
def welcome(request):
    template = loader.get_template('welcomepage.html')
    return HttpResponse(template.render())

# home page
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# semester 1 page
def sem1(request):
    template = loader.get_template('sem1.html')
    return HttpResponse(template.render())

# Evaluation of grades and grade points
def evaluate(x):
    if x == 'O' and 'o':
        return 10
    elif x == 'A+' and 'a+':
        return 9
    elif x == 'A' and 'a':
        return 8
    elif x == 'B+' and 'b+':
        return 7
    elif x == 'B' and 'b':
        return 6
    elif x == 'C' and 'c':
        return 5
    else:
        return int(x)
    
# semester 1 page
def calc_sem1(request):
    EP = evaluate(str.upper(request.GET['EP']))
    EC = evaluate(str.upper(request.GET['EC']))
    EM = evaluate(str.upper(request.GET['EM']))
    EG = evaluate(str.upper(request.GET['EG']))
    TE = evaluate(str.upper(request.GET['TE']))
    SPC = evaluate(str.upper(request.GET['SPC']))
    P_CLab = evaluate(str.upper(request.GET['P_CLab']))
    SPCLab = evaluate(str.upper(request.GET['SPCLab']))
    SSLab = evaluate(str.upper(request.GET['SSLab']))
    res = ((EP*3) + (EC*3) + (EM*4) + (EG*3) + (TE*3) + (SPC*3) + P_CLab + SPCLab + SSLab)/22
    return render(request, 'sem1.html', {'res': res})