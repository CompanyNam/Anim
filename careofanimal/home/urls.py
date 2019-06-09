from .views import homeinenglish,redirect_to_homeen,about_us_english,event_detail_eng,events_eng,contac_us_eng
from django.conf.urls import url
app_name="animalcare"
urlpatterns = [

    url(r'^home/en/$', homeinenglish, name="homeen"),

    url(r'^ /$', redirect_to_homeen, name="redirect"),
    url(r'^about-us/en/$', about_us_english , name="about_us"),
    url(r'^events/en/$', events_eng, name="events_en"),
    url(r'^event/(?P<slug>[\w-]+)/$', event_detail_eng, name='event_detail'),
    url(r'^contact-us/en/$',contac_us_eng, name="contact-us-en")

]