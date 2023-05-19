from django import forms
# from django.utils.timezone import now
from .models import Metal_detection,Emp_wellness,Hazard_material, metal_d
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ContactForm(forms.ModelForm):
    Emp = forms.TextInput()
    InsNo = forms.TextInput()
    Loc= forms.TextInput()
    Working = forms.TextInput()
    Type = forms.TextInput()
    Comments = forms.TextInput()

    class Meta:
        model = metal_d
        fields = ('Emp','InsNo','Loc','Working','Type', 'Comments')


class HazardForm(forms.ModelForm):

    
    sh_wallnut =forms.TextInput()
    Desc= forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Description of the test', 'style': 'width: 300px;'}))

    #new row 
    rc_shwallnut=forms.TextInput()
    Desc2= forms.TextInput()

    #new row
    sorting=forms.TextInput()
    Desc3= forms.TextInput()
    

    ## new row 
    shelling=forms.TextInput()
    Desc4= forms.TextInput()

    # next row

    sizer=forms.TextInput()
    Desc5= forms.TextInput()

    class Meta:
        model = Hazard_material
        fields = ('sh_wallnut','Desc', 'rc_shwallnut', 'Desc1', 'sorting','Desc2', 'shelling','Desc3','sizer','Desc4')

class CheckIN(forms.ModelForm):
    Yn= (
        ('1', 'Yes'),
        ('2', 'No')
    )
    ill=forms.ChoiceField(label='Are you currently experiencing any illness, open lesions, or other abnormal sources of microbial contamination that could potentially contaminate food, food-contact surfaces, or food-packaging materials?', widget=forms.RadioSelect(), choices=Yn)
    garments=forms.ChoiceField(label='Have you put on the appropriate outer garments suitable for your job duties, in a manner that protects against contamination of food, food-contact surfaces, or food-packaging materials?', widget=forms.RadioSelect(), choices=Yn)
    wash=forms.ChoiceField(label='Have you washed your hands thoroughly (and sanitized if necessary to protect against contamination with undesirable microorganisms) in an adequate hand-washing facility before starting work, after each absence from the workstation, and at any other time when the hands may have become soiled or contaminated?', widget=forms.RadioSelect(), choices=Yn)
    jwelry=forms.ChoiceField(label=' Are all jewelry and objects secured or removed to prevent contamination of food or equipment? If hand jewelry cannot be removed, is it covered with clean material that effectively protects against contamination?', widget=forms.RadioSelect(), choices=Yn)
    hair=forms.ChoiceField(label='Are you wearing appropriate hair nets, headbands, caps, beard covers, or any other effective hair restraints in an effective manner during the manufacturing process?  ', widget=forms.RadioSelect(), choices=Yn) 
    food=forms.ChoiceField(label='Are you confining eating food, chewing gum, drinking beverages, or using tobacco to areas other than where food may be exposed or where equipment or utensils are washed?', widget=forms.RadioSelect(), choices=Yn)
    food_package=forms.ChoiceField(label='Have you taken all necessary precautions to protect against contamination of food, food-contact surfaces, or food-packaging materials with microorganisms or foreign substances including, but not limited to, perspiration, hair, cosmetics, tobacco, chemicals, and medicines applied to the skin?', widget=forms.RadioSelect(), choices=Yn)


    class Meta:
        model=Emp_wellness
        fields="__all__"



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user        
    


   



