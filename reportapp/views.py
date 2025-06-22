from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
import datetime
from datetime import timedelta
from django.db.models import Sum,F
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from zshopapp.models import *
import datetime

import json

from itertools import chain
import pdb;

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models.functions import Cast
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Q
from django.db.models import Q, Max
from django.db.models import Max, IntegerField, F
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from zshopapp.views import deletesales

def apifetch(request):
     return JsonResponse([{
          'name':"sudharsh",
          'age':24,
          'job':"computer Engineer"
     },{
       'name':"anagha",
          'age':22,
          'job':"Psc Coaching"   
     }],safe=False)

@login_required(login_url='login')  
def summaryreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow = today + timedelta(days=1)

# Print tomorrow's date in the same format
    tomorrow_date = tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'summaryreport.html',{'fromdate':fromdate,'todate':tomorrow_date,'us':us,'company':company,'area':area,'cuser':user,'user':company})

@login_required(login_url='login')  
def salereport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'salesreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})
@login_required(login_url='login')  
def purchasereport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'purchasereport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})


@login_required(login_url='login')  
def srreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'srreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})
@login_required(login_url='login')  
def prreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'prreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})


@login_required(login_url='login')  
def soreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'soreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})
@login_required(login_url='login')  
def poreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'poreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})

@login_required(login_url='login')  
def ledgerreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'ledgerreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})

