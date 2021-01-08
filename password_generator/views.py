from django.shortcuts import render
import string
import random


def generator(request):
    return render(request, 'password_generator/generator.html')


def password(request):
    length = int(request.GET.get('length', 12))

    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    numbers = string.digits
    puncts = ",./'~#$%&*"

    pool = lowers

    if request.GET.get('upper'): pool += uppers
    if request.GET.get('number'): pool += numbers
    if request.GET.get('special'): pool += puncts

    password = ''.join(random.choice(pool) for i in range(length))

    return render(request, 'password_generator/password.html', {'password': password})
