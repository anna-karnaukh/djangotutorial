import math
import csv

from django.shortcuts import render


def square(request):
    #Square Equations
    params = {}
    params['a'] = float(request.GET['a'])
    params['b'] = float(request.GET['b'])
    params['c'] = float(request.GET['c'])
    discr = params['b']**2 - 4 * params['a'] * params['c'];
    if discr > 0:
        params['x1'] = (-params['b'] + math.sqrt(discr)) / (2 * params['a'])
        params['x2'] = (-params['b'] - math.sqrt(discr)) / (2 * params['a'])
    elif discr == 0:
        params['x'] = -params['b'] / (2 * params['a'])
    else:
        params['error'] = True
    return render(request, "nine/square.html", params)

def heroes(request):
    with open('nine/data.csv', 'r') as csvfile:
        heroes = list(csv.reader(csvfile))
    return render(request, 'nine/heroes.html', {
        'header': heroes[0], 'herodata': heroes[1:],})

def hero(request, hero):
    with open('nine/data.csv', 'r') as csvfile:
        heroes = list(csv.reader(csvfile))
    for item in heroes:
        if item[5]==hero:
            return render(request, 'nine/hero.html',{"hero":item})

