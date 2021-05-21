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

