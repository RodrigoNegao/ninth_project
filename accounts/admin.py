from django.contrib import admin
from .models import User , Profile

#python manage.py makemigrations accounts
#python manage.py migrate accounts
#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser

# SuperUserInformation
# Email: rodrigo@rodrigo.com
# User: Rpereira
# birth_date: 01/01/1900
# Password: 0123456 or 301202
#User: dede@dede.com
# Password: 01

# Register your models here.
# admin.site.register(example)
admin.site.register(User) #, Profile)
admin.site.register(Profile)
