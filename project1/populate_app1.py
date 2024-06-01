import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'project1.settings')

import django
django.setup()

import random
from faker import Faker
from app1.models import User

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        fake_fname = fakegen.first_name
        fake_lname = fakegen.last_name
        fake_mail = fakegen.email
        user = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_mail)

