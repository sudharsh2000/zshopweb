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

from zshopapp import views

urlpatterns = [

path('',views.login,name='login'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('register',views.register,name='register'),
path('home/',views.home,name='home'),
path('adm',views.adminfu, name='adminfu'),

path('itemad/',views.itemadd,name='itemadd'),
path('itemcateg/',views.itemcategory,name='itemcategory'),
path('ledgergroup/',views.ledgroup,name='ledgergroup'),
path('ledgeradd/',views.ledgeradd,name='ledgeradd'),
path('cus/',views.cus,name="cus"),
path('sup/',views.sup,name="sup"),

path('search/',views.search_customer, name='search_customer'),
path('searchitem/', views.search_item, name='search_item'),
path('searchstockitem/', views.search_stockitem, name='searchstockitem'),
path('getprevious/', views.get_previous, name='get_previous'),
path('getpreviouspurchase/', views.get_previouspurchase, name='get_previouspurchase'),
path('getpreviouspaymentreceipt/', views.get_previoupaymentreceipt, name='get_previoupaymentreceipt'),
path('getcustomer/',views.get_customer, name='get_customer'),
path('getitem/',views.get_item, name='get_item'),
path('adduser',views.addcompany, name='addcompany'),
path('jobcard/',views.jobcard, name='jobcard'),
path('workcateg/',views.workcategory, name='workcateg'),
# path('summaryrep',views.summaryreport, name='summaryreport'),
# path('salerep',views.salereport, name='salerep'),
# path('purchaserep',views.purchasereport, name='purchaserep'),
# path('salereturnreport',views.srreport, name='salereturnreport'),
# path('purchasereturnreport',views.prreport, name='purchasereturnreport'),

# path('saleorderreport',views.soreport, name='saleorderreport'),
# path('purchaseorderreport',views.poreport, name='purchaseorderreport'),

# path('ledgerrep',views.ledgerreport, name='ledgerrep'),
# path('summaryget/',views.summaryget, name='summaryget'),
# path('salesget/',views.salesget, name='salesget'),
# path('purchaseget/',views.purchaseget, name='purchaseget'),
# path('ledgerget/',views.ledgerget, name='ledgerget'),

path('cleartrn/',views.cleartrn, name='cleartrn'),
path('printtrn/',views.printtrn, name='printtrn'),
path('printbarcode/',views.barcodeprint, name='barcodeprint'),
path('printbarcodeview/',views.barcodeprintview, name='barcodeprintview'),
path('edit/',views.editwindow, name='editwindow'),
path('getedit/',views.getedititems, name='getedititems'),
path('deleteedit/',views.deleteedititem, name='deleteedititem'),
path('getitemcateg/',views.getitemcateg, name='getitemcateg'),
path('useradd/',views.useradd,name='useradd'),
path('getusers/',views.getusers,name='getusers'),
path('Addarea/',views.stockareaadd,name='stockareaadd'),
path('getarea/',views.getarea,name='getarea'),
path('getvno/',views.getmaxvno,name='getmaxvno'),
path('validate/',views.createvalidation,name='createvalidation'),
path('getworkcateg/',views.getwrkcateg,name='getworkcateg'),
path('getjob/',views.getjob,name='getjob'),
path('editsearch/',views.editsearch,name='editsearch'),
path('translate/',views.translate_text,name='translate'),
path('getallitemcateg/',views.getallitemcateg, name='getallitemcateg'),
path('generate-zakat-qr/<customer>/<dates>/<vno>/<taxamt>/<totalamt>/', views.generate_zakat_qr, name='generate_zakat_qr'),
path('test/',views.testcode, name='test'),
path('generate-registration-code/', views.generate_registration_code, name='generate_registration_code'),

path('setproduct',views.setproduct,name='setproduct'),
path('finishproduct',views.finishedproduct,name='finishproduct'),
path('getproductset/', views.get_previousproductset, name='getproductset'),
path('getmaxproductid/', views.getmaxproductid, name='getmaxproductid'),
path('searchproductset/',views.searchproductset, name='searchproductset'),
path('getfinishproduct/', views.get_finishedproduct, name='getproductset'),
path('settings/', views.software_settings, name='settings'),
path('getmnusettings/', views.get_musettings, name='getmnusettings'),
]
