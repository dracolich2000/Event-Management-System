from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from signup.models import Signup
from contactus.models import Contactus
from createEvent.models import CreateEvent
from django.contrib.auth.hashers import make_password, check_password

def landing_page(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cu = Contactus(name = name, email=email, subject=subject, message=message)
        cu.save()
        return redirect('thank_you')
    except:
        print('error')
    return render(request,'landing.html')

def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        usr = Signup.objects.get(username=username)
        if check_password(password,usr.password):
            request.session['user_id'] = usr.id
            request.session['username'] = usr.username
            return redirect('dashboard')
        else:
            return render(request,'login.html',{
                'error' : 'Invalid username or password'
            })
    except:
        print('error')
    return render(request,'login.html')

def success(request):
    return render(request,'success.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password==confirm_password:
            hashed_password = make_password(password)
        else:
            return render(request,'signup.html',{
                'error' : 'Please check your password'
            })
        try:
            sg = Signup(username = username,email = email,password = hashed_password)
            sg.save()
            return redirect('success')
        except:
            print('Please try again')
            return render(request,'signup.html',{
                'error' : 'Please try with different email or username'
            })
    return render(request,'signup.html')

def forgot_password(request):
    return render(request,'forgot_password.html')

def thank_you(request):
    return render(request,'thank_you.html')

def dashboard(request):
    username = request.session.get('username')
    if username:
        uname = Signup.objects.get(username=username)
        event_count = CreateEvent.objects.filter(username=uname).count()  # Filter events by this organizer
        events = CreateEvent.objects.filter(username=uname)
        selected = request.POST.get('event_name')
        event = None
        if selected:
            try:
                event = CreateEvent.objects.get(event_name=selected)
            except CreateEvent.DoesNotExist:
                event = None
        return render(request, 'dashboard.html', {'username': username,'event_count': event_count,'events': events,'selected_event_name': selected,'event': event})
    else:
        return render(request,'dashboard.html')

def attendees(request):
    return render(request,'attendees.html')

def events(request):
    username = request.session.get('username')  # Get the organizer username from session
    if username:
        uname = Signup.objects.get(username=username)
        events = CreateEvent.objects.filter(username=uname)  # Filter events by this organizer
        return render(request, 'events.html', {'events': events})
    else:
        return render(request, 'events.html')

def overview(request):
    username = request.session.get('username')
    if username:
        uname = Signup.objects.get(username=username)
        event_count = CreateEvent.objects.filter(username=uname).count()
        return render(request,'overview.html',{'event_count': event_count})
    else:
        return render(request,'overview.html')

def settings(request):
    return render(request,'settings.html')

def ticket_sales(request):
    return render(request,'ticket_sales.html')

def add_event(request):
    if request.method == 'POST':
        try:
            event_name = request.POST['event-name']
            date = request.POST['event-date']
            location = request.POST['event-location']
            description = request.POST['event-description']
            img = request.FILES.get('event-image')
            username = request.session.get('username')
            uname = Signup.objects.get(username=username)
            ae = CreateEvent(event_name=event_name,date=date,location=location,description=description,img=img,username=uname)
            ae.save()
            success_message = 'Event added successfully!'
            return render(request, 'add-event.html', {'success': success_message})
        except:
            print('error occured')
            error_message = 'An error occurred. Please try again later.'
            return render(request, 'add-event.html', {'error': error_message})
    return render(request,'add-event.html')

def logout(request):
    return redirect('landing')
    
def view_event(request,event_name):
    username = request.session.get('username')  # Get the organizer username from session
    if username:
        uname = Signup.objects.get(username=username)
        event = CreateEvent.objects.get(event_name=event_name,username=uname)
    if event:
        return render(request, 'view-event.html', {'event': event})
    else:
        return render(request,'view-event.html')
    
def edit_event(request, event_name):
    username = request.session.get('username')  # Get the organizer username from session
    if username:
        uname = Signup.objects.get(username=username)
        event = CreateEvent.objects.get(event_name=event_name,username=uname)
    if request.method == 'POST':
        try:
            event.event_name = request.POST['event_name']
            event.date = request.POST['date']
            event.location = request.POST['location']
            event.description = request.POST['description']
            
            if 'img' in request.FILES:
                event.img = request.FILES['img']

            event.save()
            return render(request, 'edit_event.html', {'success': 'Event updated successfully!'})
        except:
            return render(request, 'edit_event.html', {'error': 'Please try again!'})
    return render(request, 'edit_event.html', {'event': event})

def delete_event(request, event_name):
    
    username = request.session.get('username')  # Get the organizer username from session
    if username:
        uname = Signup.objects.get(username=username)
        event = CreateEvent.objects.get(event_name=event_name,username=uname)
        event.delete()
        events = CreateEvent.objects.filter(username=uname)  # Filter events by this organizer
        return render(request, 'events.html', {'events': events})
    else:
        return render(request, 'events.html', {'events': events})