from django.shortcuts import render
import random

# Create your views here.

fortuneList = ['Ahlaklı insan olmak bir erdemdir. Ama aynı zamanda enayiliktir eğer kötüler ortamda cirit atıyorsa.  ',
'Lan bırak. Git artık buralardan. Fortune bla bla']

def fortune(request):
    fortune = random.choice(fortuneList)
    context = {"fortune" : fortune}
    return render(request, 'randomfortune/fortune.html', context)

pets = [
  { "petname": "Fido", "animal_type": "dog"},
  { "petname": "Clementine", "animal_type": "cat"},
  { "petname": "Cleo", "animal_type": "cat"},
  { "petname": "Oreo", "animal_type": "dog"},
]

def home(request):
    context = {"name": "Djangoer", "pets": pets}
    return render(request, 'randomfortune/home.html', context)
