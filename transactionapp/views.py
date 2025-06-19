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
from django.conf import settings
import os
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models.functions import Cast
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Q
from django.db.models import Q, Max
from django.db.models import Max, IntegerField, F
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from zshopapp.views import deletesales
from django.core.files import File
from django.templatetags.static import static

from io import BytesIO




@login_required(login_url='login')
    
def addsale(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
   
    tb = Tblbusinessissue.objects.filter(issuetype='SI',company=company)
    tball = Tblbusinessissue.objects.filter(issuetype='SI')
    if len(tball) == 0:
        issueid=1

    if len(tb) == 0:
        vno = 1
        
    else:
        vno=Tblbusinessissue.objects.filter(issuetype='SI',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1

    q=None
    
    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        customer = request.POST['customer']
        customerid = request.POST['customerid']
        
        paytype = request.POST['payment']
        invdate = request.POST['date']
        previous = request.POST['previous']
        

        taxtype = request.POST['taxtype']
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']

        discamount = request.POST['discountamt']
        discpercent = request.POST['discountperc']

        itemname = request.POST.getlist('itemname')
      
        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')

        itemid = request.POST.getlist('itemid')
        nowdatetime=invdate

        if discamount=='':
            discamount=0
        if discpercent=='':
            discpercent=0


        print(previous)
        if paytype == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif paytype == '28':
            
            ledcode = 28
            ledname = 'Bank'
        else:

            ledcode = customerid

            ledname = customer
        if previous == 'yes':

            deletesales(issuecodevno, 'SI','sales',company) 
        else:
            print(issuecodevno)
            if issuecodevno != '1':
                
                issuecodevno=Tblbusinessissue.objects.filter(issuetype='SI',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
            
        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        for i in range(itemrange):
            issuetempid=Tblissuedetails.objects.all()
            if len(issuetempid) == 0:
                issuetempid=0
            else:
                issuetempid=Tblissuedetails.objects.filter().aggregate(max=Max(Cast('issueid', IntegerField())))["max"]
            
            issueid=issuetempid + 1


            itemnamef = itemname[i]
            if itemnamef!='':
                
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
                issued = Tblissuedetails.objects.create(issuecode=issuecodevno,issueid=issueid, slno=i, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=vatf,
                                                    netamt=netamtf, ledcode=2, vtype='SI',company=company)
                issued.save()
                inventory = Tblinventory.objects.create(dcode=0, invdate=nowdatetime, pcode=itemidf, sales=qtyf,
                                                    vcode=issuecodevno, ledcode=2, batchcode=barcodef,company=company)
                inventory.save()
                nullchk=1
                finalqty=float( qtyf)+finalqty
            else:
                print("itemname",itemnamef)
        if nullchk==1:

             
            bissue = Tblbusinessissue.objects.create(opno=0,biid=issueid,qty=finalqty, issuecode=issuecodevno, vno=issuecodevno, issuedate=nowdatetime, issuetype='SI',
                                                    dcode=0, ledcodedr=ledcode, ledcodecr=2, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, taxid=taxtype, cashreceived=0,discamt=discamount,discperc=discpercent, 
                                                    tmobile=mob,company=company,uid=user,area=area,tblissuedetails=issued)
            bissue.save()

            if ledcode==1 or ledcode==28:
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
                

            else:
                
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
                
            
            genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SI', vno=issuecodevno, slno=1, ledcode=ledcode,
                                                    particulars='sales vno:' + str(ledcode), dbamt=totalamount, cramt=0,tblaccountledger=acled,
                                                    refno=2,
                                                    company=company,uid=user,area=area)
            genled.save()
        
            acled9=Tblaccountledger.objects.get(lidmain=9)
            genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SI', vno=issuecodevno, slno=1, ledcode=9,tblaccountledger=acled9,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=0, cramt=totaltax,
                                                    refno=2,
                                                    company=company,uid=user,area=area)
            genled2.save()
            
            acled2=Tblaccountledger.objects.get(lidmain=2)
            genled3 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SI', vno=issuecodevno, slno=1, ledcode=2,tblaccountledger=acled2,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=0,
                                                    cramt=totalamount,
                                                    refno=2,
                                                    company=company,uid=user,area=area)
            genled3.save()
            
        return redirect('/sale')









    
    return render(request,'sales.html',{'a':q,'vno':vno,'datecur':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})
