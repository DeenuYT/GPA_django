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

# semester 2 page
def sem2(request):
    template = loader.get_template('sem2.html')
    return HttpResponse(template.render())

# semester 3 page
def sem3(request):
    template = loader.get_template('sem3.html')
    return HttpResponse(template.render())

# semester 4 page
def sem4(request):
    template = loader.get_template('sem4.html')
    return HttpResponse(template.render())

# Evaluation of grades and grade points
def evaluate(x):
    if ((int(x)>=5 and int(x)<=10) or x=='O' or x=='A+' or x=='A' or x=='B+' or x=='B' or x=='C'):
        if x == 'O':
            return 10
        elif x == 'A+':
            return 9
        elif x == 'A':
            return 8
        elif x == 'B+':
            return 7
        elif x == 'B':
            return 6
        elif x == 'C':
            return 5
        else:
            return int(x)
    else:
        return None
# calculate semester 1
def calc_sem1(request):
    try:
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
    except:
        res = "Invalid or No Grades"
        return render(request, 'sem1.html', {'res': res})

# calculate semester 2
def calc_sem2(request):
    try:
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
        return render(request, 'sem2.html', {'res': res})
    except:
        res = "Invalid or No Grades"
        return render(request, 'sem2.html', {'res': res})

# calculate semester 3
def calc_sem3(request):
    try:
        EP = evaluate(str.upper(request.GET['EP']))
        EC = evaluate(str.upper(request.GET['EC']))
        EM = evaluate(str.upper(request.GET['EM']))
        EG = evaluate(str.upper(request.GET['EG']))
        TE = evaluate(str.upper(request.GET['TE']))
        SPC = evaluate(str.upper(request.GET['SPC']))
        P_CLab = evaluate(str.upper(request.GET['P_CLab']))
        SPCLab = evaluate(str.upper(request.GET['SPCLab']))
        DBMSLab = evaluate(str.upper(request.GET['DBMSLab']))
        SSLab = evaluate(str.upper(request.GET['SSLab']))
        res = ((EP*3) + (EC*3) + (EM*4) + (EG*3) + (TE*3) + (SPC*3) + P_CLab + SPCLab + SSLab + DBMSLab)/23
        return render(request, 'sem3.html', {'res': res})
    except:
        res = "Invalid or No Grades"
        return render(request, 'sem3.html', {'res': res})


# calculate semester 4
def calc_sem4(request):
    try:
        EP = evaluate(str.upper(request.GET['EP']))
        EC = evaluate(str.upper(request.GET['EC']))
        EM = evaluate(str.upper(request.GET['EM']))
        EG = evaluate(str.upper(request.GET['EG']))
        TE = evaluate(str.upper(request.GET['TE']))
        SPC = evaluate(str.upper(request.GET['SPC']))
        P_CLab = evaluate(str.upper(request.GET['P_CLab']))
        SPCLab = evaluate(str.upper(request.GET['SPCLab']))
        DBMSLab = evaluate(str.upper(request.GET['DBMSLab']))
        SSLab = evaluate(str.upper(request.GET['SSLab']))
        res = ((EP*3) + (EC*3) + (EM*4) + (EG*3) + (TE*0) + (SPC*3) + P_CLab + SPCLab + SSLab + DBMSLab)/20
        return render(request, 'sem4.html', {'res': res})
    except:
        res = "Enter all the fields"
        return render(request, 'sem4.html', {'res': res})