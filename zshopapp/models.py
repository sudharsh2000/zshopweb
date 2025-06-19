from django.db import models

# Create your models here.
from django.db import models


from django.contrib.auth.models import AbstractUser

class Tblitemcategory(models.Model):
    categoryidmain=models.IntegerField(primary_key=True)
    categoryid=models.IntegerField(blank=True,null=True)
    categoryname=models.CharField(blank=True,null=True,max_length=50)
    remarks=models.CharField(blank=True,null=True,max_length=50)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        return self.categoryname
class Tblitemmaster(models.Model):
    itemidmain=models.IntegerField(primary_key=True)
    itemid=models.IntegerField(blank=True,null=True)
    status=models.IntegerField( blank=True, null=True)
    itemcode=models.CharField(max_length=200)
    itemname=models.CharField(max_length=200)
    categoryid=models.IntegerField( blank=True, null=True)
    description=models.CharField(max_length=200,)
    mrp=models.IntegerField( blank=True, null=True)
    srate=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    prate=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    manufacturer=models.IntegerField( blank=True, null=True)
    agentcommision=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    cooly=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    minstock=models.IntegerField( blank=True, null=True)
    reorder=models.IntegerField( blank=True, null=True)
    maximum=models.IntegerField( blank=True, null=True)
    slabid=models.IntegerField( blank=True, null=True)
    balance=models.IntegerField( blank=True, null=True)
    unit=models.TextField( blank=True, null=True)
    vat=models.DecimalField( blank=True, null=True,decimal_places=1,max_digits=10)
    cst=models.DecimalField( blank=True, null=True,decimal_places=1,max_digits=10)
    purtax=models.DecimalField( blank=True, null=True,decimal_places=1,max_digits=10)
    incs=models.IntegerField( blank=True, null=True)
    incp=models.IntegerField( blank=True, null=True)
    itemclass=models.CharField(max_length=200)
    rack=models.CharField(max_length=200, blank=True, null=True)
    crate=models.DecimalField( blank=True, null=True,decimal_places=1,max_digits=10)
    sizelessname=models.CharField(max_length=200, blank=True, null=True)
    plu=models.CharField(max_length=200, blank=True, null=True)
    unit2=models.CharField(max_length=200, blank=True, null=True)
    unitamount1=models.DecimalField( blank=True, null=True,decimal_places=1,max_digits=10)
    unitamount2=models.DecimalField( blank=True, null=True,decimal_places=1,max_digits=10)
    ledid=models.IntegerField( blank=True, null=True,)
    ilang=models.CharField(max_length=200)
    itemnote=models.CharField(max_length=200, blank=True, null=True)
    bunit=models.CharField(max_length=200, blank=True, null=True)
    usingmechine=models.IntegerField( blank=True, null=True)
    item2=models.IntegerField( blank=True, null=True)
    itemidlocal=models.IntegerField( blank=True, null=True)
    company=models.CharField(max_length=200, blank=True, null=True)
    bcode = models.CharField(max_length=200, blank=True, null=True)
    company= models.CharField(blank=True,null=True,max_length=50)
    os = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    area= models.CharField(blank=True,null=True,max_length=50)
    litid=models.IntegerField( blank=True, null=True)



    def __str__(self):
        return self.itemname

class Tblbatch(models.Model):
    bcode=models.CharField(max_length=30)
    itemidmain=models.IntegerField( blank=True, null=True)
    itemid=models.IntegerField( blank=True, null=True)
    costcenter=models.CharField(max_length=50,blank=True, null=True)
    depo=models.CharField(max_length=50,blank=True, null=True)
    bid=models.CharField( blank=True, null=True,max_length=50)
    ledcode=models.CharField(blank=True, null=True,max_length=50)
    mrp=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    srate=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    mandate=models.DateTimeField( blank=True, null=True)
    exdate=models.DateTimeField(blank=True, null=True)
    prate=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)
    unconv=models.IntegerField( blank=True, null=True)
    recptcode=models.CharField(blank=True, null=True,max_length=50)
    company=models.CharField(blank=True, null=True,max_length=50)
    computer=models.CharField(blank=True, null=True,max_length=50)
    itemid2=models.CharField(blank=True, null=True,max_length=50)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)
    crate=models.DecimalField( blank=True, null=True,decimal_places=2,max_digits=10)

    def __str__(self):
        return self.bcode
