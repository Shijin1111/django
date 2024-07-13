import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'level1.settings')

import django
django.setup()

import random
from faker import Faker
from app1.models import student

fakegen = Faker() 

def populate(N=5):
    for i in range(N):
        fake_name = fakegen.name()
        fake_age = fakegen.random_int(max=75)
        s = student.objects.get_or_create(sname=fake_name,age=fake_age)[0]
        
populate(20)