from django.shortcuts import render
from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
import joblib

def home_view(request):
    return render(request,'index.html')

def predictor_view(request):
    return render(request,'onionPriceInput.html')

def result_view(request):
    lis = []
    year = int(request.GET['Bosor'])
    month = int(request.GET['Month'])
    day = int(request.GET['Day'])
    lis.append(year)
    lis.append(month)
    lis.append(day)
    season = 0
    if (month == 1 and (day >= 1 and day <= 31)):
        season = 4
        lis.append(season)
    elif (month == 2 and (day >= 1 and day <= 12)):
        season = 4
        lis.append(season)
    elif (month == 2 and (day >= 13 and day <= 28)):
        season = 5
        lis.append(season)
    elif (month == 3 and (day >= 1 and day <= 31)):
        season = 5
        lis.append(season)
    elif month == 4 and (day >= 1 and day <= 13):
        season = 5
        lis.append(season)
    elif month == 4 and (day >= 14 and day <= 30):
        season = 0
        lis.append(season)
    elif month == 5 and (day >= 1 and day <= 31):
        season = 0
        lis.append(season)
    elif month == 6 and (day >= 1 and day <= 14):
        season = 0
        lis.append(season)
    elif month == 6 and (day >= 15 and day <= 30):
        season = 1
        lis.append(season)
    elif month == 7 and (day >= 1 and day <= 31):
        season = 1
        lis.append(season)
    elif month == 8 and (day >= 1 and day <= 15):
        season = 1
        lis.append(season)
    elif month == 8 and (day >= 16 and day <= 31):
        season = 2
        lis.append(season)
    elif month == 9 and (day >= 1 and day <= 30):
        season = 2
        lis.append(season)
    elif month == 10 and (day >= 1 and day <= 15):
        season = 2
        lis.append(season)
    elif month == 10 and (day >= 16 and day <= 31):
        season = 3
        lis.append(season)
    elif month == 11 and (day >= 1 and day <= 30):
        season = 3
        lis.append(season)
    elif month == 12 and (day >= 1 and day <= 14):
        season = 3
        lis.append(season)
    elif month == 12 and (day >= 15 and day <= 31):
        season = 4
        lis.append(season)

    clf = joblib.load('MLModel.sav')
    result = clf.predict([lis])
    result = result[0]
    context = {
        'result': result
    }
    return  render(request, 'predictionResult.html',context)