class Tblinventory(models.Model):
    dcode = models.CharField(max_length=30,blank=True, null=True)
    invdate = models.DateTimeField(blank=True, null=True)
    pcode = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    os = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    purchase = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    mr = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    sr = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    ireceipt = models.DecimalField(blank=True, null=True, decimal_places=2,max_digits=10)
    bmr = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    sales = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    ps = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    dn = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    pr = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    iissue = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    sh = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    dnr = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    dmg = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    bmi = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    freepre = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    freeiss = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    vcode = models.CharField(max_length=50,null=True,blank=True)
    ledcode = models.CharField(max_length=50,null=True,blank=True)
    costcenter = models.CharField(max_length=50,null=True,blank=True)
    batchcode = models.CharField(max_length=50,null=True,blank=True)
    slno = models.CharField(max_length=50,null=True,blank=True)
    uc = models.DecimalField(max_length=50,decimal_places=10,blank=True, null=True,max_digits=10)
    exdate = models.DateTimeField(blank=True, null=True)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        return self.dcode
class Tblaccountgroup(models.Model):
    agroupidmain=models.IntegerField(primary_key=True)
    agroupid=models.IntegerField(blank=True,null=True)
    
    agroupname=models.CharField(max_length=100)
    Aunder=models.IntegerField(blank=True,null=True)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        return  self.agroupname
class Tblaccgroup(models.Model):
    agroupidmain=models.IntegerField(primary_key=True)
    agroupid=models.IntegerField(blank=True,null=True) 
    agroupname=models.CharField(max_length=100)
    Aunder=models.IntegerField(blank=True,null=True)
    company= models.CharField(blank=True,null=True,max_length=50)  
    area= models.CharField(blank=True,null=True,max_length=50)
    def __str__(self):
        return  self.agroupname 
class Tblaccountledger(models.Model):
    lidmain = models.IntegerField(primary_key=True)
    lid = models.IntegerField(blank=True,null=True)
    lname = models.CharField(max_length=150, blank=True, null=True)
    laliasname = models.CharField(max_length=150, blank=True, null=True)
    agroupid = models.IntegerField(blank=True, null=True)
    balance = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    address = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    mobile = models.CharField(max_length=150, blank=True, null=True)
    discper = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    taxregno = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    creditdays = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    creditlimit = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    other = models.CharField(max_length=150, blank=True, null=True)
    area = models.CharField(max_length=150, blank=True, null=True)
    commission = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    cplan = models.FloatField(max_length=50,blank=True, null=True)
    lstatus =  models.IntegerField(blank=True, null=True)
    lstatus2 = models.IntegerField(blank=True, null=True)
    usecard = models.IntegerField(blank=True, null=True)
    cst = models.CharField(max_length=50,null=True,blank=True)
    cpbalance = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)


    def __str__(self):
        return self.lname
class Tblgeneralledger(models.Model):
    vdate= models.DateTimeField(blank=True, null=True)
    vtype=models.CharField(max_length=150,blank=True,null=True)
    vno=models.CharField(max_length=150,blank=True,null=True)
    tblaccountledger = models.ForeignKey(Tblaccountledger, on_delete=models.CASCADE)
    slno=models.IntegerField(blank=True,null=True)
    ledcode=models.CharField(max_length=150,blank=True,null=True)
    particulars=models.CharField(max_length=150,blank=True,null=True)
    dbamt=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    cramt=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    naration2=models.CharField(max_length=150,blank=True,null=True)
    naration=models.CharField(max_length=150,blank=True,null=True)
    refno=models.IntegerField(blank=True,null=True)
    pproject=models.IntegerField(blank=True,null=True)
    uid=models.CharField(max_length=150,blank=True,null=True)
    employee=models.CharField(max_length=150,blank=True,null=True)
    recvdamt=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    billbalance=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    discount=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    rptaxperc=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    rptaxamt=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        return self.ledcode



