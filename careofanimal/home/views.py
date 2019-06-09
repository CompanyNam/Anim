from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from .models import Menu, Home, Donor_review,Languages,Event,Contacts,Message
from .models import Animal_need_help,Volunteer


# Create your views here.


def redirect_to_homeen(request):
    return HttpResponseRedirect("animalcare:redirect")


def homeinenglish(request):
    langs=Languages.objects.all()
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    event=Event.objects.all().filter(upcoming=1,language=language)

    donor_review = Donor_review.objects.all().filter(language=language)
    animal_need_help = Animal_need_help.objects.all()
    # percentage = (animal_need_help.animal_is_donated/animal_need_help.animal_need_amount)*100
    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'slogan': home.slogan,
        'total_donation_title': home.total_donation_title,
        'total_donation_text': home.total_donation_text,
        'total_donation_amount': home.total_donation_amount,
        'total_volunteers_title': home.total_volunteers_title,
        'total_volunteers_text': home.total_volunteers_text,
        'total_volunteers_amount': home.total_volunteers_amount,
        'future_plans_title': home.future_plans_title,
        'future_plans_text': home.future_plans_text,
        'future_plans_amount': home.future_plans_amount,
        'total_projects_title': home.total_projects_title,
        'total_projects_amount': home.total_projects_amount,
        'our_key_features_title': home.our_key_features_title,
        'our_key_features_text': home.our_key_features_text,
        'sponsorship_title': home.sponsorship_title,
        'sponsorship_text': home.sponsorship_text,
        'donate_amount_title': home.donate_amount_title,
        'donate_amount_text': home.donate_amount_text,
        'become_volunteer_title': home.become_volunteer_title,
        'langs':langs,
        'animal_need_help': animal_need_help,
        # 'percentage':percentage,
        'event': event,
        'home_logo':home.logo,
        "upcoming_events_title":home.upcoming_events_title,
        "upcoming_events_slogan": home.upcoming_events_slogan,
        'donor_review': donor_review,
    }
    return render(request, 'index.html', context)
def about_us_english(request):
    langs = Languages.objects.all()
    language = Languages.objects.all().filter(language_name="English")
    menu = Menu.objects.all().filter(language=language)
    home = Home.objects.all().filter(language=language)
    donor_review = Donor_review.all().filter(language=language
                                            )
    about_us="About us"
    write_home="Home"
    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'slogan': home.slogan,
        'total_donation_title': home.total_donation_title,
        'total_donation_text': home.total_donation_text,
        'total_donation_amount': home.total_donation_amount,
        'total_volunteers_title': home.total_volunteers_title,
        'total_volunteers_text': home.total_volunteers_text,
        'total_volunteers_amount': home.total_volunteers_amount,
        'future_plans_title': home.future_plans_title,
        'future_plans_text': home.future_plans_text,
        'future_plans_amount': home.future_plans_amount,
        'total_projects_title': home.total_projects_title,
        'total_projects_amount': home.total_projects_amount,
        'our_key_features_title': home.our_key_features_title,
        'our_key_features_text': home.our_key_features_text,
        'sponsorship_title': home.sponsorship_title,
        'sponsorship_text': home.sponsorship_text,
        'donate_amount_title': home.donate_amount_title,
        'donate_amount_text': home.donate_amount_text,
        'become_volunteer_title': home.become_volunteer_title,
        'donor_name': donor_review.donor_name,
        'donor_is_who': donor_review.donor_is_who,
        'donor_description': donor_review.donor_description,
        'about_us':about_us,
        'write-home':write_home,
        'langs':langs,

    }
    return render(request, 'about-us.html', context)

def events_eng(request):
    langs = Languages.objects.all()
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    event=Event.objects.all().filter(language=language)

    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'event':event,
        'langs': langs,
    }
    return render(request, "event.html", context)

def event_detail_eng(request,slug):
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    event = get_object_or_404(Event, slug=slug)

    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'event_date': event.date,
        'event_desc':event.details,
        'event_little_details': event.event_little_detail,
        'event_title': event.title,
        "event_main_image": event.image_main,
        'event_img_1':event.event_image1,
        'event_img_2': event.event_image2,
        'event_img_3': event.event_image3,
        'event_img_4': event.event_image4,
        'event_img_5': event.event_image5,
        'event_img_6': event.event_image6,
        'event_img_7': event.event_image7,
        'event_img_8': event.event_image8,
        'event_img_9': event.event_image9,
        'event_img_10': event.event_image10,
        'event_details':event.details,

        'address':event.event_adress,
        'city':event.event_city,




    }
    return render(request, "event-details.html", context)


def contac_us_eng(request):
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    contacts = Contacts.objects.get(language=language)
    if request.method == "post":
        name=request.POST.get('name')
        email=request.POST.get('email')

        subject=request.POST.get('subject')

        message=request.POST.get('message')

        Message.objects.create(message_text=message,email=email,name=name,subject=subject)


    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'contacts_mail':contacts.mail,
        'contacts_mail_text': contacts.mail_text,
        'contacts_telephone': contacts.telephone_number,
        'contacts_telephone_text': contacts.telephone_number_text,

    }
    return render(request, "event-details.html", context)


def volunteer_info():
    language = Languages.objects.all().filter(language_name="English")
    menu = Menu.objects.all().filter(language=language)
    volunteer = Volunteer.all().filter(language=language)
    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'volunteer': volunteer

    }