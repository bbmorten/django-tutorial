mkdir django-tutorial
cd django-tutorial
pipenv --python 3.9.5
pipenv install Django


django-admin startproject mysite



# Management commands
python manage.py runserver


# Adding an application
python manage.py startapp polls


# Models
python manage.py migrate
python manage.py makemigrations polls 

python manage.py sqlmigrate polls 0001
python manage.py check

/*
Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
*/


python manage.py shell
/* Shell 
from polls.models import Choice, Question  # Import the model classes we just wrote.
from django.utils import timezone

Question.objects.all()

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text

q.pub_date
q.question_text = "What's up?"
q.save()

Question.objects.all()


Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
current_year = timezone.now().year

Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)

Question.objects.get(pk=1)
q = Question.objects.get(pk=1)
q.was_published_recently()

q.choice_set.all()


q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

c.question
q.choice_set.all()
q.choice_set.count()
Choice.objects.filter(question__pub_date__year=current_year)
c = q.choice_set.filter(choice_text__startswith='Just hacking')


*/


python manage.py createsuperuser


Running Tests

python manage.py test polls


The Django test client¶

Django provides a test Client to simulate a user interacting with the code at the view level. We can use it in tests.py or even in the shell.

from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
# create an instance of the client for our use
client = Client()
# get a response from '/'
response = client.get('/')
# we should expect a 404 from that address; if you instead see an
# "Invalid HTTP_HOST header" error and a 400 response, you probably
# omitted the setup_test_environment() call described earlier.
response.status_code
# on the other hand we should expect to find something at '/polls/'
# we'll use 'reverse()' rather than a hardcoded URL
from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']




https://www.selenium.dev/

https://en.wikipedia.org/wiki/Continuous_integration

https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#topics-testing-code-coverage

https://docs.djangoproject.com/en/3.2/topics/testing/

