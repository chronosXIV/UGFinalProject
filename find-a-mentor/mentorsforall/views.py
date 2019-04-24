from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from .decorators import profile
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Message, Subject, Event
from django.db.models import Q

import datetime

User = get_user_model()

def index(request):
    if request.user.is_authenticated:
        return redirect(home)
    return render(request,'mentorsforall/index.html')

#sign in page
def signin(request):
    if request.user.is_authenticated:
        return redirect(home)
    return render(request, 'mentorsforall/signin.html')

# handle user authentication POST
def login_auth_view(request):
    if request.method != 'POST': return redirect(home)

    fields = QueryDict(request.body)

    username = fields.get('login_username')
    password = fields.get('login_password')

    #try to authenticate
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect(home)
    else:
        return redirect(signin)

#register page
def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    fields = QueryDict(request.body)

    f_role = fields.get('role_button')

    subjects = Subject.objects.all()

    categories = []

    for s in subjects:
        category = s.get_category_display()
        categories.append(category)
    categories = list(set(categories))

    context = {
        'role': f_role,
        'subjects': subjects,
        'categories': categories
    }

    return render(request, 'mentorsforall/signup.html', context)

# handle registration
def complete_signup(request):

    fields = QueryDict(request.body)

    # get registration data
    f_first_name = fields.get('register_first_name')
    f_last_name = fields.get('register_last_name')
    f_email = fields.get('register_email')
    f_username = fields.get('register_username')
    f_password = fields.get('register_password')
    f_privacy_consent = fields.get('register_privacy_consent')
    f_role = fields.get('register_role')
    new_user = User.objects.create_user(f_username, f_email, f_password)
    new_profile = Profile(  gender=None,
                            birthdate=None,
                            givenname=f_first_name,
                            familyname=f_last_name,
                            role=f_role,
                            job=None,
                            accountid=new_user
                        )

    new_profile.save()

    user = authenticate(request, username=f_username, password=f_password)

    if user is not None:
        login(request, user)
        request.session['pp_complete_signup'] = True
        return redirect(create_profile_view)
    else:
        return redirect(index)

def create_profile_view(request):
    if not request.user.is_authenticated:
        return redirect(index)
    elif not 'pp_complete_signup' in request.session:
        return redirect(home)
    else:
        current_user = request.user

        p = Profile.objects.get(accountid = current_user.id)

        request.session['pp_create_profile_view'] = True
        context = {
            'profile' : p
        }
        return render(request, 'mentorsforall/profilecreate.html', context)

def complete_profile(request):
    if not request.user.is_authenticated:
        return redirect(index)

    fields = QueryDict(request.body)

    current_user = request.user

    # get registration data
    f_job = fields.get('register_job')
    f_city = fields.get('register_city')
    f_gender = fields.get('register_gender')
    f_dob = fields.get('register_dob')
    f_about = fields.get('register_about')

    p = Profile.objects.filter(accountid = current_user.id)

    p.update(job=f_job,city=f_city,gender=f_gender,birthdate=f_dob,about=f_about)

    return redirect(home)

#home page
def home(request):
    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user
    p = Profile.objects.get(accountid=current_user.id)

    events = []

    for subject in p.subjects.all():
        events.extend(Event.objects.filter(subjects__id__exact=subject.id))
    eventlist = list(dict.fromkeys(events))

    if len(eventlist) == 0:
        events.extend(Event.objects.filter(city=p.city))
        eventlist = list(dict.fromkeys(events))

    context = {
        'profile': p,
        'events': eventlist
    }

    return render(request, 'mentorsforall/home.html', context)

def do_search(request):
    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user

    p = Profile.objects.get(accountid=current_user.id)

    fields = request.GET

    # get data
    subjectquery = fields.get('search_box_mentor', None)
    subjectdropdown = fields.get('mentor_dropdown', None)
    eventquery = fields.get('search_box_event', None)
    eventdropdown = fields.get('event_dropdown', None)

    if (subjectquery != None):
        if (subjectdropdown == "Subject"):
            filtered = list(Profile.objects.filter(Q(subjects__name__icontains=subjectquery) & Q(role='TOR') & ~Q(accountid=current_user.id)))
        elif (subjectdropdown == "Name"):
            filtered = list(Profile.objects.filter(Q(givenname__icontains=subjectquery) | Q(familyname__icontains=subjectquery)).filter(~Q(accountid=current_user.id) & Q(role='TOR')))
        elif (subjectdropdown == "City"):
            filtered = list(Profile.objects.filter(Q(city__icontains=subjectquery) & Q(role='TOR') & ~Q(accountid=current_user.id)))

        filtered = list(set(filtered))
        searchedfor = "mentor"

    elif (eventquery != None):
        if (eventdropdown == "Subject"):
            filtered = list(Event.objects.filter(Q(subjects__name__icontains=eventquery)).exclude(public=False))
        elif (eventdropdown == "Name"):
            filtered = list(Event.objects.filter(Q(name__icontains=eventquery)).exclude(public=False))
        elif (eventdropdown == "City"):
            filtered = list(Event.objects.filter(Q(city__icontains=eventquery)).exclude(public=False))
        elif (eventdropdown == "Mentor"):
            filtered = list(Event.objects.filter(Q(host__givenname__icontains=eventquery) | Q(host__familyname__icontains=eventquery)).exclude(public=False))

        filtered = list(set(filtered))
        searchedfor = "event"

    else:
        filtered = []
        searchedfor = "empty"

    context = {
        'matched': filtered,
        'searchedfor': searchedfor
    }
    return render(request, 'mentorsforall/searchresults.html', context)

