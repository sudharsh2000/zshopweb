"""technocart URL Configuration

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
from django.urls import path

from reportapp import views

urlpatterns = [
path('apifetch',views.apifetch, name='apifetch'),
path('summaryrep',views.summaryreport, name='summaryreport'),
path('salerep',views.salereport, name='salerep'),
path('purchaserep',views.purchasereport, name='purchaserep'),
path('salereturnreport',views.srreport, name='salereturnreport'),
path('purchasereturnreport',views.prreport, name='purchasereturnreport'),

path('saleorderreport',views.soreport, name='saleorderreport'),
path('purchaseorderreport',views.poreport, name='purchaseorderreport'),

path('ledgerrep',views.ledgerreport, name='ledgerrep'),
path('summaryget/',views.summaryget, name='summaryget'),
path('salesget/',views.salesget, name='salesget'),
path('purchaseget/',views.purchaseget, name='purchaseget'),
path('ledgerget/',views.ledgerget, name='ledgerget'),
path('opget/',views.opget, name='opget'),
path('servicerep',views.servicereport, name='servicerep'),
path('lossprofiterep',views.lossprofitreport, name='lossprofitrep'),
path('lossprofitget/',views.lossprofitget, name='lossprofitget'),
path('ledgergrprep',views.ledgergroupreport, name='ledgergrprep'),
path('ledgergrpget/',views.ledgergrpget, name='ledgergrpget'),
path('saletaxrep',views.saletaxreport, name='saletaxrep'),
path('salestaxreportget/',views.salestaxreportget, name='salestaxreportget'),

]