@login_required(login_url='login')
def summaryget(request):

    company = request.GET.get('comp')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    
    if chkarea=='all':
        print("Type1")
        fromdate  = request.GET.get('fromdt')
        todate= request.GET.get('todt')
        cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company)
    
        openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
        Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company)
    
        openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
        purchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company)
    
        total_purchase = purchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
        cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company)
    
        totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
        creditpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company).exclude(ledcodecr=1)
    
        totalcreditpurchase = creditpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
        pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company)
    
        totalpr = pr.aggregate(totalpr=Sum('amt',default=0))['totalpr']
        prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company).exclude(ledcodecr__gt=30)
    
        totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
        sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company)
    
        totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
        salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company)
    
        totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
        salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company)
    
        totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
        salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company).exclude(ledcodedr='1').exclude(ledcodedr='28')
    
        totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
        sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company)
    
        totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
        srcash = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,ledcodecr=1)
    
        totalsrcash = srcash.aggregate(totalsrcash=Sum('amt',default=0))['totalsrcash']
        srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company).exclude(ledcodecr='1').exclude(ledcodecr='28')
    
        totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
        paytax = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company)
    
        paymenttax = paytax.aggregate(paymenttax=Sum('rptaxamt',default=0))['paymenttax']

        issuecode=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company).values_list('issuecode', flat=True)
        stax = Tblissuedetails.objects.filter(issuecode__in=issuecode,vtype='SI',company=company)
    
        saletax = stax.aggregate(saletax=Sum('taxrate',default=0))['saletax']

        recptcode=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company).values_list('recptcode', flat=True)
        taxsr = Tblreceiptdetails.objects.filter(recptcode__in=recptcode,vtype='SR',company=company)
    
        srtax = taxsr.aggregate(srtax=Sum('taxrate',default=0))['srtax']

        recptcodepur=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company).values_list('recptcode', flat=True)
        taxpur = Tblreceiptdetails.objects.filter(recptcode__in=recptcodepur,vtype='PI',company=company)
    
        purchasetax = taxpur.aggregate(purchasetax=Sum('taxrate',default=0))['purchasetax']


        issuecodepr=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company).values_list('issuecode', flat=True)
        taxpr = Tblissuedetails.objects.filter(issuecode__in=issuecodepr,vtype='PR',company=company)
    
        prtax = taxpr.aggregate(prtax=Sum('taxrate',default=0))['prtax']


        pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company)
    
        payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
        rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company)
    
        receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
        ledcode=Tblaccountledger.objects.filter(agroupid=24).values_list('lid', flat=True)
        bank = Tblgeneralledger.objects.filter(ledcode__in=ledcode,vdate__range=[fromdate, todate],company=company)
    
        totbank = bank.aggregate(totbank=Sum('dbamt')-Sum('cramt'))['totbank']

        cash = Tblgeneralledger.objects.filter(ledcode=1,vdate__range=[fromdate, todate],company=company)
    
        totcash = cash.aggregate(totcash=Sum('dbamt')-Sum('cramt'))['totcash']
        print(totcash)
        if totbank==None:
            totbank=0
        if totcash==None:
            totcash=0


        cus = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='18',company=company)
        cusd=cus.aggregate(cusd=Sum('dbamt',default=0))['cusd']
        cusc=cus.aggregate(cusc=Sum('cramt',default=0))['cusc']
        cusdb=cusd
        cuscr=cusc
    
        cusremain=cusdb - cuscr
   
    
        sup = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='19',company=company)
        supdb=sup.aggregate(supdb=Sum('dbamt',default=0))['supdb']
        supcr=sup.aggregate(supcr=Sum('cramt',default=0))['supcr']
        supremain=int( supdb) - int( supcr)
    else:
        if curuser=='HEAD OFFICE' and chkarea=='no':
            if chkuser=='all':
                print("Type2",area)
                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,area=area)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                purchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area)
            
                total_purchase = purchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,area=area)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                creditpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area).exclude(ledcodecr=1)
            
                totalcreditpurchase = creditpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area)
            
                totalpr = pr.aggregate(totalpr=Sum('amt',default=0))['totalpr']
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,area=area)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,area=area)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company,area=area).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcash = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,ledcodecr=1,area=area)
            
                totalsrcash = srcash.aggregate(totalsrcash=Sum('amt',default=0))['totalsrcash']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                paytax = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area)
            
                paymenttax = paytax.aggregate(paymenttax=Sum('rptaxamt',default=0))['paymenttax']

                issuecode=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',area=area,company=company).values_list('issuecode', flat=True)
                stax = Tblissuedetails.objects.filter(issuecode__in=issuecode,vtype='SI',company=company)
            
                saletax = stax.aggregate(saletax=Sum('taxrate',default=0))['saletax']

                recptcode=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',area=area,company=company).values_list('recptcode', flat=True)
                taxsr = Tblreceiptdetails.objects.filter(recptcode__in=recptcode,vtype='SR',company=company)
            
                srtax = taxsr.aggregate(srtax=Sum('taxrate',default=0))['srtax']

                recptcodepur=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',area=area,company=company).values_list('recptcode', flat=True)
                taxpur = Tblreceiptdetails.objects.filter(recptcode__in=recptcodepur,vtype='PI',company=company)
            
                purchasetax = taxpur.aggregate(purchasetax=Sum('taxrate',default=0))['purchasetax']


                issuecodepr=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',area=area,company=company).values_list('issuecode', flat=True)
                taxpr = Tblissuedetails.objects.filter(issuecode__in=issuecodepr,vtype='PR',company=company)
            
                prtax = taxpr.aggregate(prtax=Sum('taxrate',default=0))['prtax']


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,area=area)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                ledcode=Tblaccountledger.objects.filter(agroupid=24).values_list('lid', flat=True)
                bank = Tblgeneralledger.objects.filter(ledcode__in=ledcode,vdate__range=[fromdate, todate],company=company,area=area)
            
                totbank = bank.aggregate(totbank=Sum('dbamt')-Sum('cramt'))['totbank']

                cash = Tblgeneralledger.objects.filter(ledcode=1,vdate__range=[fromdate, todate],company=company,area=area)
            
                totcash = cash.aggregate(totcash=Sum('dbamt')-Sum('cramt'))['totcash']
        
                if totbank==None:
                    totbank=0
                if totcash==None:
                    totcash=0


                cus = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='18',area=area,company=F('tblaccountledger__company'))
                cusd=cus.aggregate(cusd=Sum('dbamt',default=0))['cusd']
                cusc=cus.aggregate(cusc=Sum('cramt',default=0))['cusc']
                cusdb=cusd
                cuscr=cusc
            
                cusremain=cusdb - cuscr
            
            
                sup = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='19',area=area,company=F('tblaccountledger__company'))
                supdb=sup.aggregate(supdb=Sum('dbamt',default=0))['supdb']
                supcr=sup.aggregate(supcr=Sum('cramt',default=0))['supcr']
                supremain=int( supdb) - int( supcr)




            else:
                print("Type3")

                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area,uid=user)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,uid=user,area=area)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                purchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,uid=user,area=area)
            
                total_purchase = purchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,uid=user,area=area)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                creditpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,uid=user,area=area).exclude(ledcodecr=1)
            
                totalcreditpurchase = creditpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,uid=user,area=area)
            
                totalpr = pr.aggregate(totalpr=Sum('amt',default=0))['totalpr']
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,uid=user,area=area).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,uid=user,area=area)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,uid=user,area=area)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,uid=user,area=area)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company,uid=user,area=area).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,uid=user,area=area)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcash = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,ledcodecr=1,uid=user,area=area)
            
                totalsrcash = srcash.aggregate(totalsrcash=Sum('amt',default=0))['totalsrcash']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,uid=user,area=area).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                paytax = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,uid=user,area=area)
            
                paymenttax = paytax.aggregate(paymenttax=Sum('rptaxamt',default=0))['paymenttax']

                issuecode=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',uid=user,area=area).values_list('issuecode', flat=True)
                stax = Tblissuedetails.objects.filter(issuecode__in=issuecode,vtype='SI',company=company)
            
                saletax = stax.aggregate(saletax=Sum('taxrate',default=0))['saletax']

                recptcode=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',uid=user,area=area).values_list('recptcode', flat=True)
                taxsr = Tblreceiptdetails.objects.filter(recptcode__in=recptcode,vtype='SR',company=company)
            
                srtax = taxsr.aggregate(srtax=Sum('taxrate',default=0))['srtax']

                recptcodepur=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',uid=user,area=area).values_list('recptcode', flat=True)
                taxpur = Tblreceiptdetails.objects.filter(recptcode__in=recptcodepur,vtype='PI',company=company)
            
                purchasetax = taxpur.aggregate(purchasetax=Sum('taxrate',default=0))['purchasetax']


                issuecodepr=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',uid=user,area=area).values_list('issuecode', flat=True)
                taxpr = Tblissuedetails.objects.filter(issuecode__in=issuecodepr,vtype='PR',company=company)
            
                prtax = taxpr.aggregate(prtax=Sum('taxrate',default=0))['prtax']


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,uid=user,area=area)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,uid=user,area=area)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                ledcode=Tblaccountledger.objects.filter(agroupid=24).values_list('lid', flat=True)
                bank = Tblgeneralledger.objects.filter(ledcode__in=ledcode,vdate__range=[fromdate, todate],company=company,uid=user,area=area)
            
                totbank = bank.aggregate(totbank=Sum('dbamt')-Sum('cramt'))['totbank']

                cash = Tblgeneralledger.objects.filter(ledcode=1,vdate__range=[fromdate, todate],company=company,uid=user,area=area)
            
                totcash = cash.aggregate(totcash=Sum('dbamt')-Sum('cramt'))['totcash']
        
                if totbank==None:
                    totbank=0
                if totcash==None:
                    totcash=0


                cus = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='18',uid=user,area=area,company=F('tblaccountledger__company'))
                cusd=cus.aggregate(cusd=Sum('dbamt',default=0))['cusd']
                cusc=cus.aggregate(cusc=Sum('cramt',default=0))['cusc']
                cusdb=cusd
                cuscr=cusc
            
                cusremain=cusdb - cuscr
            
            
                sup = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='19',uid=user,area=area,company=F('tblaccountledger__company'))
                supdb=sup.aggregate(supdb=Sum('dbamt',default=0))['supdb']
                supcr=sup.aggregate(supcr=Sum('cramt',default=0))['supcr']
                supremain=int( supdb) - int( supcr)
    
        else:
            if chkuser=='all':
                print("Type4")
                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,area=area)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                purchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area)
            
                total_purchase = purchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,area=area)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                creditpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area).exclude(ledcodecr=1)
            
                totalcreditpurchase = creditpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area)
            
                totalpr = pr.aggregate(totalpr=Sum('amt',default=0))['totalpr']
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,area=area)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,area=area)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company,area=area).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcash = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,ledcodecr=1,area=area)
            
                totalsrcash = srcash.aggregate(totalsrcash=Sum('amt',default=0))['totalsrcash']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                paytax = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area)
            
                paymenttax = paytax.aggregate(paymenttax=Sum('rptaxamt',default=0))['paymenttax']

                issuecode=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',area=area,company=company).values_list('issuecode', flat=True)
                stax = Tblissuedetails.objects.filter(issuecode__in=issuecode,vtype='SI',company=company)
            
                saletax = stax.aggregate(saletax=Sum('taxrate',default=0))['saletax']

                recptcode=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',area=area,company=company).values_list('recptcode', flat=True)
                taxsr = Tblreceiptdetails.objects.filter(recptcode__in=recptcode,vtype='SR',company=company)
            
                srtax = taxsr.aggregate(srtax=Sum('taxrate',default=0))['srtax']

                recptcodepur=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',area=area,company=company).values_list('recptcode', flat=True)
                taxpur = Tblreceiptdetails.objects.filter(recptcode__in=recptcodepur,vtype='PI',company=company)
            
                purchasetax = taxpur.aggregate(purchasetax=Sum('taxrate',default=0))['purchasetax']


                issuecodepr=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',area=area,company=company).values_list('issuecode', flat=True)
                taxpr = Tblissuedetails.objects.filter(issuecode__in=issuecodepr,vtype='PR',company=company)
            
                prtax = taxpr.aggregate(prtax=Sum('taxrate',default=0))['prtax']


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,area=area)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                ledcode=Tblaccountledger.objects.filter(agroupid=24).values_list('lid', flat=True)
                bank = Tblgeneralledger.objects.filter(ledcode__in=ledcode,vdate__range=[fromdate, todate],company=company,area=area)
            
                totbank = bank.aggregate(totbank=Sum('dbamt')-Sum('cramt'))['totbank']

                cash = Tblgeneralledger.objects.filter(ledcode=1,vdate__range=[fromdate, todate],company=company,area=area)
            
                totcash = cash.aggregate(totcash=Sum('dbamt')-Sum('cramt'))['totcash']
        
                if totbank==None:
                    totbank=0
                if totcash==None:
                    totcash=0


                cus = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='18',area=area,company=F('tblaccountledger__company'))
                cusd=cus.aggregate(cusd=Sum('dbamt',default=0))['cusd']
                cusc=cus.aggregate(cusc=Sum('cramt',default=0))['cusc']
                cusdb=cusd
                cuscr=cusc
            
                cusremain=cusdb - cuscr
            
            
                sup = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='19',area=area,company=F('tblaccountledger__company'))
                supdb=sup.aggregate(supdb=Sum('dbamt',default=0))['supdb']
                supcr=sup.aggregate(supcr=Sum('cramt',default=0))['supcr']
                supremain=int( supdb) - int( supcr)




            else:
                print("Type5")

                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area,uid=user)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,uid=user,area=area)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                purchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,uid=user,area=area)
            
                total_purchase = purchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,uid=user,area=area)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                creditpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,uid=user,area=area).exclude(ledcodecr=1)
            
                totalcreditpurchase = creditpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,uid=user,area=area)
            
                totalpr = pr.aggregate(totalpr=Sum('amt',default=0))['totalpr']
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,uid=user,area=area).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,uid=user,area=area)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,uid=user,area=area)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,uid=user,area=area)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company,uid=user,area=area).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,uid=user,area=area)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcash = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,ledcodecr=1,uid=user,area=area)
            
                totalsrcash = srcash.aggregate(totalsrcash=Sum('amt',default=0))['totalsrcash']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,uid=user,area=area).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                paytax = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,uid=user,area=area)
            
                paymenttax = paytax.aggregate(paymenttax=Sum('rptaxamt',default=0))['paymenttax']

                issuecode=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',uid=user,area=area).values_list('issuecode', flat=True)
                stax = Tblissuedetails.objects.filter(issuecode__in=issuecode,vtype='SI',company=company)
            
                saletax = stax.aggregate(saletax=Sum('taxrate',default=0))['saletax']

                recptcode=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',uid=user,area=area).values_list('recptcode', flat=True)
                taxsr = Tblreceiptdetails.objects.filter(recptcode__in=recptcode,vtype='SR',company=company)
            
                srtax = taxsr.aggregate(srtax=Sum('taxrate',default=0))['srtax']

                recptcodepur=TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',uid=user,area=area).values_list('recptcode', flat=True)
                taxpur = Tblreceiptdetails.objects.filter(recptcode__in=recptcodepur,vtype='PI',company=company)
            
                purchasetax = taxpur.aggregate(purchasetax=Sum('taxrate',default=0))['purchasetax']


                issuecodepr=Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',uid=user,area=area).values_list('issuecode', flat=True)
                taxpr = Tblissuedetails.objects.filter(issuecode__in=issuecodepr,vtype='PR',company=company)
            
                prtax = taxpr.aggregate(prtax=Sum('taxrate',default=0))['prtax']


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,uid=user,area=area)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,uid=user,area=area)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                ledcode=Tblaccountledger.objects.filter(agroupid=24).values_list('lid', flat=True)
                bank = Tblgeneralledger.objects.filter(ledcode__in=ledcode,vdate__range=[fromdate, todate],company=company,uid=user,area=area)
            
                totbank = bank.aggregate(totbank=Sum('dbamt')-Sum('cramt'))['totbank']

                cash = Tblgeneralledger.objects.filter(ledcode=1,vdate__range=[fromdate, todate],company=company,uid=user,area=area)
            
                totcash = cash.aggregate(totcash=Sum('dbamt')-Sum('cramt'))['totcash']
        
                if totbank==None:
                    totbank=0
                if totcash==None:
                    totcash=0


                cus = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='18',uid=user,area=area,company=F('tblaccountledger__company'))
                cusd=cus.aggregate(cusd=Sum('dbamt',default=0))['cusd']
                cusc=cus.aggregate(cusc=Sum('cramt',default=0))['cusc']
                cusdb=cusd
                cuscr=cusc
            
                cusremain=cusdb - cuscr
            
            
                sup = Tblgeneralledger.objects.filter(ledcode=F('tblaccountledger__lid'),vdate__range=[fromdate, todate],tblaccountledger__agroupid='19',uid=user,area=area,company=F('tblaccountledger__company'))
                supdb=sup.aggregate(supdb=Sum('dbamt',default=0))['supdb']
                supcr=sup.aggregate(supcr=Sum('cramt',default=0))['supcr']
                supremain=int( supdb) - int( supcr)
           
    
    print("bank ",totbank)
    data = [{'opcash': openingcash, 'opbank': openingbank,'totpurchase':total_purchase,'totcashpurchase':totalcashpurchase,
    'totcreditpurchase':totalcreditpurchase,'totpr':totalpr,'totsale':totalsale,'totsalecard':totalsalecard,'totsalecash':totalsalecash,
    'totsalecredit':totalsalecredit,'totsr':totalsr,'totsrcash':totalsrcash,'totsrcredit':totalsrcredit,'paymenttax':paymenttax,'saletax':saletax,
    'srtax':srtax,'purchasetax':purchasetax,'prtax':prtax,'payment':payment,'receipt':receipt,'totbank':totbank,'totcash':totcash,'supremain':supremain,'cusremain':cusremain,'totalprwithoutcr':totalprwithoutcr} ]
    
    return JsonResponse({'reportdata': data})



