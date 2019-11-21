from django import forms
from .models import User , Profile
from django.forms.widgets import ClearableFileInput
#update
# from django.forms import ModelForm
# from django.views.generic.edit import UpdateView

# class CustomClearableFileInput(ClearableFileInput):
#     def get_context(self, name, value, attrs):
#         value.name = path.basename(value.name)
#         context = super().get_context(name, value, attrs)
#         return context

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','username','birth_date','password','password2')

    password = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text = ("Enter the same password as above, for verification."))

    # Check if passwords match
    def clean_password2(self):
        password = self.cleaned_data.get("password", "")
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError(['password_mismatch'])
        return password

    # Check username is unique
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(['duplicate_username'])

class updateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','birth_date')

class updateAvatarForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('avatar',)

class updatePicResumeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('picresume',)

class updateImageResumeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('imageresume',)
