import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_name.settings')


import django
django.setup()


import random
from appname.models import Topic,Webpage,AccessRecord
from faker import Faker

fakegen = Faker()
topic = ['search','social','marketplace','news','games']
def addTopic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = addTopic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        webpg =Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('poupulation completed')
