from django.shortcuts import render

# Create your views here.
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
from django.utils.functional import empty
from zshopapp.models import *
from zshopapp import models
from zshopapp.models import Tblcomplaintdetails,Tbljob,Tblworkcategory, Tbldepot, Tblitemcategory, Tblitemmaster,TblTransactionReceipt,Tblreceiptdetails, Tbluserdetails,Tblusermaster, Tblbatch,Tblcompanymaster, Tblbusinessissue,Tblissuedetails, Tblinventory,Tblaccgroup,Tblaccountledger,Tblgeneralledger
from django.http import HttpResponse, JsonResponse
import datetime
from datetime import timedelta
from django.db.models import Sum,F
from django.utils import timezone

from django.contrib.auth.decorators import login_required
# from technoapp.models import
from django_countries import countries
from googletrans import Translator
import requests
import qrcode
from django.http import HttpResponse
from django.shortcuts import render

import base64
import struct

from decimal import Decimal

# registration/views.pyimport hashlib
from django.shortcuts import render
from django.http import JsonResponse
import hashlib
import json

# MD5 hash generator function
def generate_hash(source_object, is_reg=True):
    if source_object is None:
        raise ValueError("Source object cannot be None")
    
    # Convert the object to a JSON string, this can be changed depending on how you want to serialize the object
    object_str = json.dumps(source_object, sort_keys=True)

    # Compute the hash
    md5_hash = hashlib.md5(object_str.encode('utf-8')).hexdigest()
    
    # Return the hash based on the is_reg flag
    if is_reg:
        return md5_hash[:8]  # First 8 characters (similar to C# code)
    else:
        return md5_hash[:16]  # Different length for non-registration

# View to handle registration code generation
import hashlib

import hashlib

