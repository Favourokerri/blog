from django.contrib import admin
from .models import Profile, Contact, About, FAQ

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', 'facebook_link']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(FAQ, FAQAdmin)