def salesget(request):
    vtype=request.GET.get('vtype')
    company = request.GET.get('comp')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    fromdate  = request.GET.get('fromdt')
    todate= request.GET.get('todt')
    if vtype=='SI' or vtype == 'SO' or vtype == 'SS':

        if chkarea=='all':
            results = Tblbusinessissue.objects.filter(
            issuetype=vtype,
            ledcodecr=2,
            company=company,
            issuedate__range=[fromdate,todate]
            ).annotate(
            Qty=F('qty'),
            freeQty=Sum('tblissuedetails__freeqty'),
            Taxamt=F('taxamt') * 100 / 100,
            amount=((F('amt') * 100 / 100) ) - F('taxamt'),
            discount=F('discamt'),
            netAmount=F('amt') * 100 / 100,
            cash=F('adamount'),
            mainAccount=F('ledcodedr'),
            user=F('uid'),
            dt=F('issuedate'),
            VVno=F('vno')
            ).order_by('issuedate')
            print("my data is",len(results))
            data = [{'vno': result.VVno,'qty': result.Qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
        else:
            if curuser=='HEAD OFFICE' and chkarea=='no':
                if chkuser=='all':
                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodecr=2,
                    company=company,area=area,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),  
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

            



                else:
                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodecr=2,company=company,area=area,uid=user,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),                 
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
            else:
                if chkuser=='all':

                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodecr=2,
                    company=company,area=area,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),                 
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]


                else:
                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodecr=2,
                    company=company,area=area,uid=user,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

    else:
        if chkarea=='all':

            results = TblTransactionReceipt.objects.filter(
            recpttype=vtype,
            ledcodedr=2,
            company=company,
            recptdate__range=[fromdate,todate]
            ).annotate(
            Qty=F('qty'), 
            freeQty=Sum('recptdetails__freeqty'),
            Taxamt=F('taxamt') * 100 / 100,
            amount=((F('amt') * 100 / 100) ) - F('taxamt'),
            discount=F('discamt'),
            netAmount=F('amt') * 100 / 100,
            cash=F('adamount'),
            mainAccount=F('ledcodecr'),
            user=F('uid'),
            dt=F('recptdate'),
            Refno=F('refno'),
            VVno=F('vno')
            ).order_by('recptdate')
            print("my data is",len(results))
            data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'refno':result.Refno,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

      
        else:
        
            if curuser=='HEAD OFFICE' and chkarea=='no':
                if chkuser=='all':
                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=2,
                    company=company,area=area,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodecr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

            



                else:
                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=2,
                    company=company,area=area,uid=user,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodecr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
            else:
                if chkuser=='all':

                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=2,
                    company=company,area=area,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]


                else:
                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=2,
                    company=company,area=area,uid=user,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),                 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

                                          
           
    
    
    
    return JsonResponse({'reportdata': data})



