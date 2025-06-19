from django.contrib import admin

# Register your models here.
from django.contrib import admin

from zshopapp.models import Tblitemcategory,Tblissuedetails,TblTransactionReceipt,Tblreceiptdetails,Tblcompanymaster,Tblusermaster, Tblitemmaster,Tblbusinessissue, Tblbatch, Tblinventory, Tblaccgroup,Tblgeneralledger,Tblaccountledger




# from technocart.wisedecoreapp.models import Tblgeneralledger


# Register your models here.
class Itemcategadmin(admin.ModelAdmin):
    admin.site.register(Tblitemcategory)
class itemadmin(admin.ModelAdmin):
    admin.site.register(Tblitemmaster)
    admin.site.register(Tblbatch)
    # admin.site.register(Tblgeneralledger)
class inventoryadmin(admin.ModelAdmin):
    admin.site.register(Tblinventory)
class lgroupadmin(admin.ModelAdmin):
    admin.site.register(Tblaccgroup)
class generalledger(admin.ModelAdmin):
    admin.site.register(Tblgeneralledger)
admin.site.register(Tblaccountledger)

class salesadmin(admin.ModelAdmin):
    admin.site.register(Tblbusinessissue)
    admin.site.register(Tblissuedetails)
class purchaseadmin(admin.ModelAdmin):
    admin.site.register(TblTransactionReceipt)
    admin.site.register(Tblreceiptdetails)
admin.site.register(Tblcompanymaster)
admin.site.register(Tblusermaster)