@profile
def profile_view(request, profile_id=None):
    try:
        p = Profile.objects.get(id=profile_id)
    except:
        p = request.profile

    try:
        messages = Message.objects.filter(receiver=p.id, public=True) | Message.objects.filter(sender=request.profile, receiver=p.id)
    except:
        messages = None

    request.session['pp_profile_view'] = True

    context = {
        'profile': p,
        'age': (datetime.date.today() - p.birthdate) // datetime.timedelta(days=365),
        'gender_icon': p.gender,
        'image': p.image.name.replace('mentorsforall/static/',''),
        'messages': messages
        }
    return render(request, 'mentorsforall/profileview.html', context)

@profile
def profile_post_message_view(request):

    fields = QueryDict(request.body)
    f_account = fields.get('receiver_id')
    f_content = fields.get('new_message')
    f_public = fields.get('public_check')

    if f_public == "on":
        f_public = True
    else:
        f_public = False

    nf_rec = Profile.objects.get(id=f_account)
    new_message = Message(  sender=request.profile,
                            receiver=nf_rec,
                            content=f_content,
                            public=f_public )
    new_message.save()
    return redirect(profile_view, profile_id = f_account)

def profile_edit_view(request):
    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user

    p = Profile.objects.get(accountid=current_user.id)

    request.session['pp_profile_edit_view'] = True

    context = {
        'profile': p,
        'age': (datetime.date.today() - p.birthdate) // datetime.timedelta(days=365),
        'image': p.image.name.replace('mentorsforall/static/',''),
        }
    return render(request, 'mentorsforall/profileedit.html', context)

def profile_image_upload_endpoint(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['profile_image']

            current_user = request.user

            p = Profile.objects.get(accountid=current_user.id)

            p.image.save('', uploaded_file)
        except:
            uploaded_file = None;
    if 'pp_profile_edit_view' in request.session:
        return redirect(profile_edit_view)
    elif 'pp_create_profile_view' in request.session:
        return redirect(create_profile_view)
    else:
        return redirect(index)

def subjectlist_view(request):
    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user

    subjectlist = list(Subject.objects.all())

    context = {
        'subjectlist': subjectlist
    }

    return render(request, 'mentorsforall/subjectlist.html', context)

def messaging(request):

    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user

    p = Profile.objects.get(accountid=current_user.id)

    try:
        messages = list(Message.objects.filter(Q(sender=p) | Q(receiver=p)).filter(public=False))
    except:
        messages = None

    listofprofiles = []

    for m in messages:
        if (getattr(m, 'sender') != p):
            listofprofiles.append(getattr(m, 'sender'))

        if (getattr(m, 'receiver') != p):
            listofprofiles.append(getattr(m, 'receiver'))

    listofprofiles = list(set(listofprofiles))

    context = {
        'profiles': listofprofiles,
        'messages': messages
    }
    return render(request, 'mentorsforall/messaging.html', context)

@profile
def messaging_post_message_view(request):
    fields = QueryDict(request.body)

    f_account = fields.get('receiver_id')
    f_content = fields.get('new_message')

    nf_rec = Profile.objects.get(id=f_account)

    new_message = Message(  sender=request.profile,
                            receiver=nf_rec,
                            content=f_content,
                            public=False
                        )
    new_message.save()

    return redirect(messaging)

def event_view(request, event_id=None):

    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user

    p = Profile.objects.get(accountid=current_user.id)

    try:
        e = Event.objects.get(id=event_id)
    except:
        e = request.event

    try:
        attendees = list(e.attendees.all())

    except:
        attendees = None

    current_user_attending = False

    for attendee in attendees:
        if attendee == p:
            current_user_attending = True

    context = {
        'event': e,
        'image': e.image.name.replace('mentorsforall/static/',''),
        'userattending' : current_user_attending
        }
    return render(request, 'mentorsforall/eventview.html', context)

def event_edit_view(request, event_id=None):
    if not request.user.is_authenticated:
        return redirect(index)

    current_user = request.user

    p = Profile.objects.get(accountid=current_user.id)

    try:
        e = Event.objects.get(id=event_id)
    except:
        e = request.event

    if e.host != p:
        return redirect(event_view, event_id=event_id)

    context = {
        'event': e,
        'image': e.image.name.replace('mentorsforall/static/',''),
        }
    return render(request, 'mentorsforall/eventedit.html', context)

def event_management_view(request, event_id=None):

    if request.method != 'POST': return redirect(event_view, event_id=event_id)

    current_user = request.user

    p = Profile.objects.get(accountid=current_user.id)
    e = Event.objects.get(id=event_id)

    fields = QueryDict(request.body)
    f_eventrequest = fields.get('event_button')

    if f_eventrequest == 'leave':
        e.attendees.remove(p)
    elif f_eventrequest == 'attend':
        e.attendees.add(p)
        e.save()

    return redirect(event_view, event_id=event_id)

#logout page
def signout(request):
    logout(request)
    return redirect(index)
