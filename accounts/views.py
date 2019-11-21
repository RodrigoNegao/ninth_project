from django.shortcuts import render
from .forms import (
UserCreateForm, updateUserForm , updateAvatarForm, updateImageResumeForm
)
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
#UpdateView
from django.contrib import messages
from django.shortcuts import redirect
from .models import User


@login_required
def logout_view(request):
    # Log out the user.
    logout(request)
    # Return to index.
    return HttpResponseRedirect(reverse('index'))

def signup(request):

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserCreateForm(data=request.POST)
        # profile_default = updateImageResumeForm(data=request.POST, files=request.FILES)
        # Check to see the form is valid
        if user_form.is_valid(): # and profile_default.is_valid() :
            # Save User Form to Database
            user = user_form.save()#commit=False)

            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # profile = profile_default.save()
            # profile.save()

            # Registration Successful! messages.success
            messages.success(request, 'Account created successfully')
            #Go to Login
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserCreateForm()
        # profile_default = updateImageResumeForm()


    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'accounts/signup.html',
                          {'form': user_form })

def user_login(request):
    if request.method == 'POST':
        # First get the EMAIL and password supplied
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(email=email, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # print("Someone tried to login and failed.")
            # print("They used email: {} and password: {}".format(email,password))
            messages.error(request, 'Invalid login details supplied.')
        return redirect('accounts:login')

    else:
        #Nothing has been provided for username or password.
        return render(request, 'accounts/login.html', {})


@login_required
def updateuser(request):
    if request.method == 'POST':
        # files=request.FILES is necessary to upload Files
        form = updateUserForm(data=request.POST, instance=request.user)  #files=request.FILES,
        avatar = updateAvatarForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = updateImageResumeForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        
        if form.is_valid() and avatar.is_valid():
            form.save()
            avatar.save()
            profile_form.save()
            # user = form.save()
            # user.save()

            #'Profile details updated.' or 'You account has been updated'
            messages.success(request, 'You account has been updated')
            return redirect('accounts:updateuser')
            # return HttpResponseRedirect(reverse('accounts/updateuser'))
    else:
        form = updateUserForm(instance=request.user) #request.user)
        avatar = updateAvatarForm(files=request.FILES)
        profile_form = updateImageResumeForm(files=request.FILES)
        context = {'form':form, 'avatar':avatar , 'profile_form':profile_form}
    return render(request, 'accounts/updateuser.html', context )