def purchaseget(request):
    vtype=request.GET.get('vtype')
    print(vtype)
    company = request.GET.get('comp')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    fromdate  = request.GET.get('fromdt')
    todate= request.GET.get('todt')
    if vtype=='PI' or vtype=='PO':
        if chkarea=='all':
            results = TblTransactionReceipt.objects.filter(
            recpttype=vtype,
            ledcodedr=3,
            company=company,
            recptdate__range=[fromdate,todate]
            ).annotate(
            Qty=F('qty'), 
            freeQty=Sum('recptdetails__freeqty'),
            Taxamt=F('taxamt') * 100 / 100,
            amount=((F('amt') * 100 / 100) ) - F('taxamt'),
            discount=F('discamt'),
            netAmount=F('amt') * 100 / 100,
            cash=F('adamount'),
            mainAccount=F('ledcodecr'),
            user=F('uid'),
            dt=F('recptdate'),
            Refno=F('refno'),
            VVno=F('vno')
            ).order_by('recptdate')
            print("my data is",len(results))
            data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'refno':result.Refno,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
        else:
            if curuser=='HEAD OFFICE' and chkarea=='no':
                if chkuser=='all':
                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=3,
                    company=company,area=area,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodecr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

            



                else:
                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=3,
                    company=company,area=area,uid=user,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodecr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
            else:
                if chkuser=='all':

                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=3,
                    company=company,area=area,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]


                else:
                    results = TblTransactionReceipt.objects.filter(
                    recpttype=vtype,
                    ledcodedr=3,
                    company=company,area=area,uid=user,
                    recptdate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),                 
                    freeQty=Sum('recptdetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('recptdate'),
                    VVno=F('vno')
                    ).order_by('recptdate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]
    else:
        if chkarea=='all':
            results = Tblbusinessissue.objects.filter(
            issuetype=vtype,
            ledcodedr=3,
            company=company,
            issuedate__range=[fromdate,todate]
            ).annotate(
            Qty=F('qty'),
            freeQty=Sum('tblissuedetails__freeqty'),
            Taxamt=F('taxamt') * 100 / 100,
            amount=((F('amt') * 100 / 100) ) - F('taxamt'),
            discount=F('discamt'),
            netAmount=F('amt') * 100 / 100,
            cash=F('adamount'),
            mainAccount=F('ledcodedr'),
            user=F('uid'),
            dt=F('issuedate'),
            VVno=F('vno')
            ).order_by('issuedate')
            print("my data is",len(results))
            data = [{'vno': result.VVno,'qty': result.Qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
        else:
            if curuser=='HEAD OFFICE' and chkarea=='no':
                if chkuser=='all':
                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodedr=3,
                    company=company,area=area,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),  
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

            



                else:
                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodedr=3,company=company,area=area,uid=user,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),                 
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

        
            else:
                if chkuser=='all':

                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodedr=3,
                    company=company,area=area,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'),                 
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]


                else:
                    results = Tblbusinessissue.objects.filter(
                    issuetype=vtype,
                    ledcodedr=3,
                    company=company,area=area,uid=user,
                    issuedate__range=[fromdate,todate]
                    ).annotate(
                    Qty=F('qty'), 
                    freeQty=Sum('tblissuedetails__freeqty'),
                    Taxamt=F('taxamt') * 100 / 100,
                    amount=((F('amt') * 100 / 100) ) - F('taxamt'),
                    discount=F('discamt'),
                    netAmount=F('amt') * 100 / 100,
                    cash=F('adamount'),
                    mainAccount=F('ledcodedr'),
                    user=F('uid'),
                    dt=F('issuedate'),
                    VVno=F('vno')
                    ).order_by('issuedate')
                    print("my data is",len(results))
                    data = [{'vno': result.VVno,'qty': result.qty,'freeqty':result.freeQty,'lid':result.mainAccount,'dat':result.dt, 'user':result.user,'taxamt': result.Taxamt,'amount':result.amount} for result in results ]

                        
           
    
    
    
    return JsonResponse({'reportdata': data})

def opget(request):
    company=request.session.get('company')
    lid = request.GET.get('lid')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    fromdate  = request.GET.get('fromdt')
    


    current_time = datetime.datetime.now().time()

    # Combine date and time
    
    

    if chkarea=='all':
        results =Tblgeneralledger.objects.get(ledcode=lid,company=company,vtype='OB')
        total_sum = Tblgeneralledger.objects.filter(ledcode=lid,company=company,vdate__range=['1995-01-31 00:00:00.000000',fromdate]
            ).exclude(vtype='OB').aggregate(
                total=Sum(F('dbamt') - F('cramt'))
            )
        
        results_value = float(results.dbamt)  # Replace 'dbamt' with the correct field if different

# Extract the sum from the total_sum dictionary
        total_sum_value = float(total_sum['total'] or 0)  # Default to 0 if 'total' is None

        # Sum the values
        data = total_sum_value+results_value
        
        print(data)
    else:
        if curuser=='HEAD OFFICE' and chkarea=='no':
            if chkuser=='all':
                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]

         



            else:
                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,user=user,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]

                
    
        else:
            if chkuser=='all':

                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]


            else:
                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,user=user,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]
      
           
    
    
    
    return JsonResponse({'reportdata': data})
    

def ledgerget(request):

    company = request.GET.get('comp')
    lid = request.GET.get('lid')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    fromdate  = request.GET.get('fromdt')
    todate= request.GET.get('todt')
    print(chkarea)
    if chkarea=='all':
        results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,vdate__range=[fromdate,todate]).exclude(vtype='OB')
        data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]

    else:
        if curuser=='HEAD OFFICE' and chkarea=='no':
            if chkuser=='all':
                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]

         



            else:
                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,user=user,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]

                
    
        else:
            if chkuser=='all':

                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]


            else:
                results =Tblgeneralledger.objects.filter(ledcode=lid,company=company,area=area,user=user,vdate__range=[fromdate,todate])
                data = [{'vno': result.vno,'vtype': result.vtype,'ledcode': result.ledcode,'vdate': result.vdate,'particulars':result.particulars,'dbamt':result.dbamt,'cramt':result.cramt, 'note':result.naration2,'user':result.uid} for result in results ]
      
           
    
    
    
    return JsonResponse({'reportdata': data})


@login_required(login_url='login')  
def servicereport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'servicereport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})

