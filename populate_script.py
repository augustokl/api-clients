# autopep8: off
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from client.models import Client

def create_persons(quantity):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower().split()[0], fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(
            100, 999), random.randrange(100, 999), random.randrange(0, 9))
        celphone = "{} 9{}-{}".format(random.randrange(10, 21),
                                      random.randrange(4000, 9999), random.randrange(4000, 9999))
        is_active = random.choice([True, False])
        p = Client(name=name, email=email, cpf=cpf, rg=rg,
                   celphone=celphone, is_active=is_active)
        p.save()


create_persons(75)
print('Success!')
