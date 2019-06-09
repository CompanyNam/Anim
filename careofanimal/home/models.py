from django.db import models
import os
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Languages(models.Model):

    language_name = models.CharField(max_length=122)
    language_id=models.IntegerField()

    def __str__(self):
        return self.language_name



class Menu(models.Model):
    home = models.CharField(max_length=122)
    gallery = models.CharField(max_length=122)
    about = models.CharField(max_length=122)
    events = models.CharField(max_length=122)
    pages = models.CharField(max_length=122)
    blog = models.CharField(max_length=122)
    contact = models.CharField(max_length=122)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)


    def __str__(self):

        return self.home+" / "+self.gallery+" / "+self.about+" / "+self.events+" / "+self.pages+" / "+self.blog+" / "+self.contact+"/"+ "this menu is in ==================>"+self.language.language_name

class Home(models.Model):

    slogan=models.CharField(max_length=265)
    total_donation_title = models.CharField(max_length=122)
    total_donation_text = models.TextField()
    total_donation_amount = models.CharField(max_length=122)
    total_volunteers_title = models.CharField(max_length=122)
    total_volunteers_text = models.TextField()
    total_volunteers_amount = models.CharField(max_length=15)
    future_plans_title = models.CharField(max_length=122)
    future_plans_text = models.TextField()
    future_plans_amount = models.CharField(max_length=22)
    total_projects_title = models.CharField(max_length=33)
    total_projects_amount = models.CharField(max_length=22)
    image_welcome_acc = models.ImageField(blank=True)
    our_key_features_title = models.CharField(max_length=122)
    our_key_features_text = models.TextField()
    sponsorship_title = models.CharField(max_length=44)
    sponsorship_text = models.TextField()
    donate_amount_title = models.CharField(max_length=44)
    donate_amount_text = models.TextField()
    become_volunteer_title = models.CharField(max_length=44)
    become_volunteer_text = models.TextField()
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    upcoming_events_title=models.CharField(max_length=120)
    upcoming_events_slogan=models.CharField(max_length=120)
    logo=models.ImageField(blank=True)
    def __str__(self):
        return str(self.slogan) + str(self.total_donation_title)

class Event(models.Model):
    title = models.CharField(max_length=44)
    event_little_detail = models.TextField()
    details = models.TextField()
    date = models.DateTimeField()
    event_adress=models.CharField(max_length=120)
    event_city=models.CharField(max_length=120)
    image_main = models.ImageField(blank=True)
    event_image1 = models.ImageField(blank=True)
    event_image2 = models.ImageField(blank=True)
    event_image3 = models.ImageField(blank=True)
    event_image4 = models.ImageField(blank=True)
    event_image5 = models.ImageField(blank=True)
    event_image6 = models.ImageField(blank=True)
    event_image7 = models.ImageField(blank=True)
    event_image8 = models.ImageField(blank=True)
    event_image9 = models.ImageField(blank=True)
    event_image10 = models.ImageField(blank=True)
    event_image11 = models.ImageField(blank=True)
    event_image12 = models.ImageField(blank=True)
    event_image13 = models.ImageField(blank=True)
    upcoming = models.BooleanField(default=False)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)

    slug=models.SlugField(unique=True, editable=False, max_length=130)


    class Meta:
        ordering = ['-date']
    def get_absolute_url(self):
        return reverse('animalcare:event_detail', kwargs={'slug': self.slug})
        # return "/post/{}".format(self.id)

    def __str__(self):
        if self.upcoming==1:
            return self.title + "////////////////////////////This event is UPCOMING/////////////////////////////////" + "this menu is in ==================>" + self.language.language_name
        else:
            return self.title + "////////////////////////////This event is NOT UPCOMING/////////////////////////////" + "this menu is in ==================> "+ self.language.language_name

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Event, self).save(*args, **kwargs)


class Volunteer(models.Model):
    full_name = models.CharField(max_length=122)
    birth = models.DateTimeField()
    is_doing = models.CharField(max_length=122)
    description = models.TextField()
    image = models.ImageField(blank=True)

    language = models.ForeignKey(Languages, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name + "in" + self.language.language_name


class Contacts(models.Model):
    telephone_number = models.CharField(max_length=122)
    telephone_number_text = models.TextField()
    mail = models.EmailField()
    mail_text = models.TextField()
    language = models.ForeignKey(Languages,on_delete=models.CASCADE)
    def __str__(self):
        return self.language.language_name

class Message(models.Model):
    name = models.CharField(max_length=122)
    email =models.EmailField()
    subject=models.CharField(max_length=122)
    message_text=models.TextField()
    def __str__(self):
        return self.name + self.email



class Donor_review(models.Model):
    donor_name = models.CharField(max_length=122)
    donor_is_who = models.CharField(max_length=122)
    donor_description = models.TextField()
    donor_image = models.ImageField(blank=True)
    language=models.ForeignKey(Languages,on_delete=models.CASCADE)

class Donor_Details(models.Model):
    Donor_name = models.CharField(max_length=122)
    Donor_surname = models.CharField(max_length=122)
    Donor_gives = models.IntegerField()
    Donation_time = models.DateTimeField(auto_now_add=True)

class Animal_need_help(models.Model):
    animal_name = models.CharField(max_length=122)
    animal_image1 = models.ImageField(blank=True,upload_to="animal_need_help")

    animal_image2 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image3 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image4 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image5 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image6 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image7 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image8 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image9 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image10 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image11 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image12 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_image13 = models.ImageField(blank=True,upload_to="animal_need_help")
    animal_need_amount = models.IntegerField()
    animal_is_donated = models.IntegerField()

    donor = models.ManyToManyField(Donor_Details,blank=True)
