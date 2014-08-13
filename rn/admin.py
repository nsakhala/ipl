from django.contrib import admin
from rn.models import User,Player,UserProfile,Timer,Bid
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    exclude=["posted"]
    
class PlayerAdmin(admin.ModelAdmin):
    exclude=["posted"]
    
class UserProfileAdmin(admin.ModelAdmin):
    exclue=["posted"]
    
class TimerAdmin(admin.ModelAdmin):
    exclude=["posted"]

class BidAdmin(admin.ModelAdmin):
    exclude=["posted"]
    
admin.site.register(User,UserAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Timer,TimerAdmin)
admin.site.register(Bid,BidAdmin)