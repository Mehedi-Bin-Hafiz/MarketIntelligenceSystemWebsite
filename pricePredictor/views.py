from django.shortcuts import render
from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import messages
import joblib
import time

def monthlyPredictor(year, month,clf):
    import calendar
    season = 0
    lis = list()
    lis.append(year)
    lis.append(month)
    predicted_resut = list()

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 2:
        if calendar.isleap(year):
            days = 29
        else:
            days = 28
    else:
        days = 30

    for i in range(1, days + 1):
        if (month == 1 and (i >= 1 and i <= 31)):
            season = 4
            lis.append(season)
        elif (month == 2 and (i >= 1 and i <= 12)):
            season = 4
            lis.append(season)
        elif (month == 2 and (i >= 13 and i <= 28)):
            season = 5
            lis.append(season)
        elif (month == 3 and (i >= 1 and i <= 31)):
            season = 5
            lis.append(season)
        elif month == 4 and (i >= 1 and i <= 13):
            season = 5
            lis.append(season)
        elif month == 4 and (i >= 14 and i <= 30):
            season = 0
            lis.append(season)
        elif month == 5 and (i >= 1 and i <= 31):
            season = 0
            lis.append(season)
        elif month == 6 and (i >= 1 and i <= 14):
            season = 0
            lis.append(season)
        elif month == 6 and (i >= 15 and i <= 30):
            season = 1
            lis.append(season)
        elif month == 7 and (i >= 1 and i <= 31):
            season = 1
            lis.append(season)
        elif month == 8 and (i >= 1 and i <= 15):
            season = 1
            lis.append(season)
        elif month == 8 and (i >= 16 and i <= 31):
            season = 2
            lis.append(season)
        elif month == 9 and (i >= 1 and i <= 30):
            season = 2
            lis.append(season)
        elif month == 10 and (i >= 1 and i <= 15):
            season = 2
            lis.append(season)
        elif month == 10 and (i >= 16 and i <= 31):
            season = 3
            lis.append(season)
        elif month == 11 and (i >= 1 and i <= 30):
            season = 3
            lis.append(season)
        elif month == 12 and (i >= 1 and i <= 14):
            season = 3
            lis.append(season)
        elif month == 12 and (i >= 15 and i <= 31):
            season = 4
            lis.append(season)
        result = clf.predict([[year,i,month,season]])
        result = result[0]
        predicted_resut.append(round(result,2))
    return predicted_resut

def home_view(request):
    return render(request,'index.html')

def onion_predictor_view(request):
    context = {
        'ProSelect': 'Onion',
    }
    return render(request, 'priceInput.html', context)
def onion_result_view(request):
    year = int(request.GET['Bosor'])
    month = int(request.GET['Month'])
    day = int(request.GET['Day'])
    clf = joblib.load('OnionRegressionModel.sav')
    montlyPrice = monthlyPredictor(year, month, clf)
    result = montlyPrice[day-1]
    labels=list()
    for label in range(1,len(montlyPrice)+1):
        labels.append(label)
    if result<40 and result>0:
        decision = 'Low'
    elif result<60 and result>=40:
        decision = 'Medium'
    else:
        decision = 'High'
    context = {
        'decision': decision,
        'product': 'Onion',
        'result': 'Price may be: {:.2f} taka'.format(result),
        'monthlyPrice': montlyPrice,
        'labels': labels,
    }
    return  render(request, 'priceResult.html', context)
def rice_predictor_view(request):
    context = {
        'ProSelect': 'Rice',
    }
    return render(request, 'priceInput.html', context)
def rice_result_view(request):
    year = int(request.GET['Bosor'])
    month = int(request.GET['Month'])
    day = int(request.GET['Day'])
    clf = joblib.load('riceRegressionModel.sav')
    montlyPrice = monthlyPredictor(year, month, clf)
    result = montlyPrice[day-1]
    labels = list()
    for label in range(1,len(montlyPrice)+1):
        labels.append(label)
    print('label:',labels)
    print('data:',montlyPrice)
    decision = 'None'
    if result < 95 and result > 0:
        decision = 'Low'
    elif result < 140 and result >= 95:
        decision = 'Medium'
    elif result >= 140:
        decision = 'High'
    context = {
        'decision': decision,
        'product': 'Rice',
        'result': 'Price may be: {:.2f} taka'.format(result),
        'monthlyPrice': montlyPrice,
        'labels': labels,

    }
    return  render(request, 'priceResult.html', context)


