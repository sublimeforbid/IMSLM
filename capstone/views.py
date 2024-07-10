from datetime import datetime
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from datetime import datetime
from .models import BarangayUser


def index(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin_page')

    print(request.user.id)
    return render(request, 'pages/dashboard.html', {'user': request.user})


def adminlogin_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('index')
        messages.error(request, "Logged in Unsuccessfully")
    return render(request, 'pages/adminlogin.html')


def adminregister_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        profile = request.FILES.get('profile')
        barangay_position = request.POST.get('barangay_position')
        phonenumber = request.POST.get('phonenumber')
        office_hours_weekdays = request.POST.get('office_hours_weekdays')
        office_hours_weekends = request.POST.get('office_hours_weekends')
        responsibilities = request.POST.get('responsibilities')
        about = request.POST.get('about')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        confirmationPass = request.POST.get('password2')
        context = {
            'username': username,
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'profile': profile,
            'barangay_position': barangay_position,
            'phonenumber': phonenumber,
            'office_hours_weekdays': office_hours_weekdays,
            'office_hours_weekends': office_hours_weekends,
            'responsibilities': responsibilities,
            'about': about,
            'email': email,
            'username': username,
        }
        if password != confirmationPass:
            messages.error(request, "Passwords do not match")
            return render(request, 'pages/adminregister.html', context)

        try:
            if office_hours_weekdays:
                office_hours_weekdays = datetime.strptime(
                    office_hours_weekdays, '%Y-%m-%dT%H:%M')
            if office_hours_weekends:
                office_hours_weekends = datetime.strptime(
                    office_hours_weekends, '%Y-%m-%dT%H:%M')
        except ValueError:
            messages.error(request, "Input date and time")
            return render(request, 'pages/adminregister.html')

        if profile:
            fs = FileSystemStorage()
            filename = fs.save(profile.name, profile)
        else:
            filename = None

        User = get_user_model()

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            middle_name=middle_name,
            profile_pic=filename,
            barangay_position=barangay_position,
            phone=phonenumber,
            office_hours_weekdays=office_hours_weekdays,
            office_hours_weekends=office_hours_weekends,
            responsibilities=responsibilities,
            about=about
        )
        user.set_password(password)

        user.save()

        # authenticate the user
        authenticate(request, username=user.username,
                     password=user.password)

        messages.success(request, "Registration Complete")
        return redirect('adminlogin_page')

    return render(request, 'pages/adminregister.html')


def aboutPage(request):
    return render(request, 'pages/about.html')


@login_required
def profile_page(request):
    user = request.user

    if request.method == 'POST':
        profile = request.FILES.get('profile')
        barangay_position = request.POST.get('barangay_position')
        phonenumber = request.POST.get('phonenumber')
        office_hours_weekdays = request.POST.get('office_hours_weekdays')
        office_hours_weekends = request.POST.get('office_hours_weekends')
        responsibilities = request.POST.get('responsibilities')
        about = request.POST.get('about')

        if profile:
            fs = FileSystemStorage()
            filename = fs.save(profile.name, profile)
        else:
            filename = None

        user.barangay_position = barangay_position
        user.phone = phonenumber
        user.office_hours_weekdays = office_hours_weekdays
        user.office_hours_weekends = office_hours_weekends
        user.responsibilities = responsibilities
        user.about = about
        if filename:
            user.profile_pic = filename

        user.save()
        messages.success(request, "Profile Updated Successfully")

        return redirect('profile_page')

    office_hours_weekdays = datetime.fromisoformat(
        str(user.office_hours_weekdays))
    office_hours_weekends = datetime.fromisoformat(
        str(user.office_hours_weekends))

    # Convert the datetime object to the format compatible with datetime-local input
    formatted_weekdays = office_hours_weekdays.strftime("%Y-%m-%dT%H:%M")
    formatted_weekends = office_hours_weekends.strftime("%Y-%m-%dT%H:%M")
    print(formatted_weekdays)
    print(formatted_weekends)

    return render(request, 'pages/profile.html', {'user': user, 'formatted_weekdays': formatted_weekdays, 'formatted_weekends': formatted_weekdays})


def updateProfile(request):
    return render(request, 'pages/updateprofile.html')


def announcement_page(request):
    return render(request, 'pages/announcement.html')


def market_page(request):
    return render(request, 'pages/market.html')


def reports_page(request):
    return render(request, 'pages/reports.html')


def log_out(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('adminlogin_page')
