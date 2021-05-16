from django.contrib import admin
from .models import Kyc_Info, Kyc_Infotemp, Id_Info, Image, Kyc_Reject
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

#admin.site.register(Kyc_Info)
admin.site.register(Kyc_Infotemp)
admin.site.register(Id_Info)
admin.site.register(Image)
admin.site.register(Kyc_Reject)
#admin.site.register(HistoricalKyc_Info)

class kycHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "full_name_temp", "nics_no_temp", "mob_no_temp"]
    history_list_display = ["nics_no_temp"]
    search_fields = ['nics_no_temp', 'full_name_temp']
    

admin.site.register(Kyc_Info, kycHistoryAdmin)