@login_required(login_url='login')
def addpurchase(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")

    tr = TblTransactionReceipt.objects.filter(recpttype='PI',company=company)
    trall = TblTransactionReceipt.objects.filter(recpttype='PI')
    if len(trall) == 0:
        recptid=1

    if len(tr) == 0:
        vno = 1
        
    else:
        vno=TblTransactionReceipt.objects.filter(recpttype='PI',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    aa= None
    
    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        supplier = request.POST['customer']
        supplierid = request.POST['customerid']
        refno = request.POST['refno']
        paytype = request.POST['payment']
        invdate = request.POST['date']
        previous = request.POST['previous']
        taxtype = request.POST['taxtype']
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']
        uploaded_image = request.FILES.get('billimg', None)

        if not uploaded_image:  # If no image is uploaded, set a default image
            default_image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'noimage.jpg')
            
            # Open the default image and store its content in memory
            with open(default_image_path, 'rb') as default_image_file:
                default_image_content = default_image_file.read()
            
            # Use BytesIO to wrap the content and create a Django File object
            uploaded_image = File(BytesIO(default_image_content), name='noimage.jpg')

        discamount = request.POST['discountamt']
        discpercent = request.POST['discountperc']
        itemname = request.POST.getlist('itemname')

        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')
        
        itemid = request.POST.getlist('itemid')
        nowdatetime=invdate
        if discamount=='':
            discamount=0
        if discpercent=='':
            discpercent=0

        
        if paytype == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif paytype == '28':
            
            ledcode = 28
            ledname = 'Bank'
        else:

            ledcode = supplierid

            ledname = supplier
        if previous == 'yes':
            deletesales(issuecodevno,'PI','purchase',company)
        else:
            if issuecodevno != '1':
                    
                issuecodevno=TblTransactionReceipt.objects.filter(recpttype='PI',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1

        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        for i in range(itemrange):
            recpttempid=Tblreceiptdetails.objects.all()
            if len(recpttempid) ==0:
                recptid=1
            else:

                recptid=Tblreceiptdetails.objects.filter().aggregate(max=Max(Cast('rdid', IntegerField())))["max"] + 1
            print("recpid is",recptid)
            itemnamef = itemname[i]
            if itemnamef!='':
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
            
                rd = Tblreceiptdetails.objects.create(recptcode=issuecodevno,rdid=recptid, slno=i, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=vatf,
                                                    netamt=netamtf, ledcode=3, vtype='PI',company=company)
                rd.save()
                inventory = Tblinventory.objects.create(dcode=0, invdate=nowdatetime, pcode=itemidf, purchase=qtyf,
                                                    vcode=issuecodevno, ledcode=3, batchcode=barcodef,company=company)
                inventory.save()
                nullchk=1
                finalqty=float( qtyf)+finalqty
            
        if nullchk==1:

            tr = TblTransactionReceipt.objects.create(recptcode=issuecodevno,trid=recptid,qty=finalqty, vno=issuecodevno,refno=refno, recptdate=nowdatetime, recpttype='PI',
                                                    dcode=0, ledcodecr=ledcode, ledcodedr=3, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, taxid=taxtype,  mpayment=ledcode,uid=user,discamt=discamount,discperc=discpercent, 
                                                    tmobile=mob,company=company,area=area,recptdetails=rd,pbill=uploaded_image)
            tr.save()
            if ledcode==1 or ledcode==28:
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
                

            else:
                
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
            genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='PI', vno=issuecodevno, slno=1, ledcode=ledcode,tblaccountledger=acled,
                                                    particulars='Purchase vno:' + str(ledcode), dbamt=0, cramt=totalamount,
                                                    refno=3,company=company,
                                                    uid=user,area=area)
            genled.save()
            acled9=Tblaccountledger.objects.get(lidmain=8)
            genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='PI', vno=issuecodevno, slno=1, ledcode=9,tblaccountledger=acled9,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=totaltax, cramt=0,
                                                    refno=3,
                                                    uid=user,company=company,area=area)
            genled2.save()
            acled3=Tblaccountledger.objects.get(lidmain=3)
            genled3 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='PI', vno=issuecodevno, slno=1, ledcode=3,tblaccountledger=acled3,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=totalamount,
                                                    cramt=0,
                                                    refno=2,
                                                    uid=user,company=company,area=area)
            genled3.save()

        return redirect('/purchase')



    return render(request,'purchase.html',{'vno':vno,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})


