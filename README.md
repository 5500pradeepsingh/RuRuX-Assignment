
Attached Demo Video ->

https://github.com/user-attachments/assets/04be6e63-cf09-441c-adf7-764ea28de902

Web page URL->

> Access Fan Control:
Go to http://127.0.0.1:8000/fan/control/ to test the fan simulator.

> Check Energy Consumption:
Go to http://127.0.0.1:8000/fan/consumption/ to check power and energy consumption between two time intervals.

=================================================================================================================

Project Setup->

> Install Django and PostgreSQL:
pip install django
pip install django psycopg2

> Run Migrations:
python manage.py makemigrations
python manage.py migrate

> Run the server:
python manage.py runserver

> Insert Fan Specifications in Django Shell:
python manage.py shell

from fan.models import FanSpecification

FanSpecification.objects.bulk_create([
    FanSpecification(speed_level=1, current=0.63),
    FanSpecification(speed_level=2, current=0.69),
    FanSpecification(speed_level=3, current=0.74),
    FanSpecification(speed_level=4, current=0.89),
    FanSpecification(speed_level=5, current=0.97),
])

