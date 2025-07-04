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
from django.conf.urls.static import static
from transactionapp import views
from zshop import settings

urlpatterns = [

path('sale/',views.addsale,name='sale'),
path('purchase/',views.addpurchase,name='purchase'),
path('salereturn/',views.addsalereturn,name='addsalereturn'),
path('purchasereturn/',views.addpurchasereturn,name='addpurchasereturn'),
path('saleorder/',views.addsaleorder,name='addsaleorder'),
path('purchaseorder/',views.addpurchaseorder,name='addpurchaseorder'),
path('receipt/',views.addreceipt,name='addreceipt'),
path('payment/',views.addpayment,name='addpayment'),
path('service/',views.service,name='service'),
path('checkvoucher/',views.checkvoucher, name='checkvoucher'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)