class Tblissuedetails(models.Model):
    issueid= models.IntegerField(primary_key=True)
    issuecode = models.IntegerField(blank=True, null=True)
    slno = models.IntegerField( blank=True, null=True)
    pcode = models.IntegerField(blank=True, null=True)
    unitid = models.IntegerField( blank=True, null=True)
    batchid = models.CharField(max_length=50,  blank=True, null=True)
    multirateid = models.IntegerField(blank=True, null=True)
    qty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    qty1 = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    qty2 = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    pnum = models.IntegerField(blank=True, null=True)
    freeqty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    rate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    crate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    discrate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    billdisc = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    taxrate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    mrp = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    taxper = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    netamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    itemnote = models.CharField(max_length=50,  blank=True, null=True)
    ledcode = models.CharField(max_length=50,  blank=True, null=True)
    vtype = models.CharField(max_length=50,  blank=True, null=True)
    ith = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    wth = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    slnotracking = models.CharField(max_length=150, blank=True, null=True)
    exdate = models.DateField(blank=True, null=True)
    itemnote2 = models.CharField(max_length=150, blank=True, null=True)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)
    def __str__(self):
        return self.issueid


class Tblbusinessissue(models.Model):
    biid=models.IntegerField(blank=True, null=True)
    opno = models.IntegerField(blank=True, null=True)
    issuecode = models.IntegerField( blank=True, null=True)
    vno = models.IntegerField(blank=True, null=True)
    issuedate = models.DateTimeField(blank=True, null=True)
    issuetype = models.CharField(max_length=50,  blank=True, null=True)
    dcode = models.CharField(max_length=50,  blank=True, null=True)
    refno = models.CharField(max_length=50,  blank=True, null=True)
    tblissuedetails = models.ForeignKey(Tblissuedetails, on_delete=models.CASCADE)
    qty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    ledcodecr = models.CharField(max_length=50,  blank=True, null=True)
    ledcodedr = models.CharField(max_length=50,  blank=True, null=True)
    amt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    empid = models.CharField(max_length=150, blank=True, null=True)
    invdisc = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    discamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    discperc=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)

    taxamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    adamount = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    cooly = models.DecimalField(max_length=50, decimal_places=10, blank=True, null=True, max_digits=10)
    agent = models.CharField(max_length=50,  blank=True, null=True)
    pvno = models.CharField(max_length=50,  blank=True, null=True)
    taxid = models.CharField(max_length=50,  blank=True, null=True)
    tename = models.CharField(max_length=50,  blank=True, null=True)
    cpdiscount = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    mpayment = models.IntegerField( blank=True, null=True)
    cashreceived = models.CharField(max_length=150, blank=True, null=True)
    SR = models.CharField(max_length=150, blank=True, null=True)
    uid = models.CharField(max_length=150, blank=True, null=True)
    pproject = models.IntegerField(blank=True, null=True)
    warranty = models.CharField(max_length=150, blank=True, null=True)
    tmobile = models.CharField(max_length=150, blank=True, null=True)
    taddress = models.CharField(max_length=150, blank=True, null=True)
    tvat = models.CharField(max_length=150, blank=True, null=True)
    vehiclenum = models.CharField(max_length=150, blank=True, null=True)
    mtrread = models.CharField(max_length=150, blank=True, null=True)
    twopayment = models.CharField(max_length=150, blank=True, null=True)
    twopayamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    lblaccnt = models.CharField(max_length=150, blank=True, null=True)
    ftable = models.CharField(max_length=150, blank=True, null=True)
    company= models.CharField(blank=True,null=True,max_length=50)
    
    area= models.CharField(blank=True,null=True,max_length=50)
    def __str__(self):
        return self.issueid

     
    
class Tblreceiptdetails(models.Model):
    rdid= models.IntegerField(primary_key=True)
    recptcode = models.IntegerField(blank=True, null=True)
    slno = models.IntegerField( blank=True, null=True)
    pcode = models.IntegerField(blank=True, null=True)
    unitid = models.IntegerField( blank=True, null=True)
    batchid = models.CharField(max_length=50,  blank=True, null=True)
    multirateid = models.IntegerField(blank=True, null=True)
    qty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    
    freeqty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    rate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    
    discrate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    billdisc = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    profit  = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    taxrate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    
    
    netamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    itemnote = models.CharField(max_length=50,  blank=True, null=True)
    itemnote1 = models.CharField(max_length=150, blank=True, null=True)
    mandate = models.DateField(blank=True, null=True)
    exdate = models.DateField(blank=True, null=True)
    srate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    crate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    mrp = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    ledcode = models.CharField(max_length=50,  blank=True, null=True)
    vtype = models.CharField(max_length=50,  blank=True, null=True)
    taxper = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    exciseduty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    wrate = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    area= models.CharField(blank=True,null=True,max_length=50)
    company= models.CharField(blank=True,null=True,max_length=50)
    
