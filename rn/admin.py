from django.contrib import admin
from rn.models import UserDetails,Player,UserProfile,Timer,Bid,pBidModel,activePlayer
# Register your models here.

class UserDetailsAdmin(admin.ModelAdmin):
    exclude=["posted"]

class pBidModelAdmin(admin.ModelAdmin):
	exclude=["posted"]
    
class PlayerAdmin(admin.ModelAdmin):
    exclude=["posted"]
    
class UserProfileAdmin(admin.ModelAdmin):
    exclue=["posted"]
    
class TimerAdmin(admin.ModelAdmin):
    exclude=["posted"]

class BidAdmin(admin.ModelAdmin):
    exclude=["posted"]

class activePlayerAdmin(admin.ModelAdmin):
	exclude=["posted"]
    
admin.site.register(UserDetails,UserDetailsAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Timer,TimerAdmin)
admin.site.register(Bid,BidAdmin)
admin.site.register(pBidModel,pBidModelAdmin)
admin.site.register(activePlayer,activePlayerAdmin)