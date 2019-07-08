"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .views import bio_detail, access_data, biomodel_new
from .apiviews import BioModelList, BioModelDetails, BioModelSearch

urlpatterns = [
    path('biomodels/', BioModelList.as_view(), name='bio_list'),
    path('biomodel/<int:key>/', BioModelDetails.as_view(), name='bio_detail'),
    path('biomodel', access_data, name='access_data'),
    path('addrecord', biomodel_new, name='biomodel_new'),
    path('search', BioModelSearch.as_view(), name='search'),
]