def compute_hash(object_as_bytes, is_reg):
    try:
        # Create an MD5 hash object
        md5_hash = hashlib.md5()
        
        # Update the hash object with the byte data
        md5_hash.update(object_as_bytes)
        
        # Get the computed hash as bytes
        result = md5_hash.digest()

        # Create the final string by formatting the bytes into hex
        result_hex = ""
        
        if is_reg:
            # If 'is_reg' is True, append the first half of the MD5 hash in uppercase (X1 format in C#)
            for i in range(len(result) // 2):
                result_hex += format(result[i], "X")
        else:
            # If 'is_reg' is False, append the entire MD5 hash in uppercase (X2 format in C#)
            for i in range(len(result)):
                result_hex += format(result[i], "X2")
        
        # Return the final hash string
        return result_hex
    except Exception as e:
        print(f"Error in hash generation: {e}")
        return None
def generate_registration_code(request):
        cd_key = "SR-83937395589"
        product_id = "6447WR8956577895"

        # Combine the CD key and Product ID (after removing spaces) and convert to bytes
        combined_string = (cd_key.replace(" ", "") + product_id.replace(" ", "")).encode('utf-8')

        # Call the hash function with 'is_reg' set to True or False
        is_reg = True  # or False depending on the desired behavior
        hash_result = compute_hash(combined_string, is_reg)

        print(f"Generated Hash: {hash_result}")
        return HttpResponse(hash_result)

def testcode(request):
    return render(request,'test.html')
#SATLV Class to encode the invoice data in TLV format
class KSATLV:
    def __init__(self, branch_name, vat_no, inv_date, total, tax):
        self.branch_name = branch_name
        self.vat_no = vat_no
        self.inv_date = inv_date
        self.total = total
        self.tax = tax

    # Helper function to get the TLV bytes for each field
    def get_bytes(self, tag, value):
        value_bytes = value.encode('utf-8')
        length = len(value_bytes)
        return struct.pack(f"!B B {length}s", tag, length, value_bytes)

    # Function to generate the Base64 encoded TLV string
    def to_base64(self):
        tlv_bytes = b""

        # Add each field to the TLV byte array
        tlv_bytes += self.get_bytes(1, self.branch_name)  # Branch Name
        tlv_bytes += self.get_bytes(2, self.vat_no)      # VAT Number
        tlv_bytes += self.get_bytes(3, self.inv_date)    # Invoice Date
        tlv_bytes += self.get_bytes(4, self.total)       # Total Amount
        tlv_bytes += self.get_bytes(5, self.tax)         # Tax Amount

        # Return Base64 encoded string of the TLV data
        return base64.b64encode(tlv_bytes).decode('utf-8')

# View to generate QR Code for the e-Invoice
def generate_zakat_qr(request,customer,dates,vno,taxamt,totalamt):
    # Example dynamic data
    branch_name =customer  # Replace with actual branch name
    vat_no = vno  # Replace with actual VAT number
    inv_date =dates  # Current date in ISO format
    total = totalamt  # Replace with actual total amount
    tax = taxamt # Replace with actual tax amount

    # Instantiate KSATLV and get the Base64 encoded TLV data
    ksa_tlv = KSATLV(branch_name, vat_no, inv_date, total, tax)
    encrypted_data = ksa_tlv.to_base64()

    # Generate the URL with query parameters (modify this URL according to your needs)
    qr_url =encrypted_data

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Return the image as HTTP response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
def scan_invoice(request):
    # Get the 'data' query parameter from the URL
    qr_data = request.GET.get('data', None)
    
    if qr_data:
        # Decode the Base64 string (simply return the raw QR data for now)
        decoded_data = {
            'data': qr_data  # Simply return the raw QR data as is for this example
        }
    else:
        decoded_data = {}

    return render(request, 'test.html', {'data': decoded_data})
# Create your views here.
@login_required(login_url='login')
def home(request):
    company=request.session.get('company')
    cuser=request.session.get('cur_user')
    area=request.session.get('area')

    c_page=None
    mob=None
    c=None
    add_accGrp(company)
    catNoneAdd(company)
    add_ledger(company)
    
   
    
    
    print(cuser)
    ug=Tbluserdetails.objects.get(company=company,username=cuser)
    ugroup=ug.ugroup
 
        
    
        
    return render(request, 'index.html',{'user':company,'cuser':cuser,'area':area,'ug':ugroup})





@login_required(login_url='login')
def adminfu(request):
    company=request.session.get('company')
    cuser=request.session.get('cur_user')
    area=request.session.get('area')
    print(company)
    cd=Tblcompanymaster.objects.get(companyname=company)
    passw=cd.password
    
    

    if request.method=='POST':
        cm=Tblcompanymaster.objects.get(companyname=company)
        cm.delete()
        um=Tblusermaster.objects.all()
        um.delete()
        username=request.POST['uname']
        password=request.POST['pass']
        addcm=Tblcompanymaster.objects.create(companyname=username,password=password)
        addcm.save()
        delusertable=Tblusermaster.objects.filter(companyname=company,user=cuser,area=area)
        delusertable.delete()
        addusertable=Tblusermaster(companyname=username,password=password,user=cuser,area=area)
        addusertable.save()
        return redirect('/home')


    return render(request,'admin.html',{'company':company,'password':passw,'user':company,'cuser':cuser,'area':area})


def register(request):
    if request.method =='POST':
        username=request.POST['name']
        passw=request.POST['password']
        email=request.POST['mail']
        cpass=request.POST['cpassword']
        if passw==cpass:
            user=User.objects.create_user(username=username,email=email,password=passw)
            user.save()
            messages.info(request,"success")
            return redirect('login')
        else:
            messages.info(request,"password missmatch")

    return  render(request,'register.html')
def login(request):
    if 'company' in request.session:
        return redirect(home)
    cm=Tblcompanymaster.objects.all()
   
    if request.method=='POST':
        username=request.POST['company']
        password=request.POST['pass']
        cuser=request.POST['user']
        upass=request.POST['upass']
        area=request.POST['area']
       
        comp=Tblcompanymaster.objects.get(companyname=username)
        us=Tbluserdetails.objects.get(company=username,username=cuser)
        delusertable=Tblusermaster.objects.filter(companyname=username,user=cuser,area=area)
        delusertable.delete()
        addusertable=Tblusermaster(companyname=comp.companyname,password=password,user=cuser,area=area)
        addusertable.save()
        
        usero =auth.authenticate(request, username=username,password=password)
        if usero is not None:
            try:
                curusr=Tbluserdetails.objects.get(username=cuser,upassword=upass,company=username)
                if curusr is not None:
                    
                    auth.login(request,usero)
                    request.session['company']=username
                    request.session['area']=area
                    request.session['cur_user']=cuser
                    return redirect('/home')
                else:
                    messages.error(request, 'Invalid username or password')
            except Exception as e:
                messages.error(request,' Invalid username or password')
              # Redirect to your home page
        else:
            messages.error(request, 'Invalid Companyname  or password')
       
           
            
    return render(request,'login.html',{'company':cm})
def logout(request):
    auth.logout(request)
    request.session.flush()
    
    return redirect(login)

@login_required(login_url='login')
def itemcategory(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    preid = request.GET.get('itemid')
    type = request.GET.get('type')
    cname=''
    remark=''

    if preid!=None:
        ic=Tblitemcategory.objects.get(company=company,categoryid=preid)
        cname=ic.categoryname
        remark=ic.remarks
        cidmain=ic.categoryidmain

    
    cid=1

    a=Tblitemcategory.objects.filter(company=company)

    amain=Tblitemcategory.objects.all()
    if len(amain)==0:
        cidmain=1

    else:
        cidmain= Tblitemcategory.objects.aggregate(max=Max('categoryidmain'))["max"]+1
    if len(a)==0:
        cid=1

    else:
        cid= Tblitemcategory.objects.filter(company=company).aggregate(max=Max('categoryid'))["max"]+1
    
    if request.method == 'POST':
        name = request.POST['categname']
        remark = request.POST['categremark']
        catid = request.POST['categid']
        cmain = request.POST['cm']
        edittype=request.POST [ 'edittype' ]
        print()
        if (name!=""):
            delitem = Tblitemcategory.objects.filter(categoryid=catid,company=company)
            delitem.delete()
            categ = Tblitemcategory.objects.create(categoryid=catid,categoryidmain=cmain,area=area, categoryname=name, remarks=remark,company=company)
            categ.save()
            messages.info(request, "success")
            if edittype=='edit':
                return HttpResponse('<script type="text/javascript">window.close()</script>') 
            else:
                return redirect('/itemcateg')
            # return render(request, 'itemcategory.html', {'cid': cid})


        else:

            messages.info(request, "Please enter category name")

    return render(request,'itemcategory.html',{'cid':cid,'cname':cname,'preid':preid,'cidmain':cidmain ,'remark':remark,'type':type,'user':company,'cuser':user,'area':area})
@login_required(login_url='login')
def itemadd(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    preid = request.GET.get('itemid')
    type = request.GET.get('type')
    today=datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    itid=0
    litid=0
    itidmain=0
    # icateg=Tblitemcategory.objects.all()
    itemcat = Tblitemcategory.objects.get(categoryidmain=0)
    a = Tblitemmaster.objects.filter(company=company)
    amain = Tblitemmaster.objects.all()
    if len(amain) ==0:
        itidmain=1
    else:
        itidmain = Tblitemmaster.objects.aggregate(max=Max('itemidmain'))["max"] + 1

    
    if len(a) == 0:
        itid = 1
        litid=1
        

    else:
        itid = Tblitemmaster.objects.filter(company=company).aggregate(max=Max('itemid'))["max"] + 1
        litid = Tblitemmaster.objects.filter(company=company).aggregate(max=Max('litid'))["max"] + 1
        
    itembcode=(100+litid)

    itemc=Tblitemcategory.objects.filter(Q(company=company)|Q(company=None))
    if len(itemc) == 0:
        itemc2=None
    else:
        itemc2=itemc
    if preid==None:
        preid='empt'

    if request.method =='POST':

        bcode=request.POST['barcode']
        itemidpg=request.POST['itemid']
        itemname=request.POST['itemname']
        itemcode=request.POST['itemcode']
        usingmechine=request.POST['usingmechine']
        ilang=request.POST [ 'secodlanguage' ]
        itemcateg=request.POST [ 'itemcategory' ]
        manufacturer=request.POST [ 'manufacturer' ]
        itemclass=request.POST [ 'itemclass' ]
        vat=request.POST [ 'vat' ]
        srate=request.POST [ 'srate' ]
        prate=request.POST [ 'prate' ]
        saletax=request.POST [ 'saletax' ]
        ptax=request.POST [ 'ptax' ]
        op=request.POST [ 'opqty' ]
        edittype=request.POST [ 'edittype' ]

        if itemcateg =='None':
            itemcateg=0

        if itemclass=='0':
            itemclass='Stock Item'
        elif itemclass=='1':
            itemclass='Services'
        elif itemclass=='2':
            itemclass='Finished product'
        elif itemclass=='3':
            itemclass='Finished product2'
        if srate == '':
            srate=0
        
        if prate == '':
            prate=0

        if ptax == 1:
            costrate=prate
        else:
            cost=int(float( vat))*(float(prate)/100)
            costrate=float( prate)+float( cost)



        if itemname!="":
            
            
            if op=='':
                op=0
            delitem = Tblitemmaster.objects.filter(itemid=itemidpg,company=company)
            delitem.delete()
            delitem = Tblbatch.objects.filter(bcode=bcode,company=company)
            delitem.delete()


            itemmster=Tblitemmaster.objects.create(itemid=itemidpg,itemidmain=itidmain,itemname=itemname,bcode=bcode,itemcode=itemcode,categoryid=itemcateg,
                                usingmechine=usingmechine,ilang=ilang,manufacturer=0,itemclass=itemclass,vat=vat,srate=srate,
                                prate=prate,incs=saletax,incp=ptax,status=1,agentcommision=0,minstock=0,cooly=0,maximum=0,unit="0",
                                cst=0,rack=0,slabid=0,ledid=0,balance=0,plu="",bunit="0",company=company,os=op,litid=litid)
            itemmster.save()
            batch=Tblbatch.objects.create(bcode=bcode,itemid=itemidpg,itemidmain=itidmain,srate=srate,prate=prate,bid=bcode,costcenter=0,depo=0,
                                ledcode=0,recptcode=0,unconv=0,company=company,crate=costrate)
            batch.save()
           
            if op !='':
                delitem = Tblinventory.objects.filter(pcode=itemidpg,company=company)
                delitem.delete()
                inventory = Tblinventory.objects.create(vcode=0, dcode="0", invdate=curtime,pcode=itid,os=op, 
                            batchcode=bcode,company=company)
                inventory.save()

            if edittype=='edit':
                return HttpResponse('<script type="text/javascript">window.close()</script>')  

            else:

                return redirect('/itemad')
            


        else:
            messages.info(request,"Please enter itemname")
    
    return render(request,'itemadd.html',{'categ':itemc2,'itemiddbcode':itembcode,'itemidd':itid,'catname':itemcat,'preid':preid,'type':type,'user':company,'cuser':user,'area':area})

@login_required(login_url='login')

def cus(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')

    preid = request.GET.get('lid')
    type = request.GET.get('type')

    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    
    b=Tblaccgroup.objects.get(agroupidmain=18)

    a = "Create Customer"
    # ACCG = Tblaccgroup.objects.all()
    led = Tblaccountledger.objects.filter(company=company)
    ledmain = Tblaccountledger.objects.all()
    if len(ledmain) == 0:
        ledidmain=30
    else:
        ledidmain = Tblaccountledger.objects.aggregate(max=Max('lidmain'))["max"] + 1

    if len(led) == 0:
        ledid = 30
    

    else:
        ledid = Tblaccountledger.objects.filter(company=company).aggregate(max=Max('lid'))["max"] + 1
    # if len(ACCG) == 0:
    #     ACCG2 = None
    # else:
    #     ACCG2 = ACCG
    
    if request.method == 'POST':
        lname = request.POST['lname']
        lalias = request.POST['laliasname']
        accgrp = request.POST['accgroup']
        openingb = request.POST['ob']
        obtype = request.POST['obtype']
        usecard = request.POST['obtype']
        date = request.POST['date']
        address = request.POST['address']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        disc = request.POST['disc']
        taxno = request.POST['taxno']
        area = request.POST['area']
        commision = request.POST['commision']
        lid = request.POST['lid']
        lidmain = request.POST['lidmain']
        edittype = request.POST['edittype']
        if disc=='' or disc==None:
            disc=0.0
        if taxno=='' or taxno==None:
            taxno=0.0
        if commision=='' or commision==None:
            commision=0.0
        if openingb=='':
            openingb=0
            
        if obtype == '1':
            cr = openingb
            dr = 0
        else:
            dr = openingb
            cr = 0
            


        if lname != '':
            acled=Tblaccountledger.objects.filter(company=company,lid=lid)
            acled.delete()
            genled=Tblgeneralledger.objects.filter(company=company,ledcode=lid)
            genled.delete()
            ledger = Tblaccountledger.objects.create(lid=lid,lidmain=lidmain, lname=lname, laliasname=lalias, agroupid=18,
                                                     usecard=usecard,company=company,
                                                     address=address,phone=phone,mobile=mobile,discper=disc,taxregno=taxno,area=area,commission=commision)
            ledger.save()
            generalledger = Tblgeneralledger.objects.create(ledcode=lid, vdate=date, dbamt=dr, cramt=cr, vtype="OB",
                                                            particulars="Opening Balance", refno="1001",tblaccountledger=ledger,uid=user,company=company)

            generalledger.save()
            if edittype=='edit':

                return HttpResponse('<script type="text/javascript">window.close()</script>')
            else:

                return redirect( '/cus')
    
    return render(request, 'ledgeradd.html',{'accg':b,'lid':ledid,'lidmain':ledidmain,'heading':a,'date':curtime,'preid':preid,'type':type,'user':company,'cuser':user,'area':area})
@login_required(login_url='login')
def sup(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    preid = request.GET.get('lid')
    type = request.GET.get('type')
    
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    a = "Create Supplier"
    supp = Tblaccgroup.objects.get(agroupidmain=19)
    led = Tblaccountledger.objects.filter(company=company)

    ledmain = Tblaccountledger.objects.all()
    if len(ledmain) == 0:
        ledidmain=30
    else:
        ledidmain = Tblaccountledger.objects.aggregate(max=Max('lidmain'))["max"] + 1
    if len(led) == 0:
        ledid = 30
        ref = 1001

    else:
        ledid = Tblaccountledger.objects.filter(company=company).aggregate(max=Max('lid'))["max"] + 1
    
    if request.method == 'POST':
        lname = request.POST['lname']
        lalias = request.POST['laliasname']
        accgrp = request.POST['accgroup']
        openingb = request.POST['ob']
        obtype = request.POST['obtype']
        usecard = request.POST['obtype']
        date = request.POST['date']
        address = request.POST['address']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        disc = request.POST['disc']
        taxno = request.POST['taxno']
        area = request.POST['area']
        lid = request.POST['lid']
        lidmain = request.POST['lidmain']
        edittype = request.POST['edittype']
        commision = request.POST['commision']
        if disc=='' or disc==None:
            disc=0.0
        if taxno=='' or taxno==None:
            taxno=0.0
        if commision=='' or commision==None:
            commision=0.0
        
        if openingb=='':
            openingb=0
        if obtype == '1':
            cr = openingb
            dr = 0
        else:
            dr = openingb
            cr = 0
        if lname != '':
            acled=Tblaccountledger.objects.filter(company=company,lid=lid)
            acled.delete()
            genled=Tblgeneralledger.objects.filter(company=company,ledcode=lid)
            genled.delete()
            ledger = Tblaccountledger.objects.create(lid=lid,lidmain=lidmain, lname=lname, laliasname=lalias, agroupid=19,
                                                     usecard=usecard,company=company,
                                                     address=address,phone=phone,mobile=mobile,discper=disc,taxregno=taxno,area=area,commission=commision)
            ledger.save()
            generalledger = Tblgeneralledger.objects.create(ledcode=lid, vdate=date, dbamt=dr, cramt=cr, vtype="OB",
                                                            particulars="Opening Balance", refno=1001,tblaccountledger=ledger,uid=user,area=area, company=company)

            generalledger.save()

            if edittype=='edit':

                return HttpResponse('<script type="text/javascript">window.close()</script>')
            else:

                return redirect('/?comp' and '/sup')
    
    return render(request, 'ledgeradd.html',{'accg':supp,'lid':ledid,'lidmain':ledidmain,'heading':a,'date':curtime,'preid':preid,'type':type,'user':company,'cuser':user,'area':area})
@login_required(login_url='login')
def ledgeradd(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')

    preid = request.GET.get('lid')
    type = request.GET.get('type')

    
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    a="Create Ledger"
    ACCG = Tblaccgroup.objects.filter(Q(company=company) |Q(company=None) )
    print(len(ACCG))
    led = Tblaccountledger.objects.filter(company=company)
    ledmain = Tblaccountledger.objects.all()
    if len(ledmain) == 0:
        ledidmain=30
    else:
        ledidmain = Tblaccountledger.objects.aggregate(max=Max('lidmain'))["max"] + 1
    if len(led) == 0:
        ledid = 30

    else:
        ledid = Tblaccountledger.objects.filter(company=company).aggregate(max=Max('lid'))["max"] + 1

    if len(ACCG) == 0:
        ACCG2 = 'None'
    else:
        ACCG2 = ACCG
    
    if request.method =='POST':
        lname = request.POST['lname']
        lalias = request.POST['laliasname']
        accgrp = request.POST['accgroup']
        openingb = request.POST['ob']
        obtype = request.POST['obtype']
        usecard = request.POST['obtype']
        date = request.POST['date']
        lid = request.POST['lid']
        lidmain = request.POST['lidmain']
        edittype = request.POST['edittype']
       




        if obtype=='1':
            cr=openingb
            dr=0
        else:
            dr=openingb
            cr=0
        if lname!='':
                acled=Tblaccountledger.objects.filter(company=company,lid=lid)
                acled.delete()
                genled=Tblgeneralledger.objects.filter(company=company,ledcode=lid)
                genled.delete()
                ledger = Tblaccountledger.objects.create(lid=lid,lidmain=lidmain,lname=lname,laliasname=lalias,agroupid=accgrp,usecard=usecard,area=area,company=company)
                ledger.save()
                generalledger = Tblgeneralledger.objects.create(ledcode=lid ,tblaccountledger=ledger,vdate=date,dbamt=dr,cramt=cr,vtype="OB",area=area,
                                particulars="Opening Balance",refno="1001",company=company)
                generalledger.save()
                messages.info(request, "success")
                if edittype=='edit':

                    return HttpResponse('<script type="text/javascript">window.close()</script>') 
                else:
                    return redirect('/?comp' and '/ledgeradd')
        else:
            messages.info(request,"password missmatch")

    return render(request, 'ledgeradd.html',{'accg':ACCG2,'lid':ledid,'lidmain':ledidmain,'heading':a,'date':curtime,'preid':preid,'type':type,'user':company,'cuser':user,'area':area} )

@login_required(login_url='login')
def ledgroup(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    preid = request.GET.get('ledid')
    type = request.GET.get('type')
    accg = Tblaccgroup.objects.filter(company=None)
    aname=''
    aunder=''
    if preid!=None:
        ic=Tblaccgroup.objects.get(company=company,agroupid=preid)
        aname=ic.agroupname
        aunder=ic.Aunder
        # ic2=Tblaccgroup.objects.get(company=company,agroupid=aunderid)
        # aunder=ic2.agroupname
    lidd=1
    a=Tblaccgroup.objects.filter(company=company)
    amain=Tblaccgroup.objects.all()
    if len(amain)==0:
        lidmain=32

    else:
        lidmain= Tblaccgroup.objects.aggregate(max=Max('agroupidmain'))["max"]+1
    if len(a)==0:
        lidd=32

    else:
        lidd= Tblaccgroup.objects.filter(company=company).aggregate(max=Max('agroupid'))["max"]+1
    if request.method == 'POST':
        name = request.POST['gname']
        under = request.POST['aunder']
        aid = request.POST['aid']
        edittype = request.POST['edittype']

        if (name!=""):
            delitem=Tblaccgroup.objects.filter(company=company,agroupid=aid)
            delitem.delete()
            lg = Tblaccgroup.objects.create(agroupid=lidd,agroupidmain=lidmain, agroupname=name,Aunder=under,company=company)
            lg.save()
            messages.info(request, "success")
            if edittype=='edit':
                return HttpResponse('<script type="text/javascript">window.close()</script>') 
            else:
                return redirect('/' and '/ledgergroup')


        else:

            messages.info(request, "Please enter category name")

    return render(request,'ledgergroup.html',{'lid':lidd,'accg':accg,'preid':preid,'type':type,'aname':aname,'aunder':aunder,'user':company,'cuser':user,'area':area})

def insert_ledgroup(id,name,under,comp):
    # u=Tblusermaster.objects.get(companyname=comp)
    # company=u.companyname
    a = Tblaccgroup.objects.all()
    
    if len(a)<27:
          Tblaccgroup.objects.create(agroupidmain=id,agroupid=id, agroupname=name, Aunder=under)
          

    else:
        return

def insert_ledger(id,name,acgroup,comp):
    # u=Tblusermaster.objects.get(companyname=comp)
    # company=u.companyname
    print(comp)
    a = Tblaccountledger.objects.filter(company=comp)
    aa = Tblaccountledger.objects.filter()
    if len(aa)==0:
        ldid=1
    else:
         
         ldid=Tblaccountledger.objects.aggregate(max=Max('lidmain'))["max"]+1
    

    
    if len(a)<27:

        al=Tblaccountledger.objects.create(lidmain=ldid,lid=id, lname=name, agroupid=acgroup,company=comp)
        al.save()

    

def categNone(id,name,remark,comp):
    # u=Tblusermaster.objects.get(companyname=comp)
    # company=u.companyname
    it=Tblitemcategory.objects.all()

    if len(it)<1:
        Tblitemcategory.objects.create(categoryidmain=id,categoryid=0,categoryname=name,remarks=remark)
    else:
        return

def catNoneAdd(company):
    categNone(0,"None","",company)

def add_accGrp(company):

    insert_ledgroup(1, "Asset", 4,company)
    insert_ledgroup(2, "Liability", 4,company)
    insert_ledgroup(3, "Profit $ Loss A/C", 0,company)
    insert_ledgroup(4, "Balancesheet", 0,company)
    insert_ledgroup(6, "Expense", 3,company)
    insert_ledgroup(7, "Income", 3,company)
    insert_ledgroup(10, "Current Assets", 1,company)
    insert_ledgroup(11, "Current Liability", 2,company)
    insert_ledgroup(12, "Direct Expense", 6,company)
    insert_ledgroup(13, "Direct Income", 7,company)
    insert_ledgroup(14, "Fixed Assets", 1,company)
    insert_ledgroup(15, "Indirect Expense", 6,company)
    insert_ledgroup(16, "Indirect Income", 7,company)
    insert_ledgroup(17, "Long Term Liability", 2,company)
    insert_ledgroup(18, "customer", 10,company)

    insert_ledgroup(19, "Supplier", 11,company)
    insert_ledgroup(20, "Services", 13,company)
    insert_ledgroup(21, "Sales", 13,company)
    insert_ledgroup(22, "Employee", 15,company)
    insert_ledgroup(23, "Tax Collected", 11,company)
    insert_ledgroup(24, "Bank", 10,company)
    insert_ledgroup(25, "Cash", 10,company)
    insert_ledgroup(26, "Purchase", 12,company)
    insert_ledgroup(27, "Opening Stock", 12,company)
    insert_ledgroup(28, "Capital", 17,company)
    insert_ledgroup(29, "Agent", 11,company)
    insert_ledgroup(30, "Salaries & Incentives", 15,company)
    insert_ledgroup(31, "Salaries", 30,company)
def add_ledger(company):
    insert_ledger(1, "Cash", 25,company)
    insert_ledger(2, "Sales", 21,company)
    insert_ledger(3, "Purchase", 26,company)
    insert_ledger(6, "Discount Received", 16,company)
    insert_ledger(7, "Discount Allowed", 15,company)
    insert_ledger(8, "VAT Paid", 23,company)
    insert_ledger(9, "VAT collected", 23,company)
    insert_ledger(10, "Excise Duty", 16,company)
    insert_ledger(11, "Roundoff Received", 15,company)
    insert_ledger(12, "Roundoff Allowed", 13,company)
    insert_ledger(13, "Profit or Loss for Previous Year", 2,company)
    insert_ledger(14, "Service Account", 20,company)
    insert_ledger(15, "Service Tax", 20,company)
    insert_ledger(16, "Discount on Service", 15,company)
    insert_ledger(17, "Sales Return Account", 21,company)
    insert_ledger(18, "Purchase Return Account", 26,company)
    insert_ledger(19, "Opening Stock", 27,company)
    insert_ledger(20, "Capital", 28,company)
    insert_ledger(21, "Cheques Recieved", 10,company)
    insert_ledger(22, "Credit Card Receieved", 10,company)
    insert_ledger(23, "Agent commision", 15,company)
    insert_ledger(24, "CST Receieved", 21,company)
    insert_ledger(25, "CST Paid", 26,company)
    
    insert_ledger(26, "Otherexpense on sales", 15,company)
    insert_ledger(27, "Cooly", 12,company)
    insert_ledger(28, "Bank", 24,company)
    insert_ledger(29, "Salary", 30,company)
 
def addcompany(request):
    if request.method == 'POST':
        
        
        
        
        username = request.POST['name']
        password = request.POST['password']
        repassword = request.POST['re_password']
        ucheck=Tblcompanymaster.objects.filter(companyname=username)
        if(len(ucheck)>0):
            messages.info(request,"user already exist")
        else:
            if password==repassword:
                user=Tblcompanymaster.objects.create(companyname=username,password=password)
                user.save()
                userdet=Tbluserdetails.objects.create(userid=0,username='ADMIN',upassword='admin',ugroup=0,astatus=1,company=username)
                userdet.save()
                areaadd=Tbldepot.objects.create(dcode=0,dname='HEAD OFFICE',company=username)
                areaadd.save()
                user=User.objects.create_user(username=username,password=password)
                user.save()
            else:
                messages.info(request,"password missmatch")


        
        

    return redirect('/') 
@login_required(login_url='login')
def useradd(request):
    preid = request.GET.get('uid')
    type = request.GET.get('type')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
   
    
    a=Tbluserdetails.objects.filter(company=company,area=area)
    
    
    if len(a)==0:
        uid=1

    else:
        uid= Tbluserdetails.objects.filter(company=company,area=area).aggregate(max=Max('userid'))["max"]+1
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['pass']
        ugrp = request.POST['group']
        usid = request.POST['uid']
        edittype=request.POST['edittype']
        
        astat = request.POST['astatus']
        delarea=Tbluserdetails.objects.filter(company=company,userid=usid,area=area)
        delarea.delete()
        usersave = Tbluserdetails.objects.create(userid=usid,username=uname,upassword=upass,ugroup=ugrp,astatus=astat,company=company,area=area)
        usersave.save()
        if edittype=='edit':

            return HttpResponse('<script type="text/javascript">window.close()</script>') 
        else:
            return redirect('/useradd')
        
        



    
    return render(request,'useradd.html',{'uid':uid,'preid':preid,'type':type,'user':company,'cuser':user,'area':area})
@login_required(login_url='login')

def stockareaadd(request):
    preid = request.GET.get('dcode')
    type = request.GET.get('type')
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    a=Tbldepot.objects.filter(company=company)
    
    
    if len(a)==0:
        dcode=1

    else:
        dcode= Tbldepot.objects.filter(company=company).aggregate(max=Max('dcode'))["max"]+1
    


    if request.method == 'POST':
        dc = request.POST['dcode']
        aname = request.POST['aname']
        address = request.POST['address']
        city = request.POST['city']
        pin = request.POST['pin']
        phone = request.POST['phone']
        mobile = request.POST['mobile']
        cperson = request.POST['cperson']
        regno = request.POST['regno']
        licenseno = request.POST['license']
        description = request.POST['description']
        edittype=request.POST['edittype']
        delarea=Tbldepot.objects.filter(company=company,dcode=dc)
        delarea.delete()
        areaadd=Tbldepot.objects.create(dcode=dc,dname=aname,address=address,city=city,pin=pin,phoneno=phone,mobile=mobile,cperson=cperson,
                                        regno=regno,	lescenseno=licenseno,description=description,company=company)
        areaadd.save()

        if edittype=='edit':

            return HttpResponse('<script type="text/javascript">window.close()</script>') 
        else:
            return redirect('/Addarea')
        

    return render(request,'Area.html',{'dcode':dcode,'preid':preid,'type':type,'user':company,'cuser':user,'area':area})





#Transactions




@login_required(login_url='login')

def search_customer(request):
    company=request.session.get('company')
    
   

    query = request.GET.get('query', '')
    iid = request.GET.get('id')
    lidd=int(iid)
    
    if(lidd==18 or lidd==19):
        customers = Tblaccountledger.objects.filter(lname__icontains=query,agroupid=iid,company=company)
    else:
        customers=Tblaccountledger.objects.filter(Q(lname__icontains=query,company=company) )   
    data = [{'id': customer.lid, 'name': customer.lname,'alias':customer.laliasname,'mobile':customer.mobile} for customer in customers]
    return JsonResponse({'customers': data})


def search_item(request):
    company=request.session.get('company')
    
    

    query = request.GET.get('query', '')

    customers = Tblitemmaster.objects.filter(Q(itemname__icontains=query,company=company) | Q(bcode__icontains=query,company=company) )
    data = [{'id': customer.itemid, 'name': customer.itemname,'bcode':customer.bcode,'itemcode': customer.itemcode, 'ilang': customer.ilang,'prate':customer.prate,'srate':customer.srate,'incs':customer.incs,'vat':customer.vat,'mrp':customer.mrp} for customer in customers]
    return JsonResponse({'customers': data})
def search_stockitem(request):
    company=request.session.get('company')
    
    

    query = request.GET.get('query', '')

    items = Tblitemmaster.objects.filter(Q(itemname__icontains=query,company=company,itemclass='Stock Item') )
    data = [{'id': item.itemid, 'name': item.itemname,'srate':item.prate} for item in items]
    return JsonResponse({'customers': data})


def get_previous(request):
    company=request.session.get('company')
    
    

    query = request.GET.get('query', '')
    vtype = request.GET.get('vtype')
    print(vtype)
    issuedet = Tblissuedetails.objects.filter(issuecode=query,vtype=vtype,company=company)
    


    bissue = Tblbusinessissue.objects.filter(issuecode=query,issuetype=vtype,company=company)
    
    lvno=len(bissue)
    


    
    issudata = [{'tempqty': items.qty,'freeqty':items.freeqty,'pcode':items.pcode,'rate':items.rate,'crate':items.crate,'mrp':items.mrp,
                'discrate':items.discrate,'taxrate':items.taxrate,'netamt':items.netamt,'taxper':items.taxper,'batchid':items.batchid,
                'exdate':items.exdate} for items in issuedet]
    
   
    bdata = [{'vno': bitems.issuecode,'issuedate':bitems.issuedate,'dcode':bitems.dcode,'ledcodedr':bitems.ledcodedr,'tename':bitems.tename,'refno':bitems.refno,
            'tmobile':bitems.tmobile,'taddress':bitems.taddress,'amt':bitems.amt,'taxamt':bitems.taxamt,'tvat':bitems.tvat,'twopayment':bitems.twopayment,'twopayamt':bitems.twopayamt,
            'mpayment':bitems.mpayment,'ledcode':bitems.ledcodecr,'discamt':bitems.discamt,'discperc':bitems.discperc} for bitems in bissue]
    if vtype=='SS':
        print(query)
        print(company)
        complaint = Tblcomplaintdetails.objects.filter(vno=query,company=company)
        print(len(complaint))
    
    
    


    
        complaintdata = [{'passw': items.password,'imei':items.imei,'battery':items.battery,'facecover':items.facecover,'backcover':items.backcover,
                          'mmc':items.mmc,'sim':items.sim,'charger':items.charger,'nsignal':items.nsignal,'ncharge':items.ncharge,
                          'npower':items.npower,'mnt':items.mnt,'cnt':items.cnt,'fnt':items.fnt,'snt':items.snt,
                          'keypadnt':items.keypadnt,'lcdprob':items.lcdprob,'addate':items.addate} for items in complaint]


        data={"data1":bdata,"data2":issudata,"data3":complaintdata, 'lvno':lvno}
    else:
        print('si')

        data={"data1":bdata,"data2":issudata,'lvno':lvno}
    # if(len(bissue)==0):
    #     print("chck")
    #     return render(request,'sales.html')

    return JsonResponse(data)

@login_required(login_url='login')
def get_previouspurchase(request):
    company=request.session.get('company')
    
    
    
    query = request.GET.get('query', '')
    vtype = request.GET.get('vtype')

    receipt = Tblreceiptdetails.objects.filter(recptcode=query,vtype=vtype,company=company)

    transreciept = TblTransactionReceipt.objects.filter(recptcode=query,recpttype=vtype,company=company)
    
    lvno = len(transreciept)

    issudata = [
        {'tempqty': items.qty, 'freeqty': items.freeqty, 'pcode': items.pcode, 'rate': items.rate, 'crate': items.crate,
         'mrp': items.mrp,
         'discrate': items.discrate, 'taxrate': items.taxrate, 'netamt': items.netamt, 'taxper': items.taxper,
         'batchid': items.batchid,
         'exdate': items.exdate} for items in receipt]

    bdata = [
        {'vno': bitems.recptcode, 'recptdate': bitems.recptdate, 'dcode': bitems.dcode, 'ledcodedr': bitems.ledcodedr,
         'tename': bitems.tename,
         'tmobile': bitems.tmobile, 'refno': bitems.refno, 'taddress': bitems.taddress, 'amt': bitems.amt, 'taxamt': bitems.taxamt,
         'tvat': bitems.tvat,
         'mpayment': bitems.mpayment, 'ledcode': bitems.ledcodecr,'discamt':bitems.discamt,'discperc':bitems.discperc,'billimg': bitems.pbill.url if bitems.pbill else None, } for bitems in transreciept]

    data = {"data1": bdata, "data2": issudata, 'lvno': lvno}
  
    # if(len(bissue)==0):
    #     print("chck")
    #     return render(request,'sales.html')

    return JsonResponse(data)
@login_required(login_url='login')
def get_previoupaymentreceipt(request):
    company=request.session.get('company')
    
    query = request.GET.get('query', '')
    vtype = request.GET.get('vtype', '')

    ledg = Tblgeneralledger.objects.filter(Q(vno=query,vtype=vtype,company=company))

      
    lvno = len(ledg)

    ledgerdata = [{'vno':items.vno,'vdate':items.vdate,'ledcode':items.ledcode,'cramt':items.cramt,'dbamt':items.dbamt,'cramt':items.cramt,'taxperc':items.rptaxperc,'taxamt':items.rptaxamt,'naration2':items.naration2} for items in ledg]

    

    data = { "data1": ledgerdata, 'lvno': lvno}
  
    
    return JsonResponse(data)

def deletesales(vno,vtype,invdlt,company):
    
    if(vtype=='SI' or vtype=='SO'):
        delissue = Tblissuedetails.objects.filter(issuecode=vno,vtype=vtype,company=company)
        delissue.delete()
        delbissue = Tblbusinessissue.objects.filter(vno=vno,issuetype=vtype,company=company)
        delbissue.delete()
        delinv = Tblinventory.objects.filter(vcode=vno,sales__gt=0,company=company)
        delinv.delete()
    if(vtype=='SR'):
        deltr = TblTransactionReceipt.objects.filter(recptcode=vno,recpttype=vtype,company=company)
        deltr.delete()
        delrd = Tblreceiptdetails.objects.filter(recptcode=vno,vtype=vtype,company=company)
        delrd.delete()
        delinv = Tblinventory.objects.filter(vcode=vno,sr__gt=0,company=company)
        delinv.delete()
    if(vtype=='PR'):

        delissue = Tblissuedetails.objects.filter(issuecode=vno,vtype=vtype,company=company)
        delissue.delete()
        delbissue = Tblbusinessissue.objects.filter(vno=vno,issuetype=vtype,company=company)
        delbissue.delete()
        delinv = Tblinventory.objects.filter(vcode=vno,pr__gt=0,company=company)
        delinv.delete()
    if(vtype=='SS'):

        delissue = Tblissuedetails.objects.filter(issuecode=vno,vtype=vtype,company=company)
        delissue.delete()
        delbissue = Tblbusinessissue.objects.filter(vno=vno,issuetype=vtype,company=company)
        delbissue.delete()
        delcdetail=Tblcomplaintdetails.objects.filter(vno=vno,company=company)
        delcdetail.delete()  
    else:
        deltr = TblTransactionReceipt.objects.filter(recptcode=vno,recpttype=vtype,company=company)
        deltr.delete()
        delrd = Tblreceiptdetails.objects.filter(recptcode=vno,vtype=vtype,company=company)
        delrd.delete()
        delinv = Tblinventory.objects.filter(vcode=vno,purchase__gt=0,company=company)
        delinv.delete()
     

    
    
    delinv = Tblgeneralledger.objects.filter(vno=vno,vtype=vtype,company=company)
    delinv.delete()



@login_required(login_url='login')
def get_customer(request):
    company=request.session.get('company')
    
    

    query = request.GET.get('query', '')
    
    lid=int(query)
    
    if lid>=30:
        customers = Tblaccountledger.objects.get(lid=lid ,company=company)
        genled=Tblgeneralledger.objects.get(ledcode=lid,company=company,vtype='OB')
        print(genled.vdate)

        data = [{'id': customers.lid, 'name': customers.lname,'lidmain':customers.lidmain, 'agroupid':customers.agroupid,'laliasname':customers.laliasname,
             'address':customers.address,'phone':customers.phone,'mobile':customers.mobile,'taxregno': customers.taxregno,
             'discper':customers.discper,'commision':customers.commission,'dbamt':genled.dbamt,'cramt':genled.cramt,'vdate':genled.vdate,'gl':1}]
    else:
        customers = Tblaccountledger.objects.get(lid=lid ,company=company)
        genled2=Tblgeneralledger.objects.filter(ledcode=lid,company=company,vtype='OB')
        if len(genled2)>0:
                genled=Tblgeneralledger.objects.get(ledcode=lid,company=company,vtype='OB')
                
                
            
                data = [{'id': customers.lid, 'name': customers.lname,'lidmain':customers.lidmain, 'agroupid':customers.agroupid,'laliasname':customers.laliasname,
             'address':customers.address,'phone':customers.phone,'mobile':customers.mobile,'taxregno': customers.taxregno,
             'discper':customers.discper,'commision':customers.commission,'dbamt':genled.dbamt,'cramt':genled.cramt,'vdate':genled.vdate,'gl':1}]
        else:

            data = [{'id': customers.lid, 'name': customers.lname,'lidmain':customers.lidmain, 'agroupid':customers.agroupid,'laliasname':customers.laliasname,
                'address':customers.address,'phone':customers.phone,'mobile':customers.mobile,'taxregno': customers.taxregno,
                'discper':customers.discper,'commision':customers.commission,'gl':0}]

        
   
    
    
    return JsonResponse({'customers': data})

@login_required(login_url='login')


def get_item(request):

    company=request.session.get('company')
    
    itype = request.GET.get('type')
    query = request.GET.get('query')
    # itemids=int(query)
    
    if(itype=='bcode'):
        customers = Tblitemmaster.objects.get(bcode=query,company=company)
    else:
        
        customers = Tblitemmaster.objects.get(itemid=query,company=company)
    data = [{'id': customers.itemid, 'name': customers.itemname,'itemcode':customers.itemcode,'ilang': customers.ilang,'bcode':customers.bcode,'srate':customers.srate,'prate':customers.prate,'vat':customers.vat,'incs':customers.incs,'incp':customers.incp, 'usingmechine':customers.usingmechine,'categoryid':customers.categoryid,'os':customers.os,'manufacturer':customers.manufacturer,'itemclass':customers.itemclass} ]
    return JsonResponse({'customers': data})


@login_required(login_url='login')
def cleartrn(request):
    data=None
    company=request.session.get('company')
    
    print("company",company)
    if(company==''):
        bi=Tblbusinessissue.objects.all()
        bi.delete()
        issd=Tblissuedetails.objects.all()
        issd.delete()
        tr=TblTransactionReceipt.objects.all()
        tr.delete()
        rd=Tblreceiptdetails.objects.all()
        rd.delete()
        gl=Tblgeneralledger.objects.filter(Q(vtype='SI')|Q(vtype='SR')|Q(vtype='PI')|Q(vtype='PR')|Q(vtype='R')|Q(vtype='P')|Q(vtype='SS'))
        gl.delete()
        inv=Tblinventory.objects.all()
        inv.delete()
        data='success'
    else:
        bi=Tblbusinessissue.objects.filter(company=company)
        len(bi)
        bi.delete()
        issd=Tblissuedetails.objects.filter(company=company)
        issd.delete()
        tr=TblTransactionReceipt.objects.filter(company=company)
        tr.delete()
        rd=Tblreceiptdetails.objects.filter(company=company)
        rd.delete()
        gl=Tblgeneralledger.objects.filter(company=company).exclude(vtype='OB')
        gl.delete()
        inv=Tblinventory.objects.filter(company=company,os=None )
        inv.delete()
        data='success'

    return JsonResponse({'msg':data})
@login_required(login_url='login')
def printtrn(request):
    company=request.session.get('company')
    
    printtype = request.GET.get('printtype')
    title = request.GET.get('title')
    headerchk = request.GET.get('headerchk')
    footerchk = request.GET.get('footerchk')
    print("headerchk",headerchk)
    print("footerchk",footerchk)
    
    
    vno = request.GET.get('voucher')
    mobile = request.GET.get('mobile')
    cus = request.GET.get('cus')
    date = request.GET.get('date')
    vtype = request.GET.get('vtype')
    taxamt = request.GET.get('taxamt')
    totalamt = request.GET.get('totalamt')
    itemname_array = request.GET.get('item', '[]')
    itemarray = json.loads(itemname_array)
    slang_array = request.GET.get('slang', '[]')
    slangarray = json.loads(slang_array)
    qty_array = request.GET.get('qty', '[]')
    qtyarray = json.loads(qty_array)
    price_array = request.GET.get('price', '[]')
    pricearray = json.loads(price_array)
    gross_array = request.GET.get('gross', '[]')
    grossarray = json.loads(gross_array)
    tax_array = request.GET.get('tax', '[]')
    taxarray = json.loads(tax_array)
    amount_array = request.GET.get('amount', '[]')
    amountarray = json.loads(amount_array)
    address=''
    taxregno=''
    product = Tblmnuseetings.objects.get()
    if product.printheaderimage:
        print("Image uploaded")
        headerimg=product.printheaderimage
        
    else:
        headerimg=None
        print("No image uploaded")
    if product.printfooterimage:
        print("Image uploaded")
        footerimg=product.printfooterimage
        
    else:
        footerimg=None
        print("No image uploaded")
        

    if cus!='CASH' and cus!='CREDIT':
        led=Tblaccountledger.objects.get(lname=cus,company=company)
        address=led.address
        taxregno=led.taxregno
        print(address)

    if vtype=='SS':
        password = request.GET.get('pass')
        imei = request.GET.get('imei')
        apddate = request.GET.get('apdate')
        battery = request.GET.get('battery')
        bcid = request.GET.get('bcid')
        fcid = request.GET.get('fcid')
        mmcid = request.GET.get('mmcid')
        sim = request.GET.get('sim')
        charger = request.GET.get('charger')
        ns = request.GET.get('ns')
        mnw = request.GET.get('mnw')
        snw = request.GET.get('snw')
        nc = request.GET.get('nc')
        cnw = request.GET.get('cnw')
        fnw = request.GET.get('fnw')
        knw = request.GET.get('knw')
        np = request.GET.get('np')
        lcd = request.GET.get('lcd')

    
    if printtype=='a4':
        if vtype=='SS':
            
            return render(request,'print.html',{'vno':vno,'mobile':mobile, 'customer':cus,'dates':date,'itemname':itemarray,
                    'qty':qtyarray,'price':pricearray,'gross':grossarray,'tax':taxarray,'amount':amountarray,'address':address,
                    'taxregno':taxregno,'company':company,'taxamt':taxamt,'totalamt':totalamt,'vtype':vtype,
                    'password':password,'imei':imei,'apdate':apddate,'battery':battery,'bcid':bcid,'fcid':fcid,'mmcid':mmcid,
                    'ns':ns,'np':np,'nc':nc,'sim':sim,'charger':charger,'mnw':mnw,'cnw':cnw,'snw':snw,'knw':knw,'fnw':fnw, 'lcd':lcd})
        else:
           

    
            return render(request,'print.html',{'vno':vno,'mobile':mobile, 'customer':cus,'dates':date,'itemname':itemarray,
                    'qty':qtyarray,'price':pricearray,'gross':grossarray,'tax':taxarray,'amount':amountarray,'address':address,
                    'taxregno':taxregno,'company':company,'taxamt':taxamt,'totalamt':totalamt,'vtype':vtype,'title':title,
                    'header_img':headerimg,'footer_img':footerimg,'headerchk':headerchk,'footerchk':footerchk})
    else:
        return render(request,'thermalprint.html',{'vno':vno,'mobile':mobile, 'customer':cus,'dates':date,'itemname':itemarray,
                'qty':qtyarray,'price':pricearray,'gross':grossarray,'tax':taxarray,'amount':amountarray,'address':address,
                'taxregno':taxregno,'company':company,'taxamt':taxamt,'totalamt':totalamt,'slang':slangarray,'vtype':vtype,'title':title})
  
@login_required(login_url='login')
def barcodeprint(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    return render(request,'barcode.html',{'user':company,'cuser':user,'area':area})
@login_required(login_url='login')
def barcodeprintview(request):
    iname = request.GET.get('iname')
    bcode = request.GET.get('bcode')
    
    mrp = request.GET.get('mrp')
    srate = request.GET.get('srate')
    if mrp=='':
        mrp='0.00'
    if srate=='':
        srate='0.00'
    return render(request,'printbarcode.html',{'iname':iname,'bcode':bcode,'mrp':mrp,'srate':srate})

@login_required(login_url='login')
def editwindow(request):
    comp=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    return render(request,'edit.html',{'user':comp,'cuser':user,'area':area})
@login_required(login_url='login')
def getedititems(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    query=request.GET.get('query')
    if query=='itemcateg':
        getdata=Tblitemcategory.objects.filter(company=company)
        data = [{'id': getdataitem.categoryid, 'name': getdataitem.categoryname,'remarks':getdataitem.remarks} for getdataitem in getdata]

    elif query=='item':
        
        getdata=Tblitemmaster.objects.filter(company=company)
      
        data = [{'id': getdataitem.itemid, 'name': getdataitem.itemname,'itemcode':getdataitem.itemcode,'itemnote':getdataitem.itemnote,'ilang': getdataitem.ilang,'bcode':getdataitem.bcode,'srate':getdataitem.srate,'prate':getdataitem.prate,'vat':getdataitem.vat,'incs':getdataitem.incs,'categid':getdataitem.categoryid} for getdataitem in getdata]

    elif query=='accountgroup':
        getdata=Tblaccgroup.objects.filter(Q(company=company) | Q(company=None))
        data = [{'id': getdataitem.agroupid, 'name': getdataitem.agroupname} for getdataitem in getdata]

    elif query=='ledger':
        getdata=Tblaccountledger.objects.filter(Q(company=company) )
        data = [{'lid': getdataitem.lid, 'lname': getdataitem.lname,'address':getdataitem.address,'phone': getdataitem.phone,'mobile':getdataitem.mobile,'taxregno':getdataitem.taxregno,'area':getdataitem.area} for getdataitem in getdata]

    elif query=='customer':
        getdata=Tblaccountledger.objects.filter(agroupid=18,company=company)
        data = [{'lid': getdataitem.lid, 'lname': getdataitem.lname,'address':getdataitem.address,'phone': getdataitem.phone,'mobile':getdataitem.mobile,'taxregno':getdataitem.taxregno,'area':getdataitem.area} for getdataitem in getdata]

    elif query=='supplier':
        getdata=Tblaccountledger.objects.filter(agroupid=19,company=company)
        data = [{'lid': getdataitem.lid, 'lname': getdataitem.lname,'address':getdataitem.address,'phone': getdataitem.phone,'mobile':getdataitem.mobile,'taxregno':getdataitem.taxregno,'area':getdataitem.area} for getdataitem in getdata]
    elif query=='area':
        getdata=Tbldepot.objects.filter(Q(company=company) )
        data = [{'dcode': getdataitem.dcode, 'name': getdataitem.dname} for getdataitem in getdata]
    elif query=='user':
        getdata=Tbluserdetails.objects.filter(Q(company=company,area=area) )
        data = [{'id': getdataitem.userid, 'name': getdataitem.username,'group':getdataitem.ugroup} for getdataitem in getdata]
    elif query=='job':
        getdata=Tbljob.objects.filter(Q(company=company) )
        data = [{'id': getdataitem.jid, 'name': getdataitem.name,'iqama':getdataitem.iqamano, 'country': getdataitem.country,'phone':getdataitem.mobile, 'whatsapp': getdataitem.whatsappno,'category':getdataitem.wcategoryid} for getdataitem in getdata]
    elif query=='jobcateg':
        getdata=Tblworkcategory.objects.filter(Q(company=company) )
        data = [{'id': getdataitem.wid, 'category': getdataitem.wcategory} for getdataitem in getdata]
    elif query=='SI':
        getdata=Tblbusinessissue.objects.filter(Q(company=company,issuetype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.issuedate,'amount': getdataitem.amt, 'party': getdataitem.ledcodedr} for getdataitem in getdata]
    elif query=='PI' :
        getdata=TblTransactionReceipt.objects.filter(Q(company=company,recpttype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.recptdate,'amount': getdataitem.amt, 'party': getdataitem.ledcodecr} for getdataitem in getdata]
    elif query=='PR':
        getdata=Tblbusinessissue.objects.filter(Q(company=company,issuetype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.issuedate,'amount': getdataitem.amt, 'party': getdataitem.ledcodecr} for getdataitem in getdata]
    elif query=='SR':
        getdata=TblTransactionReceipt.objects.filter(Q(company=company,recpttype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.recptdate,'amount': getdataitem.amt, 'party': getdataitem.ledcodecr} for getdataitem in getdata]
    elif query=='SS':
        getdata=Tblbusinessissue.objects.filter(Q(company=company,issuetype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.issuedate,'amount': getdataitem.amt, 'party': getdataitem.ledcodedr} for getdataitem in getdata]
   
    elif query=='P':
        getdata = Tblgeneralledger.objects.values('vno').filter(Q(company=company,vtype=query) ) \
        .annotate(
            date=F('vdate'),  # This will return the vdate as-is, but you'll need to handle multiple dates per vno
            amount=Sum( F('cramt')),  # Sum of dbamt - cramt
            narration=F('naration')  # If there's a null note, it will default to an empty string
        ) \
        .order_by('vno')

        data = list(getdata)
    elif query=='R':
        getdata = Tblgeneralledger.objects.values('vno').filter(Q(company=company,vtype=query) ) \
        .annotate(
            date=F('vdate'),  # This will return the vdate as-is, but you'll need to handle multiple dates per vno
            amount=Sum( F('dbamt')),  # Sum of dbamt - cramt
            narration=F('naration')  # If there's a null note, it will default to an empty string
        ) \
        .order_by('vno')

        data = list(getdata)
    
    else:
        return redirect('/')
    return JsonResponse({'data':data})


@login_required(login_url='login')
def getitemcateg(request):
    comp = request.GET.get('comp')
    u=Tblusermaster.objects.get(companyname=comp)
    company=company=request.session.get('company')
    
    idd=request.GET.get('categid')
    ic=Tblitemcategory.objects.get(categoryid=idd,company=company)
    data = [{'id': ic.categoryid, 'name': ic.categoryname}]
    return JsonResponse({'data':data})


@login_required(login_url='login')
def deleteedititem(request):
    company=request.session.get('company')
    
    
    idd=request.GET.get('modeid')
    mode=request.GET.get('mode')
    if mode=='icateg':

        delit=Tblitemcategory.objects.filter(categoryid=idd,company=company)
        delit.delete()
    elif mode=='item':
        delit=Tblitemmaster.objects.filter(itemid=idd,company=company)
        delit.delete()
        delit=Tblbatch.objects.filter(itemid=idd,company=company)
        delit.delete()
    elif mode=='ledgroup':
        delit=Tblaccgroup.objects.filter(agroupid=idd,company=company)
        delit.delete()
    elif mode=='ledger' or mode=='cus' or mode=='sup':
        delit=Tblaccountledger.objects.filter(lid=idd,company=company)
        delit.delete()
        delit=Tblgeneralledger.objects.filter(ledcode=idd,company=company,vtype='OB')
        delit.delete()
    elif mode=='area':
        delit=Tbldepot.objects.filter(dcode=idd,company=company)
        delit.delete()
    elif mode=='user':
        delit=Tbluserdetails.objects.filter(userid=idd,company=company)
        delit.delete()
    elif mode=='job':
        delit=Tbljob.objects.filter(jid=idd,company=company)
        delit.delete()
    elif mode=='jobcateg':
        delit=Tblworkcategory.objects.filter(wid=idd,company=company)
        delit.delete()
    elif mode=='SI':
        print(mode)
        delissue = Tblissuedetails.objects.filter(issuecode=idd,vtype=mode,company=company)
        delissue.delete()
        delbissue = Tblbusinessissue.objects.filter(vno=idd,issuetype=mode,company=company)
        delbissue.delete()
        delinv = Tblinventory.objects.filter(vcode=idd,sales__gt=0,company=company)
        delinv.delete()
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    elif mode=='SS':
        print(mode)
        delissue = Tblissuedetails.objects.filter(issuecode=idd,vtype=mode,company=company)
        delissue.delete()
        delbissue = Tblbusinessissue.objects.filter(vno=idd,issuetype=mode,company=company)
        delbissue.delete()
        delinv = Tblinventory.objects.filter(vcode=idd,sales__gt=0,company=company)
        delinv.delete()
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    elif mode=='SR':
        print(mode)
        deltr = TblTransactionReceipt.objects.filter(recptcode=idd,recpttype=mode,company=company)
        deltr.delete()
        delrd = Tblreceiptdetails.objects.filter(recptcode=idd,vtype=mode,company=company)
        delrd.delete()
        delinv = Tblinventory.objects.filter(vcode=idd,sr__gt=0,company=company)
        delinv.delete()
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    elif mode=='PR':
        print(mode)

        delissue = Tblissuedetails.objects.filter(issuecode=idd,vtype=mode,company=company)
        delissue.delete()
        delbissue = Tblbusinessissue.objects.filter(vno=idd,issuetype=mode,company=company)
        delbissue.delete()
        delinv = Tblinventory.objects.filter(vcode=idd,pr__gt=0,company=company)
        delinv.delete()
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    elif mode=='PI':
        print(mode)
        deltr = TblTransactionReceipt.objects.filter(recptcode=idd,recpttype=mode,company=company)
        deltr.delete()
        delrd = Tblreceiptdetails.objects.filter(recptcode=idd,vtype=mode,company=company)
        delrd.delete()
        delinv = Tblinventory.objects.filter(vcode=idd,purchase__gt=0,company=company)
        delinv.delete()
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    elif mode=='P':
        
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    elif mode=='R':
        
        delinv = Tblgeneralledger.objects.filter(vno=idd,vtype=mode,company=company)
        delinv.delete()
    return HttpResponse('<script type="text/javascript">window.close()</script>') 



def getusers(request):
    type=request.GET.get('type')
    uid=request.GET.get('uid')
    area=request.GET.get('area')
    

   
    if type!='edit':
        query=request.GET.get('query')
        com=Tbluserdetails.objects.filter(Q(company=query,area=area)|Q(company=query,area=None))
        
        data = [{'name':usr.username} for usr in com]
    else:
        company=request.GET.get('comp')
        com=Tbluserdetails.objects.get(company=company,userid=uid)
        data = [{'id':com.userid,'name':com.username,'ugroup':com.ugroup,'password':com.upassword,'status':com.astatus}]
        

    return JsonResponse({'data':data})

def getarea(request):
    type=request.GET.get('type')
    query=request.GET.get('query')
    company=request.session.get('company')
    
    
    if type!='edit':
        
        com=Tbldepot.objects.filter(company=query)
        
        data = [{'name':area.dname,'dcode':area.dcode} for area in com]
    else:
        
        com=Tbldepot.objects.get(dcode=query,company=company)
    
        data = [{'name':com.dname,'dcode':com.dcode,'address':com.address,'pin':com.pin,'city':com.city,'phone':com.phoneno,'mobile':com.mobile,
                 'cperson':com.cperson,'regno':com.regno,'license': com.lescenseno,'desc':com.description}]

    
    return JsonResponse({'data':data})
@login_required(login_url='login')
def getmaxvno(request):
    type=request.GET.get('type')
    company=request.session.get('company')
    
    if type=='SS':
        a=Tblbusinessissue.objects.filter(company=company,issuetype='SS')
        if len(a)==0:
            vno=1
        else:

            vno = Tblbusinessissue.objects.filter(company=company,issuetype='SS').aggregate(max=Max('issuecode'))["max"] +1
    if type=='SI':
        a=Tblbusinessissue.objects.filter(company=company,issuetype='SI')
        if len(a)==0:
            vno=1
        else:

            vno = Tblbusinessissue.objects.filter(company=company,issuetype='SI').aggregate(max=Max('issuecode'))["max"] +1
    elif type=='PI':
        a=TblTransactionReceipt.objects.filter(company=company,recpttype='PI')
        if len(a)==0:
            vno=1
        else:
            vno = TblTransactionReceipt.objects.filter(company=company,recpttype='PI').aggregate(max=Max('recptcode'))["max"] +1
    elif type=='SR':
        print(company)
        a= TblTransactionReceipt.objects.filter(company=company,recpttype='SR')
        if len(a)==0:
            vno=1
        else:
            vno = TblTransactionReceipt.objects.filter(company=company,recpttype='SR').aggregate(max=Max('recptcode'))["max"] +1
    elif type=='PR':
        a= Tblbusinessissue.objects.filter(company=company,issuetype='PR')
        if len(a)==0:
            vno=1
        else:

            vno = Tblbusinessissue.objects.filter(company=company,issuetype='PR').aggregate(max=Max('issuecode'))["max"] +1
    if type=='SO':
        a=Tblbusinessissue.objects.filter(company=company,issuetype='SO')
        if len(a)==0:
            vno=1
        else:

            vno = Tblbusinessissue.objects.filter(company=company,issuetype='SO').aggregate(max=Max('issuecode'))["max"] +1
    elif type=='PO':
        print(company)
        a= TblTransactionReceipt.objects.filter(company=company,recpttype='PO')
        if len(a)==0:
            vno=1
        else:
            vno = TblTransactionReceipt.objects.filter(company=company,recpttype='PO').aggregate(max=Max('recptcode'))["max"] +1
    elif type=='P':
        a=Tblgeneralledger.objects.filter(vtype='P',company=company)
        if len(a)==0:
            vno=1
        else:
            vno =Tblgeneralledger.objects.filter(vtype='P',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    elif type=='R':
        a=Tblgeneralledger.objects.filter(vtype='R',company=company)
        if len(a)==0:
            vno=1
        else:
            vno =Tblgeneralledger.objects.filter(vtype='R',company=company).aggregate(max=Max(Cast('vno', IntegerField())))["max"] + 1
    elif type=='item':
        a=Tblitemmaster.objects.filter(company=company)
        if len(a)==0:
            vno=1
        else:
            vno =Tblitemmaster.objects.filter(company=company).aggregate(max=Max(Cast('itemid', IntegerField())))["max"] + 1
   
    return JsonResponse({'vno':vno})

@login_required(login_url='login')
def createvalidation(request):
    type=request.GET.get('type')
    query=request.GET.get('query')
    
    company=request.session.get('company')
    
    if type=='item':
        i=Tblitemmaster.objects.filter(company=company,bcode=query)
        data=len(i)
    if type=='itemcateg':
        i=Tblitemcategory.objects.filter(company=company,categoryname=query)
        data=len(i)
    if type=='ledgrp':
        i=Tblaccgroup.objects.filter(company=company,agroupname=query)
        data=len(i)
    if type=='ledger':
        i=Tblaccountledger.objects.filter(company=company,lname=query)
        data=len(i)
    if type=='area':
        i=Tbldepot.objects.filter(company=company,dname=query)
        data=len(i)
    if type=='user':
        i=Tbluserdetails.objects.filter(company=company,username=query)
        data=len(i)
    if type=='job':
        i=Tbljob.objects.filter(company=company,name=query)
        data=len(i)      
        
    return JsonResponse({'data':data})
def jobcard(request):
    return render(request,'jobform.html')
@login_required(login_url='login')
def jobcard(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
   
    
    preid = request.GET.get('itemid')
    type = request.GET.get('type')
   
    itid=0
    itidmain=0
    # icateg=Tblitemcategory.objects.all()
   
    a = Tbljob.objects.filter(company=company)
    amain = Tbljob.objects.all()
    if len(amain) ==0:
        jidmain=1
    else:
        jidmain = Tbljob.objects.aggregate(max=Max('jidmain'))["max"] + 1

    
    if len(a) == 0:
        itid = 1
        

    else:
        itid = Tbljob.objects.filter(company=company).aggregate(max=Max('jid'))["max"] + 1
        
    

    itemc=Tblworkcategory.objects.filter(Q(company=company)|Q(company=None))
    cntry=countries
    print(len(itemc))
    if len(itemc) == 0:
        itemc2='None'
    else:
        itemc2=itemc
    if preid==None:
        preid='empt'

    if request.method =='POST':
        jidpg=request.POST['itemid']

        name=request.POST['name']
        iqama=request.POST['iqama']
        mail=request.POST['mail']
        country=request.POST['country']
        note=request.POST['note']
        workcategory=request.POST [ 'wcategory' ]
        mobile=request.POST [ 'mobile' ]
        whatsapp=request.POST [ 'whatsapp' ]
        edittype=request.POST [ 'edittype' ]

        
        
        
        if mobile == '':
            mobile=0
        if whatsapp == '':
            whatsapp=0
        



        if name!="":
            
            
            
            
            deljob = Tbljob.objects.filter(jid=jidpg,company=company)
            deljob.delete()


            job=Tbljob.objects.create(jid=jidpg,jidmain=jidmain,name=name,note=note,iqamano=iqama,wcategoryid=workcategory,
                                mobile=mobile,country=country,whatsappno=whatsapp,email=mail,company=company 
                                )
            job.save()
            
           
            

            if edittype=='edit':
                return HttpResponse('<script type="text/javascript">window.close()</script>')  

            else:

                return redirect('/jobcard/?comp='+company+'&user='+user+'&area='+area+'')
            


        else:
            messages.info(request,"Please enter itemname")
    
    return render(request,'jobform.html',{'categ':itemc2,'country':cntry, 'itemidd':itid,'preid':preid,'type':type,'user':company,'cuser':user,'area':area})

@login_required(login_url='login')
def workcategory(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    
    preid = request.GET.get('itemid')
    type = request.GET.get('type')
    
    cname=''
    remark=''

    if preid!=None:
        ic=Tblworkcategory.objects.get(company=company, wid=preid)
        cname=ic.wcategory
        
        cidmain=ic.widmain

    
    cid=1

    a=Tblworkcategory.objects.filter(company=company)

    amain=Tblworkcategory.objects.all()
    if len(amain)==0:
        cidmain=1

    else:
        cidmain= Tblworkcategory.objects.aggregate(max=Max('widmain'))["max"]+1
    if len(a)==0:
        cid=1

    else:
        cid= Tblworkcategory.objects.filter(company=company).aggregate(max=Max('wid'))["max"]+1
    
    if request.method == 'POST':
        name = request.POST['categname']
        
        catid = request.POST['categid']
        cmain = request.POST['cm']
        edittype=request.POST [ 'edittype' ]
        print()
        if (name!=""):
            delitem = Tblworkcategory.objects.filter(wid=catid,company=company)
            delitem.delete()
            categ = Tblworkcategory.objects.create(wid=catid,widmain=cmain,wcategory=name,company=company)
            categ.save()
            messages.info(request, "success")
            if edittype=='edit':
                return HttpResponse('<script type="text/javascript">window.close()</script>') 
            else:
                return redirect('/workcateg/?comp='+company+'&user='+user+'&area='+area+'')
            # return render(request, 'itemcategory.html', {'cid': cid})


        else:

            messages.info(request, "Please enter category name")

    return render(request,'workcategory.html',{'cid':cid,'cname':cname,'preid':preid,'cidmain':cidmain ,'remark':remark,'type':type,'user':company,'cuser':user,'area':area})
@login_required(login_url='login')
def getwrkcateg(request):
    comp=request.session.get('company')
    
    idd = request.GET.get('categid')
    ic=Tblworkcategory.objects.get(wid=idd,company=comp)
    data = [{'id': ic.wid, 'name': ic.wcategory}]
    return JsonResponse({'data':data})
def getjob(request):

    company = request.GET.get('comp')
    
    itype = request.GET.get('type')
    query = request.GET.get('query')
    # itemids=int(query)
    
    customers = Tbljob.objects.get(jid=query,company=company)
    categ=Tblworkcategory.objects.get(wid=customers.wcategoryid,company=company)
    data = [{'id': customers.jid, 'name': customers.name,'note':customers.note,'cid':customers.wcategoryid,'country': customers.country,'email':customers.email,
             'mobile':customers.mobile,'whatsapp':customers.whatsappno,'iqama':customers.iqamano,'category': categ.wcategory} ]
    return JsonResponse({'customers': data})
    return render(request,'edit.html',{'user':comp,'cuser':user,'area':area})
@login_required(login_url='login')
def editsearch(request):
    company=request.session.get('company')
    user=request.session.get('cur_user')
    area=request.session.get('area')
    searchkey = request.GET.get('search')
    
    query=request.GET.get('query')
    if query=='itemcateg':
        getdata=Tblitemcategory.objects.filter(Q(company=company,categoryname__icontains=searchkey) )
        data = [{'id': getdataitem.categoryid, 'name': getdataitem.categoryname,'remarks':getdataitem.remarks} for getdataitem in getdata]

    elif query=='item':
        
        getdata=Tblitemmaster.objects.filter(Q(company=company,itemname__icontains=searchkey) )
      
        data = [{'id': getdataitem.itemid, 'name': getdataitem.itemname,'itemcode':getdataitem.itemcode,'itemnote':getdataitem.itemnote,'ilang': getdataitem.ilang,'bcode':getdataitem.bcode,'srate':getdataitem.srate,'prate':getdataitem.prate,'vat':getdataitem.vat,'incs':getdataitem.incs,'categid':getdataitem.categoryid} for getdataitem in getdata]

    elif query=='accountgroup':
        getdata=Tblaccgroup.objects.filter(Q(company=company,agroupname__icontains=searchkey) | Q(company=None,agroupname__icontains=searchkey))
        data = [{'id': getdataitem.agroupid, 'name': getdataitem.agroupname} for getdataitem in getdata]

    elif query=='ledger':
        getdata=Tblaccountledger.objects.filter(Q(company=company,lname__icontains=searchkey))
        data = [{'lid': getdataitem.lid, 'lname': getdataitem.lname,'address':getdataitem.address,'phone': getdataitem.phone,'mobile':getdataitem.mobile,'taxregno':getdataitem.taxregno,'area':getdataitem.area} for getdataitem in getdata]

    elif query=='customer':
        getdata=Tblaccountledger.objects.filter(Q(company=company,agroupid=18,lname__icontains=searchkey) )
        data = [{'lid': getdataitem.lid, 'lname': getdataitem.lname,'address':getdataitem.address,'phone': getdataitem.phone,'mobile':getdataitem.mobile,'taxregno':getdataitem.taxregno,'area':getdataitem.area} for getdataitem in getdata]

    elif query=='supplier':
        getdata=Tblaccountledger.objects.filter(Q(company=company,agroupid=19,lname__icontains=searchkey) )
        data = [{'lid': getdataitem.lid, 'lname': getdataitem.lname,'address':getdataitem.address,'phone': getdataitem.phone,'mobile':getdataitem.mobile,'taxregno':getdataitem.taxregno,'area':getdataitem.area} for getdataitem in getdata]
    elif query=='area':
        getdata=Tbldepot.objects.filter(Q(company=company,dname__contains=searchkey) )
        data = [{'dcode': getdataitem.dcode, 'name': getdataitem.dname} for getdataitem in getdata]
    elif query=='user':
        getdata=Tbluserdetails.objects.filter(Q(company=company,area=area,username__icontains=searchkey)  )
        data = [{'id': getdataitem.userid, 'name': getdataitem.username,'group':getdataitem.ugroup} for getdataitem in getdata]
    elif query=='job':
        getdata=Tbljob.objects.filter(Q(company=company,name__icontains=searchkey) )
        data = [{'id': getdataitem.jid, 'name': getdataitem.name,'iqama':getdataitem.iqamano, 'country': getdataitem.country,'phone':getdataitem.mobile, 'whatsapp': getdataitem.whatsappno,'category':getdataitem.wcategoryid} for getdataitem in getdata]
    elif query=='jobcateg':
        getdata=Tblworkcategory.objects.filter(Q(company=company,wcategory__icontains=searchkey) )
        data = [{'id': getdataitem.wid, 'category': getdataitem.wcategory} for getdataitem in getdata]
    elif query=='SI' or query=='SS':
        getdata=Tblbusinessissue.objects.filter(Q(company=company,vno__icontains=searchkey,issuetype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.issuedate,'amount': getdataitem.amt, 'party': getdataitem.ledcodedr} for getdataitem in getdata]
    elif query=='PI' :
        getdata=TblTransactionReceipt.objects.filter(Q(company=company,vno__icontains=searchkey,recpttype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.recptdate,'amount': getdataitem.amt, 'party': getdataitem.ledcodecr} for getdataitem in getdata]
    elif query=='PR':
        getdata=Tblbusinessissue.objects.filter(Q(company=company,vno__icontains=searchkey,issuetype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.issuedate,'amount': getdataitem.amt, 'party': getdataitem.ledcodecr} for getdataitem in getdata]
    elif query=='SR':
        getdata=TblTransactionReceipt.objects.filter(Q(company=company,vno__icontains=searchkey,recpttype=query) )
        data = [{'vno': getdataitem.vno, 'date': getdataitem.recptdate,'amount': getdataitem.amt, 'party': getdataitem.ledcodecr} for getdataitem in getdata]
    elif query=='P':
        getdata = Tblgeneralledger.objects.values('vno').filter(Q(company=company,vtype=query,vno__icontains=searchkey,) ) \
        .annotate(
            date=F('vdate'),  # This will return the vdate as-is, but you'll need to handle multiple dates per vno
            amount=Sum( F('dbamt')),  # Sum of dbamt - cramt
            narration=F('naration')  # If there's a null note, it will default to an empty string
        ) \
        .order_by('vno')

        data = list(getdata)
    elif query=='R':
        getdata = Tblgeneralledger.objects.values('vno').filter(Q(company=company,vtype=query,vno__icontains=searchkey,) ) \
        .annotate(
            date=F('vdate'),  # This will return the vdate as-is, but you'll need to handle multiple dates per vno
            amount=Sum( F('cramt')),  # Sum of dbamt - cramt
            narration=F('naration')  # If there's a null note, it will default to an empty string
        ) \
        .order_by('vno')

        data = list(getdata)
    else:
        return redirect('/')
    return JsonResponse({'data':data})

# convert english to arabic

def translate_text(request):
    # Get the text to be translated from the request parameters
    text_to_translate = request.GET.get('arabic', '')

    if text_to_translate:
        try:
            url = f'https://api.mymemory.translated.net/get?q={text_to_translate}&langpair=en|ar'
            response = requests.get(url)
            data = response.json()

            return JsonResponse({'engtext': data['responseData']['translatedText']})

        except Exception as e:
            # If any error occurs, return an error message
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'No text provided to translate'}, status=400)

def getallitemcateg(request):
    company = request.session.get('company')
    itemc = Tblitemcategory.objects.filter(Q(company=company) | Q(company=None))

    # Check if any categories are found
    if itemc.exists():
        itemc2 = itemc
    else:
        itemc2 = None

    # Safely generate the response data
    data = [{'name': itemcateg.categoryname, 'categid': itemcateg.categoryid} for itemcateg in (itemc2 or [])]
    return JsonResponse(data, safe=False)
def setproduct(request):
    company = request.session.get('company')
    pset=Tblproductset.objects.all()
    if len(pset)==0:
        productid=1

    else:
        productid= Tblproductset.objects.filter(company=company).aggregate(max=Max('pid'))["max"]+1
    ititem= Tblitemmaster.objects.filter(company=company,itemclass='Finished product')
    
    if request.method == 'POST':
        pid = request.POST['vno']
        lcharge = request.POST['lc']
        fpid = request.POST['fp']
        
        item=Tblitemmaster.objects.get(company=company,itemid=fpid)
        itemnamemaster=item.itemname
        print(itemnamemaster)
        itemname = request.POST.getlist('itemname')
      
        
        srate = request.POST.getlist('srate')
        
        qty = request.POST.getlist('qty')
        
        itemid = request.POST.getlist('itemid')
            
        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        finalrate=0
        for i in range(itemrange):
            
            itemnamef = itemname[i]
            if itemnamef!='':
                
                
                sratef = srate[i]
                qtyf = qty[i]
                itemidf = itemid[i]
                finalqty=float( qtyf)+finalqty
                finalrate=float( sratef)+finalrate
                pdetail = Tblproductsetdetails.objects.create( pid=pid,company=company,slno=i,qty=qtyf,rate=sratef,item=itemidf)
                pdetail.save()
                
                nullchk=1
                
            
        if nullchk==1:
            pset = Tblproductset.objects.create(pid=pid,tblproddetails=pdetail,itemname=itemnamemaster,company=company,item=fpid,qty=finalqty,mrate=finalrate)
            pset.save()

             
            

            
            
        return redirect('/setproduct')
    return render(request,'setproduct.html',{'itemlist':ititem,'pid':productid})
def finishedproduct(request):
    company = request.session.get('company')
    today = datetime.datetime.now()
    curtime=today.strftime("%Y-%m-%dT%H:%M")
    pset=Tblrepacking.objects.all()
    if len(pset)==0:
        productid=1

    else:
        productid= Tblrepacking.objects.filter(company=company).aggregate(max=Max('vno'))["max"]+1
    if request.method == 'POST':
        invno = request.POST['invoice-number']
        lcharge = request.POST['labourcharge']
        prodid = request.POST['productid']
        cdate = request.POST['date']
        packdate = request.POST['packdate']
        rowcost = request.POST['rowcost']
        packcost = request.POST['packedcost']
        costfactor = request.POST['costfactor']
        
        customer = request.POST['customer']
        itemcoderepack = request.POST['itemcodepset']
        itemnamerepack = request.POST['itemnamepset']
        qtypack = request.POST['qtypset']
        cratepack = request.POST['cratepset']
        pratepack = request.POST['pratepset']
        sratepack = request.POST['sratepset']
        mrppack = request.POST['mrppset']
        amtpack = request.POST['amtpset']
        itemidpack = request.POST['itemidpset']
        
        
        if costfactor=='':
            costfactor=0
        if lcharge=='':
            lcharge=0
        
        itemname = request.POST.getlist('itemname')
        itemcode = request.POST.getlist('itemcode')
        prate = request.POST.getlist('prate')
        crate = request.POST.getlist('crate')
        srate = request.POST.getlist('srate')
        qty = request.POST.getlist('qty')
        mrp = request.POST.getlist('mrp')
        amt = request.POST.getlist('amt')
        itemid = request.POST.getlist('itemid')
            
        itemrange = len(itemname)
        nullchk=0
        finalqty=0
        finalrate=0
        for i in range(itemrange):
            
            itemnamef = itemname[i]
            if itemnamef!='':
                
                itemcodef = itemcode[i]
                qtyf = Decimal(qty[i]) if qty else Decimal('0.00')
                pratef = Decimal(prate[i]) if prate else Decimal('0.00')
                sratef = Decimal(srate[i]) if srate else Decimal('0.00')
                # mrpf = float(mrp[i])
                amtf = Decimal(amt[i]) if amt else Decimal('0.00')
                itemidf =float( itemid[i])
                cratef=crate[i] if crate != '' else 0
                finalqty=float( qtyf)+finalqty
                finalrate=float( sratef)+finalrate
                print(qtyf)
                print(itemidf)
                packingdetail = Tblrepackingdetails.objects.create( vno=invno,company=company,slno=i,itemid=itemidf,qty=qtyf,prate=pratef,
                                                                   crate=0,srate=sratef,mrp=0,amount=amtf)
                packingdetail.save()
                
                nullchk=1
                
            
        if nullchk==1:
            packing = Tblrepacking.objects.create(vno=invno,tblrepackdetails=packingdetail,vdate=cdate,company=company,
                                                  packdate=packdate,narration=finalqty,itemid=prodid,qty=qtypack,
                                                  prate=pratepack,crate=0,srate=sratepack,mrp=0,amount=amtpack,
                                                  labourcharge=lcharge,costfactor=costfactor,depoid=0)
            packing.save()

             
            

            
            
        return redirect('/finishproduct')
    return render(request,'finishedproduct.html',{'pid':productid,'curdate':curtime})
def get_previousproductset(request):
    company=request.session.get('company')
    
    query = request.GET.get('query', '')
    pset = Tblproductset.objects.filter(pid=query,company=company)
    


    pdetail = Tblproductsetdetails.objects.filter(pid=query,company=company)
    
    
    


    
    issudata = [{'pid': items.pid,'itemid':items.item} for items in pset]
    
   
    bdata = [{'pid': bitems.pid,'item':bitems.item,'qty': bitems.qty,'rate':bitems.rate} for bitems in pdetail]
    print(issudata)
    data={"data1":bdata,"data2":issudata}
  
    
    return JsonResponse(data)
def getmaxproductid(request):
        company=request.session.get('company')
        a=Tblproductset.objects.filter(company=company)
        if len(a)==0:
            vno=1
        else:

            vno = Tblproductset.objects.filter(company=company).aggregate(max=Max('pid'))["max"] +1
        return JsonResponse({'vno':vno})
def searchproductset(request):
    company=request.session.get('company')
    
    query = request.GET.get('query', '')
    plist = Tblproductset.objects.filter(itemname__icontains=query,company=company)
    getdata = [{'pid': items.item,'name':items.itemname,'vno':items.pid} for items in plist]
    
   

    print(getdata)
    data={"data":getdata}
  
    
    return JsonResponse(data)
def get_finishedproduct(request):
    company=request.session.get('company')
    
    query = request.GET.get('query', '')
    repack = Tblrepacking.objects.filter(vno=query,company=company)
    


    repackdetail = Tblrepackingdetails.objects.filter(vno=query,company=company)
    
    
    


    
    repackdata = [{'vno': items.vno,'narration': items.narration,'itemid':items.itemid,'prate': items.prate,'srate':items.srate,'vdate': items.vdate,'packdate':items.packdate,'qty': items.qty,'amount':items.amount,'labourcharge': items.labourcharge,'costfactor':items.costfactor} for items in repack]
    
   
    detaildata = [{'vno': items.vno,'item':items.itemid,'rate': items.prate,'srate':items.srate,'qty': items.qty,'amount':items.amount} for items in repackdetail]
   
    data={"data1":repackdata,"data2":detaildata}
    return JsonResponse(data)
def software_settings(request):
    company=request.session.get('company')
    
    if request.method == 'POST':
        saleid = request.POST['prevsaleedit']
        if 'printimg' in request.FILES:
    
            printhead = request.FILES['printimg']
    
        else:
            # No file was uploaded
            printhead = None 
        if 'printfootimg' in request.FILES:
    
            printfootimg = request.FILES['printfootimg']
    
        else:
            # No file was uploaded
            printfootimg = None
        
        tblmnuall=Tblmnuseetings.objects.all()
        tblmnuall.delete()
        tblmnu=Tblmnuseetings.objects.create(menuid=1,presaleedit=saleid,printheaderimage=printhead,printfooterimage=printfootimg, company=company)
        tblmnu.save()
        return redirect('/settings')
        
    return render(request,'swsettings.html')
def get_musettings(request):
    company=request.session.get('company')
    mnulist=Tblmnuseetings.objects.get(company=company)
    headerimg_url = mnulist.printheaderimage.url if mnulist.printheaderimage else None
    footerimg_url = mnulist.printfooterimage.url if mnulist.printfooterimage else None
    mnudata={'mnuid':mnulist.menuid,'saleedit':mnulist.presaleedit,'headerimg':headerimg_url,'footerimg':footerimg_url}
    return JsonResponse({'mnudata':mnudata})