class TblTransactionReceipt(models.Model):
    trid=models.IntegerField(blank=True,null=True)
    recptdetails = models.ForeignKey(Tblreceiptdetails, on_delete=models.CASCADE)
    qty = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    recptcode = models.IntegerField( blank=True, null=True)
    vno = models.IntegerField(blank=True, null=True)
    recptdate = models.DateTimeField(blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    refno = models.CharField(max_length=50,  blank=True, null=True)
    recpttype = models.CharField(max_length=50,  blank=True, null=True)
    dcode = models.CharField(max_length=50,  blank=True, null=True)
    ledcodecr = models.CharField(max_length=50,  blank=True, null=True)
    ledcodedr = models.CharField(max_length=50,  blank=True, null=True)
    amt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    empid = models.CharField(max_length=150, blank=True, null=True)
    invdisc = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    discamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    discperc=models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)

    taxamt = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    
    cooly = models.DecimalField(max_length=50, decimal_places=10, blank=True, null=True, max_digits=10)
    adamount = models.DecimalField(max_length=50, decimal_places=2, blank=True, null=True, max_digits=10)
    agent = models.CharField(max_length=50,  blank=True, null=True)
    pvno = models.CharField(max_length=50,  blank=True, null=True)
    taxid = models.CharField(max_length=50,  blank=True, null=True)
    tename = models.CharField(max_length=50,  blank=True, null=True)
    
    mpayment = models.IntegerField( blank=True, null=True)

    srate = models.CharField(max_length=150, blank=True, null=True)
    crate = models.CharField(max_length=150, blank=True, null=True)
    
    pproject = models.IntegerField(blank=True, null=True)
    
    uid = models.CharField(max_length=150, blank=True, null=True)
    
    warranty = models.CharField(max_length=150, blank=True, null=True)
    tmobile = models.CharField(max_length=150, blank=True, null=True)
    taddress = models.CharField(max_length=150, blank=True, null=True)
    tvat = models.CharField(max_length=150, blank=True, null=True)
    # recptdetail=models.ForeignKey(Tblreceiptdetails, on_delete=models.CASCADE)
    lblaccnt = models.CharField(max_length=150, blank=True, null=True)
    company= models.CharField(blank=True,null=True,max_length=50)
    area= models.CharField(blank=True,null=True,max_length=50)
    
    pbill=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,editable=True)

 
