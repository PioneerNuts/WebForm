from django.shortcuts import render, redirect
from .forms import ContactForm,HazardForm,CheckIN,NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something with the form data
            data = form.cleaned_data
            form.save()
            # Redirect to success page or display a message
            return render(request, 'pioneer.html')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

    

@login_required
def hazard(request):
    if request.method == 'POST':
        form1= HazardForm(request.POST)
        if form1.is_valid():
            # Do something with the form data
            data = form1.cleaned_data
            form1.save()
            # Redirect to success page or display a message
            return render(request, 'pioneer.html')
    else:
        form1= HazardForm()
    return render(request, 'hazard.html', {'form1': form1})


### adding the code 

#method for checkin form

### adding the code
@login_required
def Check(request):
    if request.method == 'POST':
        ch_form= CheckIN(request.POST)
        if ch_form.is_valid():
            # Do something with the form data
            data = ch_form.cleaned_data
            ch_form.save()
            # print(ch_form.data)
   
            data_check = ch_form.data
            # print(data_check['ill'] == '2' and data_check['garments'] == '1' and data_check['wash'] == '1' and data_check['jwelry'] == '1' and data_check['hair'] == '1' and data_check['food'] == '2' and data_check['food_package'] == '1')
            if(data_check['ill'] == '2' and data_check['garments'] == '1' and data_check['wash'] == '1' and data_check['jwelry'] == '1' and data_check['hair'] == '1' and data_check['food'] == '2' and data_check['food_package'] == '1'):
                return render(request, 'positive.html')
            else:
                return render(request, 'negative.html')
            # Redirect to success page or display a message
            # return render(request, 'checkin.html')
    else:
        ch_form= CheckIN()
        
    return render(request, 'checkin.html', {'ch_form': ch_form})


#registration form

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return render(request, 'home.html')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

#login method

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request, 'pioneer.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


#log out method 

def logout_request(request):
	logout(request)
	messages.success(request, "You have successfully logged out.") 
	return render(request, 'pioneer.html')


def pioneer_home(request):
    return render(request,'pioneer.html')    

def message_view(request):
    return render(request,'message.html') 

def about_us(request):
    return render(request,'aboutus.html')   

def contact_us(request):
    return render(request,'contactus.html')    

#login require function

@login_required
def my_view(request):
    # your view code here
    return render (request,'login.html')

