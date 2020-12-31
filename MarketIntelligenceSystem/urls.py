"""MarketIntelligenceSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pricePredictor.views import onion_predictor_view,onion_result_view,home_view,rice_predictor_view,rice_result_view
from reviewAnalyst.views import review_input, review_result
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name= 'home'),
    path('onionpredictor/',onion_predictor_view,name='onionPredictor'),
    path('onionresult/',onion_result_view, name = 'onionResult'),
    path('reviewInput/',review_input, name = 'reviewInput'),
    path('reviewresult/',review_result, name = 'reviewResult'),
    path('ricepredictor/', rice_predictor_view, name='ricePredictor'),
    path('riceresult/', rice_result_view, name='riceResult'),

]