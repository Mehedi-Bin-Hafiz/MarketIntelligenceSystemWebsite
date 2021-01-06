import datetime
import calendar
month = 11
days = 1
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    days = 31
if month == 2:
    year = 2020
    if calendar.isleap(year):
        days = 29
    else:
        days =28

for i in range(1,days+1):

    if (month == 1 and (i >= 1 and i <= 31)):
        season = 4
        # lis.append(season)
    elif (month == 2 and (i >= 1 and i <= 12)):
        season = 4
        # lis.append(season)
    elif (month == 2 and (i >= 13 and i <= 28)):
        season = 5
        # lis.append(season)
    elif (month == 3 and (i >= 1 and i <= 31)):
        season = 5
        # lis.append(season)
    elif month == 4 and (i >= 1 and i <= 13):
        season = 5
        # lis.append(season)
    elif month == 4 and (i >= 14 and i <= 30):
        season = 0
        # lis.append(season)
    elif month == 5 and (i >= 1 and i <= 31):
        season = 0
        # lis.append(season)
    elif month == 6 and (i >= 1 and i <= 14):
        season = 0
        # lis.append(season)
    elif month == 6 and (i >= 15 and i <= 30):
        season = 1
        # lis.append(season)
    elif month == 7 and (i >= 1 and i <= 31):
        season = 1
        # lis.append(season)
    elif month == 8 and (i >= 1 and i <= 15):
        season = 1
        # lis.append(season)
    elif month == 8 and (i >= 16 and i <= 31):
        season = 2
        # lis.append(season)
    elif month == 9 and (i >= 1 and i <= 30):
        season = 2
        # lis.append(season)
    elif month == 10 and (i >= 1 and i <= 15):
        season = 2
        # lis.append(season)
    elif month == 10 and (i >= 16 and i <= 31):
        season = 3
        # lis.append(season)
    elif month == 11 and (i >= 1 and i <= 30):
        season = 3
        # lis.append(season)
    elif month == 12 and (i >= 1 and i <= 14):
        season = 3
        # lis.append(season)
    elif month == 12 and (i >= 15 and i <= 31):
        season = 4
        # lis.append(season)