@login_required(login_url='login')  
def lossprofitreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'lossprofitreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})
@login_required(login_url='login')
def lossprofitget(request):

    company = request.GET.get('comp')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    
    if chkarea=='all':
        print("Type1")
        fromdate  = request.GET.get('fromdt')
        todate= request.GET.get('todt')
        cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company)
    
        openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
        Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company)
    
        openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
        
        cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company)
    
        totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
        
        prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company).exclude(ledcodecr__gt=30)
    
        totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
        sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company)
    
        totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
        salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company)
    
        totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
        salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company)
    
        totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
        salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company).exclude(ledcodedr='1').exclude(ledcodedr='28')
    
        totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
        sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company)
    
        totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
        srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company).exclude(ledcodecr='1').exclude(ledcodecr='28')
    
        totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
        


        pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company)
    
        payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
        rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company)
    
        receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
        rec = Tblbatch.objects.filter(company=company)
    
        costrate = rec.aggregate(costrate=Sum('crate',default=0))['costrate']
        sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company)
    
        salegross= sale.aggregate(salegross=Sum('amt',default=0)-Sum('taxamt',default=0))['salegross']
        pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company)
    
        prgross= pr.aggregate(prgross=Sum('amt',default=0)-Sum('taxamt',default=0))['prgross']
        pi = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company)
    
        pigross = pi.aggregate(pigross=Sum('amt',default=0)-Sum('taxamt',default=0))['pigross']
        sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company)
    
        srgross = sr.aggregate(srgross=Sum('amt',default=0)-Sum('taxamt',default=0))['srgross']
        grossprofit=float( salegross+prgross)-float(pigross+srgross)
        ledcodeincome=Tblaccountledger.objects.filter(agroupid=16).values_list('lid', flat=True)
        income = Tblgeneralledger.objects.filter(ledcode__in=ledcodeincome,vdate__range=[fromdate, todate],company=company)
            
        totindincome = income.aggregate(totindincome=Sum('cramt',default=0))['totindincome']
        ledcodeexp=Tblaccountledger.objects.filter(agroupid=15).values_list('lid', flat=True)
        expense = Tblgeneralledger.objects.filter(ledcode__in=ledcodeexp,vdate__range=[fromdate, todate],company=company)
            
        totindexpense = expense.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
        ledcodeemp=Tblaccountledger.objects.filter(agroupid=22).values_list('lid', flat=True)
        employee = Tblgeneralledger.objects.filter(ledcode__in=ledcodeemp,vdate__range=[fromdate, todate],company=company)
            
        employeexpense = employee.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
    else:
        if curuser=='HEAD OFFICE' and chkarea=='no':
            if chkuser=='all':
                print("Type2")

               
               
               
                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,area=area)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,area=area)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,area=area)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,area=area)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,area=area)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                rec = Tblbatch.objects.filter(company=company)
            
                costrate = rec.aggregate(costrate=Sum('crate',default=0))['costrate']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area)
            
                salegross= sale.aggregate(salegross=Sum('amt',default=0)-Sum('taxamt',default=0))['salegross']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area)
            
                prgross= pr.aggregate(prgross=Sum('amt',default=0)-Sum('taxamt',default=0))['prgross']
                pi = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area)
            
                pigross = pi.aggregate(pigross=Sum('amt',default=0)-Sum('taxamt',default=0))['pigross']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area)
            
                srgross = sr.aggregate(srgross=Sum('amt',default=0)-Sum('taxamt',default=0))['srgross']
                 
                grossprofit=float( salegross+prgross)-float(pigross+srgross)
                ledcodeincome=Tblaccountledger.objects.filter(agroupid=16).values_list('lid', flat=True)
                income = Tblgeneralledger.objects.filter(ledcode__in=ledcodeincome,vdate__range=[fromdate, todate],company=company,area=area)
                    
                totindincome = income.aggregate(totindincome=Sum('cramt',default=0))['totindincome']
                ledcodeexp=Tblaccountledger.objects.filter(agroupid=15).values_list('lid', flat=True)
                expense = Tblgeneralledger.objects.filter(ledcode__in=ledcodeexp,vdate__range=[fromdate, todate],company=company,area=area)
                    
                totindexpense = expense.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
                ledcodeemp=Tblaccountledger.objects.filter(agroupid=22).values_list('lid', flat=True)
                employee = Tblgeneralledger.objects.filter(ledcode__in=ledcodeemp,vdate__range=[fromdate, todate],company=company,area=area)
                    
                employeexpense = employee.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']


                




            else:
                print("Type3")

                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area,uid=user)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,area=area,uid=user)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,area=area,uid=user)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area,uid=user).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area,uid=user)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,area=area,uid=user)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,area=area,uid=user)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company,area=area,uid=user).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area,uid=user)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area,uid=user).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area,uid=user)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,area=area,uid=user)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                rec = Tblbatch.objects.filter(company=company)
            
                costrate = rec.aggregate(costrate=Sum('crate',default=0))['costrate']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area,uid=user)
            
                salegross= sale.aggregate(salegross=Sum('amt',default=0)-Sum('taxamt',default=0))['salegross']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area,uid=user)
            
                prgross= pr.aggregate(prgross=Sum('amt',default=0)-Sum('taxamt',default=0))['prgross']
                pi = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area,uid=user)
            
                pigross = pi.aggregate(pigross=Sum('amt',default=0)-Sum('taxamt',default=0))['pigross']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area,uid=user)
            
                srgross = sr.aggregate(srgross=Sum('amt',default=0)-Sum('taxamt',default=0))['srgross']
                grossprofit=float( salegross+prgross)-float(pigross+srgross)
                ledcodeincome=Tblaccountledger.objects.filter(agroupid=16).values_list('lid', flat=True)
                income = Tblgeneralledger.objects.filter(ledcode__in=ledcodeincome,vdate__range=[fromdate, todate],company=company,area=area,uid=user)
                    
                totindincome = income.aggregate(totindincome=Sum('cramt',default=0))['totindincome']
                ledcodeexp=Tblaccountledger.objects.filter(agroupid=15).values_list('lid', flat=True)
                expense = Tblgeneralledger.objects.filter(ledcode__in=ledcodeexp,vdate__range=[fromdate, todate],company=company,area=area,uid=user)
                    
                totindexpense = expense.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
                ledcodeemp=Tblaccountledger.objects.filter(agroupid=22).values_list('lid', flat=True)
                employee = Tblgeneralledger.objects.filter(ledcode__in=ledcodeemp,vdate__range=[fromdate, todate],company=company,area=area,uid=user)
                    
                employeexpense = employee.aggregate(totindexpense=(Sum('dbamt',default=0)-Sum('cramt',default=0)))['totindexpense']
    
        else:
            if chkuser=='all':

                print("Type4")
                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,area=area)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,area=area)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,area=area)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,area=area)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,area=area)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                rec = Tblbatch.objects.filter(company=company)
            
                costrate = rec.aggregate(costrate=Sum('crate',default=0))['costrate']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area)
            
                salegross= sale.aggregate(salegross=Sum('amt',default=0)-Sum('taxamt',default=0))['salegross']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area)
            
                prgross= pr.aggregate(prgross=Sum('amt',default=0)-Sum('taxamt',default=0))['prgross']
                pi = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area)
            
                pigross = pi.aggregate(pigross=Sum('amt',default=0)-Sum('taxamt',default=0))['pigross']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area)
            
                srgross = sr.aggregate(srgross=Sum('amt',default=0)-Sum('taxamt',default=0))['srgross']
                grossprofit=float( salegross+prgross)-float(pigross+srgross)
                ledcodeincome=Tblaccountledger.objects.filter(agroupid=16).values_list('lid', flat=True)
                income = Tblgeneralledger.objects.filter(ledcode__in=ledcodeincome,vdate__range=[fromdate, todate],company=company,area=area)
                    
                totindincome = income.aggregate(totindincome=Sum('cramt',default=0))['totindincome']
                ledcodeexp=Tblaccountledger.objects.filter(agroupid=15).values_list('lid', flat=True)
                expense = Tblgeneralledger.objects.filter(ledcode__in=ledcodeexp,vdate__range=[fromdate, todate],company=company,area=area)
                    
                totindexpense = expense.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
                ledcodeemp=Tblaccountledger.objects.filter(agroupid=22).values_list('lid', flat=True)
                employee = Tblgeneralledger.objects.filter(ledcode__in=ledcodeemp,vdate__range=[fromdate, todate],company=company,area=area)
                    
                employeexpense = employee.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
                
        
                




            else:
                
               
                fromdate  = request.GET.get('fromdt')
                todate= request.GET.get('todt')
                cash = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='1',company=company,area=area,uid=user)
            
                openingcash = cash.aggregate(openingcash=Sum('dbamt',default=0))['openingcash']
                Bank = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='OB',ledcode='28',company=company,area=area,uid=user)
            
                openingbank = Bank.aggregate(openingbank=Sum('dbamt',default=0))['openingbank']
                
                cashpurchase = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',ledcodecr=1, company=company,area=area,uid=user)
            
                totalcashpurchase = cashpurchase.aggregate(totalpurachase=Sum('amt',default=0))['totalpurachase']
                
                prwithoutcr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area,uid=user).exclude(ledcodecr__gt=30)
            
                totalprwithoutcr = prwithoutcr.aggregate(totalprwithoutcr=Sum('amt',default=0))['totalprwithoutcr']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area,uid=user)
            
                totalsale = sale.aggregate(totalsale=Sum('amt',default=0))['totalsale']
                salecard = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=28, company=company,area=area,uid=user)
            
                totalsalecard = salecard.aggregate(totalsalecard=Sum('amt',default=0))['totalsalecard']
                salecash = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',ledcodedr=1, company=company,area=area,uid=user)
            
                totalsalecash = salecash.aggregate(totalsalecash=Sum('amt',default=0))['totalsalecash']
                salecredit = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI', company=company,area=area,uid=user).exclude(ledcodedr='1').exclude(ledcodedr='28')
            
                totalsalecredit = salecredit.aggregate(totalsalecredit=Sum('amt',default=0))['totalsalecredit']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area,uid=user)
            
                totalsr = sr.aggregate(totalsr=Sum('amt',default=0))['totalsr']
                srcredit = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area,uid=user).exclude(ledcodecr='1').exclude(ledcodecr='28')
            
                totalsrcredit = srcredit.aggregate(totalsrcredit=Sum('amt',default=0))['totalsrcredit']
                


                pay = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='P',company=company,area=area,uid=user)
            
                payment = pay.aggregate(payment=Sum('cramt',default=0))['payment']
                rec = Tblgeneralledger.objects.filter(vdate__range=[fromdate, todate],vtype='R',company=company,area=area,uid=user)
            
                receipt = rec.aggregate(receipt=Sum('cramt',default=0))['receipt']
                rec = Tblbatch.objects.filter(company=company)
            
                costrate = rec.aggregate(costrate=Sum('crate',default=0))['costrate']
                sale = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='SI',company=company,area=area,uid=user)
            
                salegross= sale.aggregate(salegross=Sum('amt',default=0)-Sum('taxamt',default=0))['salegross']
                pr = Tblbusinessissue.objects.filter(issuedate__range=[fromdate, todate],issuetype='PR',company=company,area=area,uid=user)
            
                prgross= pr.aggregate(prgross=Sum('amt',default=0)-Sum('taxamt',default=0))['prgross']
                pi = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='PI',company=company,area=area,uid=user)
            
                pigross = pi.aggregate(pigross=Sum('amt',default=0)-Sum('taxamt',default=0))['pigross']
                sr = TblTransactionReceipt.objects.filter(recptdate__range=[fromdate, todate],recpttype='SR',company=company,area=area,uid=user)
            
                srgross = sr.aggregate(srgross=Sum('amt',default=0)-Sum('taxamt',default=0))['srgross']
                grossprofit=float( salegross+prgross)-float(pigross+srgross)
                ledcodeincome=Tblaccountledger.objects.filter(agroupid=16).values_list('lid', flat=True)
                income = Tblgeneralledger.objects.filter(ledcode__in=ledcodeincome,vdate__range=[fromdate, todate],company=company,area=area,uid=user)
                    
                totindincome = income.aggregate(totindincome=Sum('cramt',default=0))['totindincome']
                ledcodeexp=Tblaccountledger.objects.filter(agroupid=15).values_list('lid', flat=True)
                expense = Tblgeneralledger.objects.filter(ledcode__in=ledcodeexp,vdate__range=[fromdate, todate],company=company,area=area,uid=user)
                    
                totindexpense = expense.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
                ledcodeemp=Tblaccountledger.objects.filter(agroupid=22).values_list('lid', flat=True)
                employee = Tblgeneralledger.objects.filter(ledcode__in=ledcodeemp,vdate__range=[fromdate, todate],company=company,area=area,uid=user)
                    
                employeexpense = employee.aggregate(totindexpense=Sum('dbamt')-Sum('cramt'))['totindexpense']
    


               
           
    
    
    data = [{'opcash': openingcash, 'opbank': openingbank,'totcashpurchase':totalcashpurchase,
    'totsale':totalsale,'totsalecard':totalsalecard,'totsalecash':totalsalecash,
    'totsalecredit':totalsalecredit,'totsr':totalsr,'totsrcredit':totalsrcredit,'payment':payment,
    'receipt':receipt,'totalprwithoutcr':totalprwithoutcr,'crate':costrate,'grossprofit':grossprofit,
    'indirectincome':totindincome,'indirectexpense':totindexpense,'employeeexpense':employeexpense} ]
    
    return JsonResponse({'reportdata': data})

