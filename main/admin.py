from django.contrib import admin
from main.models import Zombie, Tweet

class ZombieAdmin(admin.ModelAdmin):
	list_display = ('name_of_zombie', 'cemetery_of_zombie',)
	search_field = ('cemetery_of_zombie',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('state','tweet_zombie','created_at',)


admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Tweet, TweetAdmin)