class Tblcompanymaster(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    companyname = models.CharField( blank=True, null=True,max_length=50)
    pcname = models.CharField(blank=True, null=True,max_length=50)
    password = models.CharField( blank=True, null=True,max_length=50)
class Tblusermaster(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    companyname = models.CharField( blank=True, null=True,max_length=50)
    area = models.CharField(blank=True, null=True,max_length=50)
    user = models.CharField(blank=True, null=True,max_length=50)
    password = models.CharField( blank=True, null=True,max_length=50)
    def __str__(self):
        return self.companyname   
class Tbluserdetails(models.Model):
    userid = models.IntegerField(blank=True, null=True,)
    username = models.CharField( blank=True, null=True,max_length=50)
    upassword = models.CharField(blank=True, null=True,max_length=50)
    ugroup = models.IntegerField(blank=True, null=True,)
    astatus = models.IntegerField(blank=True, null=True,)
    company = models.CharField( blank=True, null=True,max_length=50)
    area = models.CharField( blank=True, null=True,max_length=50)
    def __str__(self):
        return self.company
class Tbldepot(models.Model):
    dcode = models.IntegerField(blank=True, null=True,)
    dname = models.CharField( blank=True, null=True,max_length=50)
    vehicleno = models.CharField(blank=True, null=True,max_length=50)
    address =models.CharField(blank=True, null=True,max_length=50)
    city = models.CharField(blank=True, null=True,max_length=50)
    pin = models.CharField( blank=True, null=True,max_length=50)
    phoneno = models.CharField(blank=True, null=True,max_length=50)
    mobile =models.CharField(blank=True, null=True,max_length=50)
    cperson = models.CharField( blank=True, null=True,max_length=50)
    regno = models.CharField(blank=True, null=True,max_length=50)
    lescenseno = models.CharField(blank=True, null=True,max_length=50)
    description = models.CharField( blank=True, null=True,max_length=50)
    company=models.CharField( blank=True, null=True,max_length=50)
    def __str__(self):
        return self.dname
class Tblcomplaintdetails(models.Model):
    
    vno=models.IntegerField(blank=True,null=True)
    battery=models.IntegerField( blank=True, null=True)
    facecover=models.IntegerField( blank=True, null=True)
    backcover=models.IntegerField( blank=True, null=True)
    mmc=models.IntegerField( blank=True, null=True)
    sim=models.IntegerField( blank=True, null=True)
    charger=models.IntegerField( blank=True, null=True)
    nsignal=models.IntegerField( blank=True, null=True)
    ncharge=models.IntegerField( blank=True, null=True)
    npower=models.IntegerField( blank=True, null=True)
    mnt=models.IntegerField( blank=True, null=True)
    cnt=models.IntegerField( blank=True, null=True)
    fnt=models.IntegerField( blank=True, null=True)
    snt=models.IntegerField( blank=True, null=True)
    keypadnt=models.IntegerField( blank=True, null=True)
    lcdprob=models.IntegerField( blank=True, null=True)
    password=models.CharField(blank=True, null=True,max_length=50)
    imei=models.CharField(blank=True, null=True,max_length=50)
    addate=models.DateTimeField(blank=True, null=True)
    company=models.CharField(blank=True, null=True,max_length=50)
    
class Tbljob(models.Model):
    jidmain = models.IntegerField(primary_key=True)
    jid = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    note = models.CharField(max_length=150, blank=True, null=True)
    wcategoryid = models.IntegerField(blank=True, null=True)
    iqamano = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    mobile = models.CharField(max_length=150, blank=True, null=True)
    whatsappno = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)   
    company=models.CharField(blank=True, null=True,max_length=50) 
class Tblworkcategory(models.Model):
    widmain = models.IntegerField(primary_key=True)
    wid = models.IntegerField(blank=True,null=True)
    wcategory = models.CharField(max_length=150, blank=True, null=True)
    company=models.CharField(blank=True, null=True,max_length=50) 
class Tblrepackingdetails(models.Model):
    vno = models.IntegerField()
    
    slno = models.CharField(blank=True, null=True,max_length=50) 
    itemid = models.IntegerField(blank=True,null=True)
    batchcode = models.CharField(max_length=150, blank=True, null=True)
    qty= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    prate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    crate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    srate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    mrp= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10) 
    amount = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    depoid = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    company=models.CharField(blank=True, null=True,max_length=50) 
class Tblrepacking(models.Model):
    vno = models.IntegerField(primary_key=True)
    tblrepackdetails = models.ForeignKey(Tblrepackingdetails, on_delete=models.CASCADE)
    vdate = models.DateTimeField(blank=True, null=True)
    packdate = models.DateTimeField(blank=True, null=True)
    narration=models.CharField(blank=True, null=True,max_length=50) 
    slno = models.CharField(blank=True, null=True,max_length=50) 
    itemid = models.IntegerField(blank=True,null=True)
    batchcode = models.CharField(max_length=150, blank=True, null=True)
    qty= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    prate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    crate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    srate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    mrp= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10) 
    amount = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    depoid = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    labourcharge = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    costfactor= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    company=models.CharField(blank=True, null=True,max_length=50) 

class Tblproductsetdetails(models.Model):
    
    pid= models.IntegerField() 
    slno = models.CharField(blank=True, null=True,max_length=50) 
    item = models.IntegerField(blank=True,null=True)
    itemname = models.CharField(blank=True,null=True,max_length=100)
    qty= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    rate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    company=models.CharField(blank=True, null=True,max_length=50) 
    
class Tblproductset(models.Model):
    pid = models.IntegerField(primary_key=True,default=1)
    tblproddetails = models.ForeignKey(Tblproductsetdetails, on_delete=models.CASCADE)
    item = models.IntegerField(blank=True,null=True)
    itemname = models.CharField(blank=True,null=True,max_length=100)
    qty= models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    mrate = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10)
    lcharge = models.DecimalField(max_length=50,decimal_places=2,blank=True, null=True,max_digits=10) 
    company=models.CharField(blank=True, null=True,max_length=50) 

    

class Tblmnuseetings(models.Model):
    menuid=models.IntegerField(null=True,blank=True)
    presaleedit=models.IntegerField(null=True,blank=True)
    company=models.CharField(blank=True, null=True,max_length=50) 
    printheaderimage = models.ImageField( blank=True, null=True) 
    printfooterimage = models.ImageField( blank=True, null=True)
    