@login_required(login_url='login')

def addsalereturn(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    tr = TblTransactionReceipt.objects.filter(recpttype='SR',company=company)
    if len(tr) == 0:
        vno = 1
    else:
        vno=TblTransactionReceipt.objects.filter(recpttype='SR',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
        
    
    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        supplier = request.POST['customer']
        supplierid = request.POST['customerid']
        
        paytype = request.POST['payment']
        invdate = request.POST['date']
        previous = request.POST['previous']
        taxtype = request.POST['taxtype']
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']

        discamount = request.POST['discountamt']
        discpercent = request.POST['discountperc']

        itemname = request.POST.getlist('itemname')

        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')
        
        itemid = request.POST.getlist('itemid')
        nowdatetime=invdate

        if discamount=='':
            discamount=0
        if discpercent=='':
            discpercent=0


        if paytype == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif paytype == '28':
            
            ledcode = 28
            ledname = 'Bank'
        else:

            ledcode = supplierid

            ledname = supplier
        if previous == 'yes':

            deletesales(issuecodevno,'SR','salereturn',company)

        else:
            if issuecodevno != '1':
                    
                issuecodevno=TblTransactionReceipt.objects.filter(recpttype='SR',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1

        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        
        for i in range(itemrange):
            recpttempid=Tblreceiptdetails.objects.all()
            if len(recpttempid) ==0:
                rdid=1
            else:
            
                rdid=Tblreceiptdetails.objects.filter().aggregate(max=Max(Cast('rdid', IntegerField())))["max"] + 1

            itemnamef = itemname[i]
            if itemnamef!='':
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
            
                rd = Tblreceiptdetails.objects.create(recptcode=issuecodevno,rdid=rdid, slno=i, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=vatf,
                                                    netamt=netamtf, ledcode=2, vtype='SR',company=company)
                rd.save()
                inventory = Tblinventory.objects.create(dcode=0, invdate=nowdatetime, pcode=itemidf, purchase=qtyf,
                                                    vcode=issuecodevno, ledcode=2, batchcode=barcodef,company=company)
                inventory.save()
                nullchk=1
                finalqty=float( qtyf)+finalqty

            
            
        if nullchk==1:

            tr = TblTransactionReceipt.objects.create(recptcode=issuecodevno,qty=finalqty,trid=rdid,recptdetails=rd, vno=issuecodevno, recptdate=nowdatetime, recpttype='SR',
                                                    dcode=0, ledcodecr=ledcode, ledcodedr=2, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, taxid=taxtype,  uid=user,mpayment=ledcode,discamt=discamount,discperc=discpercent, 
                                                    tmobile=mob,company=company,area=area)
            tr.save()
            if ledcode==1 or ledcode==28:
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
                

            else:
                
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
            genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SR', vno=issuecodevno, slno=1, ledcode=ledcode,tblaccountledger=acled,
                                                    particulars='Purchase vno:' + str(ledcode), dbamt=0, cramt=totalamount,
                                                    refno=2,uid=user,company=company,area=area)
            genled.save()
            acled9=Tblaccountledger.objects.get(lidmain=9)
            genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SR', vno=issuecodevno, slno=1, ledcode=9,tblaccountledger=acled9,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=totaltax, cramt=0,
                                                    refno=2,
                                                    uid=user,company=company,area=area)
            genled2.save()
            acled2=Tblaccountledger.objects.get(lidmain=2)
            genled3 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SR', vno=issuecodevno, slno=1, ledcode=17,tblaccountledger=acled2,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=totalamount,
                                                    cramt=0,
                                                    refno=2,
                                                    uid=user,company=company,area=area)
            genled3.save()
        

        return redirect('/salereturn')
    return render(request,'sr.html',{'vno':vno,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})