@login_required(login_url='login')  
def ledgergroupreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'ledgergrpreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})
def ledgergrpget(request):

    company = request.GET.get('comp')
    typechk = request.GET.get('type')
    agroup = request.GET.get('agrp','')
    

            # Split the string by commas to create a list of strings
    number_list = agroup.split(',')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    fromdate  = request.GET.get('fromdt')
    todate= request.GET.get('todt')
  
    if chkarea=='all':
        if typechk=='all':
            
            results = Tblaccountledger.objects.filter(agroupid__in=['18','19','22'],
                company=company,
                tblgeneralledger__vdate__range=[fromdate, todate]
            ).annotate(
                tdbamt=Sum('tblgeneralledger__dbamt'),
                tcramt=Sum('tblgeneralledger__cramt'),
                tledcode=F('lid')
            )
            data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]

        else:
            
            
            results = Tblaccountledger.objects.filter(agroupid__in=number_list,
                    company=company,
                    tblgeneralledger__vdate__range=[fromdate, todate]
                ).annotate(
                    tdbamt=Sum('tblgeneralledger__dbamt'),
                    tcramt=Sum('tblgeneralledger__cramt'),
                    tledcode=F('lid')
                )           
            
                
           
            data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]
        
            
    else:
        if curuser=='HEAD OFFICE' and chkarea=='no':
            if chkuser=='all':
                if typechk=='all':

            
                    results = Tblaccountledger.objects.filter(agroupid__in=['18','19','22'],
                        company=company,tblgeneralledger__area=area,
                        tblgeneralledger__vdate__range=[fromdate, todate]
                    ).annotate(
                        tdbamt=Sum('tblgeneralledger__dbamt'),
                        tcramt=Sum('tblgeneralledger__cramt'),
                        tledcode=F('lid')
                    )
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]

                else:
                    
                    
                    results = Tblaccountledger.objects.filter(agroupid__in=number_list,
                            company=company,tblgeneralledger__area=area,
                            tblgeneralledger__vdate__range=[fromdate, todate]
                        ).annotate(
                            tdbamt=Sum('tblgeneralledger__dbamt'),
                            tcramt=Sum('tblgeneralledger__cramt'),
                            tledcode=F('lid')
                        )           
                    
                        
                
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]
                
                
         



            else:
                if typechk=='all':

            
                    results = Tblaccountledger.objects.filter(agroupid__in=['18','19','22'],
                        company=company,tblgeneralledger__area=area,tblgeneralledger__uid=user,
                        tblgeneralledger__vdate__range=[fromdate, todate]
                    ).annotate(
                        tdbamt=Sum('tblgeneralledger__dbamt'),
                        tcramt=Sum('tblgeneralledger__cramt'),
                        tledcode=F('lid')
                    )
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]

                else:
                    
                    
                    results = Tblaccountledger.objects.filter(agroupid__in=number_list,
                            company=company,tblgeneralledger__area=area,tblgeneralledger__uid=user,
                            tblgeneralledger__vdate__range=[fromdate, todate]
                        ).annotate(
                            tdbamt=Sum('tblgeneralledger__dbamt'),
                            tcramt=Sum('tblgeneralledger__cramt'),
                            tledcode=F('lid')
                        )           
                    
                        
                
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]
                
               
                
    
        else:
            if chkuser=='all':

                if typechk=='all':

            
                    results = Tblaccountledger.objects.filter(agroupid__in=['18','19','22'],
                        company=company,tblgeneralledger__area=area,
                        tblgeneralledger__vdate__range=[fromdate, todate]
                    ).annotate(
                        tdbamt=Sum('tblgeneralledger__dbamt'),
                        tcramt=Sum('tblgeneralledger__cramt'),
                        tledcode=F('lid')
                    )
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]

                else:
                    
                    
                    results = Tblaccountledger.objects.filter(agroupid__in=number_list,
                            company=company,tblgeneralledger__area=area,
                            tblgeneralledger__vdate__range=[fromdate, todate]
                        ).annotate(
                            tdbamt=Sum('tblgeneralledger__dbamt'),
                            tcramt=Sum('tblgeneralledger__cramt'),
                            tledcode=F('lid')
                        )           
                    
                        
                
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]
                

            else:
                if typechk=='all':

            
                    results = Tblaccountledger.objects.filter(agroupid__in=['18','19','22'],
                        company=company,tblgeneralledger__area=area,tblgeneralledger__uid=user,
                        tblgeneralledger__vdate__range=[fromdate, todate]
                    ).annotate(
                        tdbamt=Sum('tblgeneralledger__dbamt'),
                        tcramt=Sum('tblgeneralledger__cramt'),
                        tledcode=F('lid')
                    )
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]

                else:
                    
                    
                    results = Tblaccountledger.objects.filter(agroupid__in=number_list,
                            company=company,tblgeneralledger__area=area,tblgeneralledger__uid=user,
                            tblgeneralledger__vdate__range=[fromdate, todate]
                        ).annotate(
                            tdbamt=Sum('tblgeneralledger__dbamt'),
                            tcramt=Sum('tblgeneralledger__cramt'),
                            tledcode=F('lid')
                        )           
                    
                        
                
                    data = [{'ledcode': result.tledcode,'dbamt':result.tdbamt,'cramt':result.tcramt} for result in results ]
                
                
    
    
    
    return JsonResponse({'reportdata': data})
