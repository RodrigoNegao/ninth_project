from django import forms
from .models import ResumeUser

class NewResumeUserForm(forms.ModelForm):
    class Meta:
        model = ResumeUser
        fields = '__all__'
        # help_texts = {
        #     'first_name': ('Some useful help text.'),
        #     }
        # widgets = {
        #         'first_name':forms.TextInput(
        #         attrs={'size': 5,'class':'form-control','placeholder':'Roberto'}
        #         ),
        #         'last_name':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'nphone1':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'nphone2':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'email':forms.TextInput(
        #         attrs={'type':'email','class':'form-control','placeholder':'email@email.com'}
        #         ),
        #         'driverslicense':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'address':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'neighborHood':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'city':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'state':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'zip':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'maritalStatus':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'levelStudy':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'lInstitution':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'lyearFinish':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'course':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'cInstitution':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'cyearFinish':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'studyTime':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'company':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'function':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'worktime':forms.TextInput(
        #         attrs={'class':'form-control'}
        #         ),
        #         'functionDescribe':forms.Textarea(
        #         attrs={'class':'form-control'}
        #         ),
        #     }
