from django.contrib import admin
from rn.models import UserDetails,Player,UserProfile,Timer,Bid,activePlayer, Bidder,UserPurse
# Register your models here.

class UserDetailsAdmin(admin.ModelAdmin):
    exclude=[]

# class pBidModelAdmin(admin.ModelAdmin):
# 	exclude=["posted"]
    
class PlayerAdmin(admin.ModelAdmin):
    exclude=[]
    
class UserProfileAdmin(admin.ModelAdmin):
    exclue=[]
    
class TimerAdmin(admin.ModelAdmin):
    exclude=[]

class BidAdmin(admin.ModelAdmin):
    exclude=[]

class activePlayerAdmin(admin.ModelAdmin):
	exclude=[]

class BidderAdmin(admin.ModelAdmin):
    exclude = []

class UserPurseAdmin(admin.ModelAdmin):
	exclude=[]

admin.site.register(UserDetails,UserDetailsAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Timer,TimerAdmin)
admin.site.register(Bid,BidAdmin)
# admin.site.register(pBidModel,pBidModelAdmin)
admin.site.register(activePlayer,activePlayerAdmin)
admin.site.register(Bidder, BidderAdmin)
admin.site.register(UserPurse,UserPurseAdmin)