@login_required(login_url='login')
def addpurchasereturn(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    tb = Tblbusinessissue.objects.filter(issuetype='PR',company=company)
    
    if len(tb) == 0:
        vno = 1
        issueid=Tblbusinessissue.objects.filter().aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    else:
        vno=Tblbusinessissue.objects.filter(issuetype='PR',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
        

    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        customer = request.POST['customer']
        customerid = request.POST['customerid']
        refno = request.POST['refno']
        paytype = request.POST['payment']
        invdate = request.POST['date']
        previous = request.POST['previous']
        taxtype = request.POST['taxtype']
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']
        

        discamount = request.POST['discountamt']
        discpercent = request.POST['discountperc']

        itemname = request.POST.getlist('itemname')
        
        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')

        if discamount=='':
            discamount=0
        if discpercent=='':
            discpercent=0

        itemid = request.POST.getlist('itemid')

        nowdatetime=invdate
        if paytype == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif paytype == '28':
            
            ledcode = 28
            ledname = 'Bank'
        else:

            ledcode = customerid

            ledname = customer
        if previous == 'yes': 
            deletesales(issuecodevno, 'PR','purchasereturn',company)
        else:
            if issuecodevno != '1':
                issuecodevno=Tblbusinessissue.objects.filter(issuetype='PR',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1

        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        for i in range(itemrange):
            itemnamef = itemname[i]
            recpttempid=Tblbusinessissue.objects.all()
            if len(recpttempid) ==0:
                issueid=1
            else:
                issueid=Tblissuedetails.objects.filter().aggregate(max=Max(Cast('issueid', IntegerField())))["max"] + 1
            if itemnamef!='':
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
                issued = Tblissuedetails.objects.create(issuecode=issuecodevno,issueid=issueid, slno=i, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=15,
                                                    netamt=netamtf, ledcode=3, vtype='PR',company=company)
                issued.save()
                inventory = Tblinventory.objects.create(dcode=0, invdate=nowdatetime, pcode=itemidf, sales=qtyf,
                                                    vcode=issuecodevno, ledcode=3, batchcode=barcodef,company=company)
                inventory.save()
                nullchk=1
                finalqty=float( qtyf)+finalqty
                

        if nullchk==1:    
            bissue = Tblbusinessissue.objects.create(opno=0, issuecode=issuecodevno,refno=refno,qty=finalqty, biid=issueid,tblissuedetails=issued, vno=issuecodevno, issuedate=nowdatetime, issuetype='PR',
                                                    dcode=0, ledcodecr=ledcode, ledcodedr=3, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, taxid=taxtype, cashreceived=0, uid=user,discamt=discamount,discperc=discpercent, 
                                                    tmobile=mob,company=company,area=area)
            bissue.save()
            if ledcode==1 or ledcode==28:
                acled=Tblaccountledger.objects.get(lidmain=ledcode)
                

            else:
                
                acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
            genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='PR', vno=issuecodevno, slno=1, ledcode=ledcode,tblaccountledger=acled,
                                                    particulars='sales vno:' + str(ledcode), dbamt=totalamount, cramt=0,
                                                    refno=3,
                                                    uid=user,company=company,area=area)
            genled.save()
            acled9=Tblaccountledger.objects.get(lidmain=8)
            genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='PR', vno=issuecodevno, slno=1, ledcode=9,tblaccountledger=acled9,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=0, cramt=totaltax,
                                                    refno=3,
                                                    uid=user,company=company,area=area)
            genled2.save()
            acled3=Tblaccountledger.objects.get(lidmain=3)
            genled3 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='PR', vno=issuecodevno, slno=1, ledcode=18,tblaccountledger=acled3,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=0,
                                                    cramt=totalamount,
                                                    refno=3,
                                                    uid=user,company=company,area=area)
            genled3.save()
       
        return redirect('/purchasereturn')

    return render(request,'pr.html',{'vno':vno,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})
