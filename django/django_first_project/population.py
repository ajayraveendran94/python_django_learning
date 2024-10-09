import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_first_project.settings')

import django
# Import settings
django.setup()
import random
from first_app.models import Topic,Webpage,AccessRecord
from faker import Faker
fake = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        top = add_topic()

        
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        accRec = AccessRecord.objects.get_or_create(page=webpg,date=fake_date)[0]


if __name__ == '__main__': #if the script is being run directly and to the name of the module
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
