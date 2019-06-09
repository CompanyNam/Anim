from django.contrib import admin
from .models import Menu, Languages, Home, Event, Volunteer,Donor_review,Donor_Details,Animal_need_help




admin.site.register(Donor_Details)
admin.site.register(Animal_need_help)
admin.site.register(Menu)
admin.site.register(Languages)
admin.site.register(Donor_review)
admin.site.register(Home)
admin.site.register(Event)
admin.site.register(Volunteer)