@login_required(login_url='login')
def addsaleorder(request):
    prevno = request.GET.get('prevno')
    type = request.GET.get('type')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")

    tb = Tblbusinessissue.objects.filter(issuetype='SO',company=company)
    if len(tb) == 0:
        vno = 1
    else:
        vno=Tblbusinessissue.objects.filter(issuetype='SO',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    q=None
    
    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        customer = request.POST['customer']
        customerid = request.POST['customerid']
        
        paytype = request.POST['payment']
        invdate = request.POST['date']
        
        

        taxtype = request.POST['taxtype']
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']

        itemname = request.POST.getlist('itemname')
      
        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')
        nowdatetime=invdate

        itemid = request.POST.getlist('itemid')

        print(invdate)
        if paytype == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif paytype == '28':
            
            ledcode = 28
            ledname = 'Bank'
        else:

            ledcode = customerid

            ledname = customer

        deletesales(issuecodevno, 'SO','salesorder',company) 
        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        for i in range(itemrange):
            issueidall=Tblreceiptdetails.objects.filter(company=company)
            if len(issueidall)==0:
                issueid=1
            else:
                issueid=Tblissuedetails.objects.filter().aggregate(max=Max(Cast('issueid', IntegerField())))["max"] + 1

            itemnamef = itemname[i]
            if itemnamef!='':
                
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
                issued = Tblissuedetails.objects.create(issuecode=issuecodevno, slno=i,issueid=issueid, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=15,
                                                    netamt=netamtf, ledcode=2, vtype='SO',company=company)
                issued.save()
                
                nullchk=1
                finalqty=float( qtyf)+finalqty
            else:
                print("itemname",itemnamef)
        if nullchk==1:

             
            bissue = Tblbusinessissue.objects.create(opno=0, issuecode=issuecodevno,qty=finalqty, vno=issuecodevno, issuedate=nowdatetime, issuetype='SO',
                                                    dcode=0, ledcodedr=ledcode, ledcodecr=2, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, taxid=taxtype, cashreceived=0, 
                                                    tmobile=mob,company=company,uid=user,area=area,tblissuedetails=issued)
            bissue.save()
            
            
          
            
        return redirect('/saleorder')










    return render(request,'salesorder.html',{'a':q,'vno':vno,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})
@login_required(login_url='login')
def addpurchaseorder(request):
    prevno = request.GET.get('prevno')
    type = request.GET.get('type')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")

    tr = TblTransactionReceipt.objects.filter(recpttype='PO',company=company)
    trall = TblTransactionReceipt.objects.filter(company=company)
    if len(tr) == 0 or len(trall)==0:
        vno = 1
    else:
        vno=TblTransactionReceipt.objects.filter(recpttype='PO',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
        
    
    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        supplier = request.POST['customer']
        supplierid = request.POST['customerid']
        
        paytype = request.POST['payment']
        invdate = request.POST['date']

        taxtype = request.POST['taxtype']
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']

        itemname = request.POST.getlist('itemname')

        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')
        
        itemid = request.POST.getlist('itemid')
        nowdatetime=invdate
        
        if paytype == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif paytype == '28':
            
            ledcode = 28
            ledname = 'Bank'
        else:

            ledcode = supplierid

            ledname = supplier

        deletesales(issuecodevno,'PO','purchaseorder',company)
        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        for i in range(itemrange):
            rdidall=Tblreceiptdetails.objects.filter(company=company)
            if len(rdidall)==0:
                rdid=1
            else:

                rdid=Tblreceiptdetails.objects.filter().aggregate(max=Max(Cast('rdid', IntegerField())))["max"] + 1

            itemnamef = itemname[i]
            if itemnamef!='':
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
            
                rd = Tblreceiptdetails.objects.create(recptcode=issuecodevno,rdid=rdid,slno=i, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=vatf,
                                                    netamt=netamtf, ledcode=3, vtype='PO',company=company)
                rd.save()
               
                nullchk=1
                finalqty=float( qtyf)+finalqty
            
        if nullchk==1:

            tr = TblTransactionReceipt.objects.create(recptcode=issuecodevno, vno=issuecodevno,qty=finalqty, recptdate=nowdatetime, recpttype='PO',
                                                    dcode=0, ledcodecr=ledcode, ledcodedr=3, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, taxid=taxtype,  mpayment=ledcode,uid=user,
                                                    tmobile=mob,company=company,area=area,recptdetails=rd)
            tr.save()
            
                
           

        return redirect('/purchaseorder')



    return render(request,'purchaseorder.html',{'vno':vno,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})

@login_required(login_url='login')

def addreceipt(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    


    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    gl = Tblgeneralledger.objects.filter(vtype='R',company=company)
    if len(gl) == 0:
        rid = 1
    else:
        rid=Tblgeneralledger.objects.filter(vtype='R',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    
    if request.method == 'POST':
       
        ledvno = request.POST['invoice-number']
        
        
        ledger = request.POST['payment']
        invdate = request.POST['date']

        
        
        totalamount = request.POST['amttotal']
        discount = request.POST['amttotal']

        ledgername = request.POST.getlist('ledname')
        note = request.POST.getlist('note')

        ledid = request.POST.getlist('ledid')
        taxperc = request.POST.getlist('taxperc')
       
        taxamt = request.POST.getlist('taxamt')
        amt = request.POST.getlist('amt')
        
        nowdatetime=invdate
        
        
        
        if ledger == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif ledger == '28':
            
            ledcode = 28
            ledname = 'Bank'
        

        delinv = Tblgeneralledger.objects.filter(vno=ledvno,vtype='R',company=company)
        delinv.delete()
        nullchk=0
        itemrange = len(ledgername)
        print(ledid)
        for i in range(itemrange):
            lednamf = ledgername[i]
            print(lednamf)
            if lednamf!='':
                notef = note[i]
                taxpercf = taxperc[i]
                taxamtf = taxamt[i]
                amtf = amt[i]
                ledidf = ledid[i]
                if taxpercf=='' or taxpercf==None:

                    taxpercf=0
                if taxamtf=='' or taxamtf==None:
                    taxamtf=0
            
                if int(ledidf) >=30:
                    acled=Tblaccountledger.objects.get(lid=ledidf,company=company)
                else:
                    acled=Tblaccountledger.objects.get(lidmain=ledidf)


            


            
                genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='R', vno=ledvno, slno=1, ledcode=ledidf, tblaccountledger=acled,
                                                  particulars=ledname + 'R', dbamt=0, cramt=amtf,rptaxperc=taxpercf,rptaxamt=taxamtf,
                                                  naration2=notef,
                                                  uid=user,company=company,area=area)
                genled.save()
                nullchk=1

        if nullchk==1:

            acled2=Tblaccountledger.objects.get(lidmain=ledger)
            genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='R', vno=ledvno, slno=1, ledcode=ledger,
                                                    particulars=ledname + 'R', dbamt=totalamount, cramt=0,tblaccountledger=acled2,
                                                    
                                                    uid=user,company=company,area=area)
            genled2.save()
                
            
        
        return redirect('/receipt')
    print("prevvno",prevno)
    return render(request,'Receipt.html',{'rid':rid,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})
@login_required(login_url='login')
def addpayment(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    gl = Tblgeneralledger.objects.filter(vtype='P',company=company)
    if len(gl) == 0:
        rid = 1
    else:
        rid=Tblgeneralledger.objects.filter(vtype='P',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    
    
    if request.method == 'POST':
        
        ledvno = request.POST['invoice-number']
        
        
        ledger = request.POST['payment']
        invdate = request.POST['date']

        
        
        totalamount = request.POST['amttotal']
        discount = request.POST['amttotal']

        ledgername = request.POST.getlist('ledname')
        note = request.POST.getlist('note')

        ledid = request.POST.getlist('ledid')
        taxperc = request.POST.getlist('taxperc')
  
        taxamt = request.POST.getlist('taxamt')
        amt = request.POST.getlist('amt')

        nowdatetime=invdate
        if taxperc=='' or taxperc==None:
            taxperc=0
        if taxamt=='' or taxamt==None:
            taxamt=0
        
       
        

        
        if ledger == '1':
            
            ledcode = 1
            ledname = 'Cash'
        elif ledger == '28':
            
            ledcode = 28
            ledname = 'Bank'
        

        delinv = Tblgeneralledger.objects.filter(vno=ledvno,vtype='P',company=company)
        delinv.delete()
        itemrange = len(ledgername)
        nullchk=0
        for i in range(itemrange):
            lednamf = ledgername[i]
            if lednamf!='':
                notef = note[i]
                taxpercf = taxperc[i]
                taxamtf = taxamt[i]
                amtf = amt[i]
                ledidf = ledid[i]
                if taxpercf=='' or taxpercf==None:
                    taxpercf=0
                if taxamtf=='' or taxamtf==None:
                    taxamtf=0
            
                if int(ledidf) >=30:
                    acled=Tblaccountledger.objects.get(lid=ledidf,company=company)
                else:
                    acled=Tblaccountledger.objects.get(lidmain=ledidf)
                genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='P', vno=ledvno, slno=1, ledcode=ledidf,tblaccountledger=acled,
                                                  particulars=ledname + 'P', dbamt=amtf, cramt=0,rptaxperc=taxpercf,rptaxamt=taxamtf,
                                                  
                                                  uid=user,company=company,area=area)
                genled2.save()
                nullchk=1

        if nullchk==1:

            acled2=Tblaccountledger.objects.get(lidmain=ledger)    
            genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='P', vno=ledvno, slno=1, ledcode=ledger,tblaccountledger=acled2, 
                                                    particulars=ledname + 'P', dbamt=0, cramt=totalamount,
                                                    naration2=notef,
                                                    uid=user,company=company,area=area)
            genled.save()
            
            
        return redirect('/payment')
    print("prevvno",prevno)
    return render(request,'Payment.html',{'rid':rid,'date':curtime,'user':company,'cuser':user,'area':area,'type':type,'prevno':prevno})
    



@login_required(login_url='login')
def service(request):
    type = request.GET.get('type')
    prevno = request.GET.get('prevno')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    
    tb = Tblbusinessissue.objects.filter(issuetype='SS',company=company)
    tball = Tblbusinessissue.objects.filter(issuetype='SS')
    if len(tball) == 0:
        issueid=1

    if len(tb) == 0:
        vno = 1
        
    else:
        vno=Tblbusinessissue.objects.filter(issuetype='SS',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1

    q=None
    
    if request.method == 'POST':
        issuecodevno = request.POST['invoice-number']
        customer = request.POST['customer']
        customerid = request.POST['customerid']
        
       
        invdate = request.POST['date']
        previous = request.POST['previous']
        apdate = request.POST['apdate']
        battery = request.POST.get('battery', -1)
        facecover=request.POST.get('facecover', -1)
        
        backcover = request.POST.get('backcover', -1)
        mmc = request.POST.get('mmc', -1)
        
        sim = request.POST.get('sim', -1)
        charger = request.POST.get('charger', -1)
        knwork = request.POST.get('knwork', -1)
        nsignal = request.POST.get('nsignal', -1)
        mnwork = request.POST.get('mnwork', -1)
        snwork = request.POST.get('snwork', -1)
        ncharg = request.POST.get('ncharg', -1)
        cnwork = request.POST.get('cnwork', -1)
        knwork = request.POST.get('knwork', -1)
        npower = request.POST.get('npower', -1)
        fnwork = request.POST.get('fnwork', -1)
        lcd = request.POST.get('lcd', -1)
        password = request.POST['pass']
        imei = request.POST['imei']
       

       
        mob = request.POST['mobile']
        totalgross = request.POST['totalgross']
        totalamount = request.POST['totalnet']
        totaltax = request.POST['totaltax']

        itemname = request.POST.getlist('itemname')
      
        barcode = request.POST.getlist('barcode')
        ilang = request.POST.getlist('ilang')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        amount = request.POST.getlist('amt')
        tax = request.POST.getlist('tax')
        netamount = request.POST.getlist('netamt')
        vat = request.POST.getlist('vat')
        
        itemid = request.POST.getlist('itemid')

        
        ledcode = customerid

        ledname = customer
        apdatetime=apdate
        nowdatetime=invdate
        print(apdatetime)
        if previous == 'yes':

            deletesales(issuecodevno, 'SS','sales',company) 
        else:
            
            if issuecodevno != '1':
                
                issuecodevno=Tblbusinessissue.objects.filter(issuetype='SS',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
            
        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        for i in range(itemrange):
            issuetempid=Tblissuedetails.objects.all()
            if len(issuetempid) == 0:
                issuetempid=0
            else:
                issuetempid=Tblissuedetails.objects.filter().aggregate(max=Max(Cast('issueid', IntegerField())))["max"]
            
            issueid=issuetempid + 1


            itemnamef = itemname[i]
            if itemnamef!='':
                
                barcodef = barcode[i]
                ilangf = ilang[i]
                sratef = srate[i]
                qtyf = qty[i]
                amountf = amount[i]
                taxf = tax[i]
                netamtf = netamount[i]
                itemidf = itemid[i]
                vatf = vat[i]
                issued = Tblissuedetails.objects.create(issuecode=issuecodevno,issueid=issueid, slno=i, pcode=itemidf, batchid=barcodef,
                                                    qty=qtyf, rate=sratef, taxrate=taxf, taxper=15,
                                                    netamt=netamtf, ledcode=2, vtype='SS',company=company)
                issued.save()
                # inventory = Tblinventory.objects.create(dcode=0, invdate=invdate, pcode=itemidf, sales=qtyf,
                #                                     vcode=issuecodevno, ledcode=2, batchcode=barcodef,company=company)
                # inventory.save()
                nullchk=1
                finalqty=float( qtyf)+finalqty
            else:
                print("itemname",itemnamef)
        if nullchk==1:
             
            bissue = Tblbusinessissue.objects.create(opno=0,biid=issueid,qty=finalqty, issuecode=issuecodevno, vno=issuecodevno, issuedate=nowdatetime, issuetype='SS',
                                                    dcode=0, ledcodedr=ledcode, ledcodecr=2, amt=totalamount, remarks='',
                                                    empid=0, taxamt=totaltax, cashreceived=0, 
                                                    tmobile=mob,company=company,uid=user,area=area,tblissuedetails=issued)
            bissue.save()
           
            cdetail=Tblcomplaintdetails.objects.create(vno=issuecodevno,facecover=facecover,backcover=backcover,battery=battery,
                                                       mmc=mmc,sim=sim,charger=charger,nsignal=nsignal,ncharge=ncharg,npower=npower,
                                                       mnt=mnwork,fnt=fnwork,cnt=cnwork,snt=snwork,keypadnt=knwork,lcdprob=lcd,
                                                       password=password,imei=imei,addate=apdatetime,company=company)
            cdetail.save()
            acled=Tblaccountledger.objects.get(lid=ledcode,company=company)
                
            
            genled = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SS', vno=issuecodevno, slno=1, ledcode=ledcode,
                                                    particulars='sales vno:' + str(ledcode), dbamt=totalamount, cramt=0,tblaccountledger=acled,
                                                    refno=2,
                                                    company=company,uid=user,area=area)
            genled.save()
        
            acled9=Tblaccountledger.objects.get(lidmain=9)
            genled2 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SS', vno=issuecodevno, slno=1, ledcode=9,tblaccountledger=acled9,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=0, cramt=totaltax,
                                                    refno=2,
                                                    company=company,uid=user,area=area)
            genled2.save()
            
            acled2=Tblaccountledger.objects.get(lidmain=2)
            genled3 = Tblgeneralledger.objects.create(vdate=nowdatetime, vtype='SS', vno=issuecodevno, slno=1, ledcode=2,tblaccountledger=acled2,
                                                    particulars=ledname + ' vno:' + str(ledcode), dbamt=0,
                                                    cramt=totalamount,
                                                    refno=2,
                                                    company=company,uid=user,area=area)
            genled3.save()
            
        return redirect('/service')




    return render(request,'mobileservice.html',{'user':company,'cuser':user,'area':area,'date':curtime,'vno':vno,'type':type,'prevno':prevno})
    



@login_required(login_url='login')
def checkvoucher(request):
    company=request.session.get('company')
    
    
    vtype = request.GET.get('type', '')
    query = request.GET.get('query', '')
    
    vno=int(query)
    
    if vtype=='SI':
        customers = Tblbusinessissue.objects.filter(issuecode=query,issuetype=vtype, company=company)
        if(len(customers)>0):
            chkk='yes'
            data=[{'chk':chkk}]
        else:
            chkk='no'
            data=[{'chk':chkk}]
    else:
        chkk='ERR'
        data=[{'chk':chkk}]
    return JsonResponse('data')    

        