@login_required(login_url='login')  
def saletaxreport(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    
    us=Tbldepot.objects.filter(company=company)
    today = datetime.datetime.now()
    fromdate = today.strftime("%Y-%m-%dT%H:%M")
    tomorrow=today+timedelta(1)
    todate=tomorrow.strftime("%Y-%m-%dT%H:%M")
    return render(request,'salestaxreport.html',{'fromdate':fromdate,'todate':todate,'us':us,'company':company,'area':area,'cuser':user,'user':company})

def salestaxreportget(request):
    vtype=request.GET.get('vtype')
    company = request.GET.get('comp')
    
    curuser=request.GET.get('curarea')
    chkuser = request.GET.get('chkuser')
    chkarea = request.GET.get('chkarea')
    user = request.GET.get('user')
    area = request.GET.get('area')
    fromdate  = request.GET.get('fromdt')
    todate= request.GET.get('todt')
    if vtype=='SI' or vtype == 'SO' or vtype == 'SS':

        if chkarea=='all':
                transactions = Tblbusinessissue.objects.filter(
                    issuedate__gte=fromdate,
                    issuedate__lte=todate,
                    issuetype='SI',
                    company=company
                    ).order_by(F('vno').asc())  
                transaction_data = []
                
                for txn in transactions:
                    onepercent_tax=0
                    fifteenpercent_tax=0
                    twentypercent_tax=0

                   
                    itemids=Tblissuedetails.objects.filter(company=company,issuecode=txn.vno,vtype='SI')
                    for tax in itemids:
                            if(float( tax.taxper)==1):
                                    
                                    onepercent_tax=float(tax.taxrate) +onepercent_tax
                            if(float( tax.taxper)==15):
                                    
                                    fifteenpercent_tax=float(tax.taxrate)+fifteenpercent_tax
                            if(float( tax.taxper)==20):
                                    
                                    twentypercent_tax=float(tax.taxrate)+twentypercent_tax

                    transaction_data.append({
                        'clndate': txn.issuedate.strftime('%d/%m/%Y'),
                        'clnvno': f"{txn.vno}{txn.pvno if txn.pvno else ''}",
                        'clnparty': txn.ledcodedr,
                        'tottax': txn.taxamt,
                        'onetx': onepercent_tax,
                        'fifteentx': fifteenpercent_tax,
                        'twentytx': twentypercent_tax,
                        'netamt':txn.amt,
                        'grossamt':float(txn.amt-txn.taxamt),
                    })
                data = transaction_data

        
        else:
            if curuser=='HEAD OFFICE' and chkarea=='no':
                if chkuser=='all':
                    transactions = Tblbusinessissue.objects.filter(
                    issuedate__gte=fromdate,
                    issuedate__lte=todate,
                    issuetype='SI',area=area,
                    company=company
                    ).order_by(F('vno').asc())  
                    transaction_data = []
                
                    for txn in transactions:

                        onepercent_tax=0
                        fifteenpercent_tax=0
                        twentypercent_tax=0

                    
                        itemids=Tblissuedetails.objects.filter(company=company,issuecode=txn.vno,vtype='SI')
                        for tax in itemids:
                                if(float( tax.taxper)==1):
                                        
                                        onepercent_tax=float(tax.taxrate) +onepercent_tax
                                if(float( tax.taxper)==15):
                                        
                                        fifteenpercent_tax=float(tax.taxrate)+fifteenpercent_tax
                                if(float( tax.taxper)==20):
                                        
                                        twentypercent_tax=float(tax.taxrate)+twentypercent_tax

                        transaction_data.append({
                            'clndate': txn.issuedate.strftime('%d/%m/%Y'),
                            'clnvno': f"{txn.vno}{txn.pvno if txn.pvno else ''}",
                            'clnparty': txn.ledcodedr,
                            'tottax': txn.taxamt,
                            'onetx': onepercent_tax,
                            'fifteentx': fifteenpercent_tax,
                            'twentytx': twentypercent_tax,
                            'netamt':txn.amt,
                            'grossamt':float(txn.amt-txn.taxamt),
                        })
                    data = transaction_data



                else:
                    transactions = Tblbusinessissue.objects.filter(
                    issuedate__gte=fromdate,
                    issuedate__lte=todate,area=area,uid=user,
                    issuetype='SI',
                    company=company
                    ).order_by(F('vno').asc())  
                    transaction_data = []
                    
                    for txn in transactions:
                        onepercent_tax=0
                        fifteenpercent_tax=0
                        twentypercent_tax=0

                    
                        itemids=Tblissuedetails.objects.filter(company=company,issuecode=txn.vno,vtype='SI')
                        for tax in itemids:
                                if(float( tax.taxper)==1):
                                        
                                        onepercent_tax=float(tax.taxrate) +onepercent_tax
                                if(float( tax.taxper)==15):
                                        
                                        fifteenpercent_tax=float(tax.taxrate)+fifteenpercent_tax
                                if(float( tax.taxper)==20):
                                        
                                        twentypercent_tax=float(tax.taxrate)+twentypercent_tax

                        transaction_data.append({
                            'clndate': txn.issuedate.strftime('%d/%m/%Y'),
                            'clnvno': f"{txn.vno}{txn.pvno if txn.pvno else ''}",
                            'clnparty': txn.ledcodedr,
                            'tottax': txn.taxamt,
                            'onetx': onepercent_tax,
                            'fifteentx': fifteenpercent_tax,
                            'twentytx': twentypercent_tax,
                            'netamt':txn.amt,
                            'grossamt':float(txn.amt-txn.taxamt),
                        })
                    data = transaction_data
        
            else:
                if chkuser=='all':

                    transactions = Tblbusinessissue.objects.filter(
                    issuedate__gte=fromdate,
                    issuedate__lte=todate,area=area,
                    issuetype='SI',
                    company=company
                    ).order_by(F('vno').asc())  
                    transaction_data = []
                    
                    for txn in transactions:
                        onepercent_tax=0
                        fifteenpercent_tax=0
                        twentypercent_tax=0

                    
                        itemids=Tblissuedetails.objects.filter(company=company,issuecode=txn.vno,vtype='SI')
                        for tax in itemids:
                                if(float( tax.taxper)==1):
                                        
                                        onepercent_tax=float(tax.taxrate) +onepercent_tax
                                if(float( tax.taxper)==15):
                                        
                                        fifteenpercent_tax=float(tax.taxrate)+fifteenpercent_tax
                                if(float( tax.taxper)==20):
                                        
                                        twentypercent_tax=float(tax.taxrate)+twentypercent_tax

                        transaction_data.append({
                            'clndate': txn.issuedate.strftime('%d/%m/%Y'),
                            'clnvno': f"{txn.vno}{txn.pvno if txn.pvno else ''}",
                            'clnparty': txn.ledcodedr,
                            'tottax': txn.taxamt,
                            'onetx': onepercent_tax,
                            'fifteentx': fifteenpercent_tax,
                            'twentytx': twentypercent_tax,
                            'netamt':txn.amt,
                            'grossamt':float(txn.amt-txn.taxamt),
                        })
                    data = transaction_data

                else:
                    transactions = Tblbusinessissue.objects.filter(
                    issuedate__gte=fromdate,
                    issuedate__lte=todate,area=area,uid=user,
                    issuetype='SI',
                    company=company
                    ).order_by(F('vno').asc())  
                    transaction_data = []
                    
                    for txn in transactions:
                        onepercent_tax=0
                        fifteenpercent_tax=0
                        twentypercent_tax=0

                    
                        itemids=Tblissuedetails.objects.filter(company=company,issuecode=txn.vno,vtype='SI')
                        for tax in itemids:
                                if(float( tax.taxper)==1):
                                        
                                        onepercent_tax=float(tax.taxrate) +onepercent_tax
                                if(float( tax.taxper)==15):
                                        
                                        fifteenpercent_tax=float(tax.taxrate)+fifteenpercent_tax
                                if(float( tax.taxper)==20):
                                        
                                        twentypercent_tax=float(tax.taxrate)+twentypercent_tax

                        transaction_data.append({
                            'clndate': txn.issuedate.strftime('%d/%m/%Y'),
                            'clnvno': f"{txn.vno}{txn.pvno if txn.pvno else ''}",
                            'clnparty': txn.ledcodedr,
                            'tottax': txn.taxamt,
                            'onetx': onepercent_tax,
                            'fifteentx': fifteenpercent_tax,
                            'twentytx': twentypercent_tax,
                            'netamt':txn.amt,
                            'grossamt':float(txn.amt-txn.taxamt),
                        })
                    data = transaction_data
        
                   
    else:
        if chkarea=='all':

                    transactions = Tblbusinessissue.objects.filter(
                    issuedate__gte=fromdate,
                    issuedate__lte=todate,
                    issuetype='SI',
                    company=company
                    ).order_by(F('vno').asc())  
                    transaction_data = []
                    
                    for txn in transactions:
                        onepercent_tax=0
                        fifteenpercent_tax=0
                        twentypercent_tax=0

                    
                        itemids=Tblissuedetails.objects.filter(company=company,issuecode=txn.vno,vtype='SI')
                        for tax in itemids:
                                if(float( tax.taxper)==1):
                                        
                                        onepercent_tax=float(tax.taxrate) +onepercent_tax
                                if(float( tax.taxper)==15):
                                        
                                        fifteenpercent_tax=float(tax.taxrate)+fifteenpercent_tax
                                if(float( tax.taxper)==20):
                                        
                                        twentypercent_tax=float(tax.taxrate)+twentypercent_tax

                        transaction_data.append({
                            'clndate': txn.issuedate.strftime('%d/%m/%Y'),
                            'clnvno': f"{txn.vno}{txn.pvno if txn.pvno else ''}",
                            'clnparty': txn.ledcodedr,
                            'tottax': txn.taxamt,
                            'onetx': onepercent_tax,
                            'fifteentx': fifteenpercent_tax,
                            'twentytx': twentypercent_tax,
                            'netamt':txn.amt,
                            'grossamt':float(txn.amt-txn.taxamt),
                        })
                    data = transaction_data
        
      
           
    return JsonResponse({'reportdata': data})

