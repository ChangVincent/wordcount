from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'apple': 'made from Taiwan'})


def eggs(request):
    return HttpResponse('Eggs are great')


def count(request):
    fulltext = request.GET['fulltext']
    dict = {}

    wordlist = fulltext.split()
    for word in wordlist:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    sortedWords = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'wordlist': wordlist, 'count': len(wordlist), 'dict': sortedWords})


def about(request):
    return render(request, 'about.html')
