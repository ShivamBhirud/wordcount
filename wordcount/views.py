from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def home(request):
  return render(request, 'home.html')

def count(request):
  text = request.GET['Text']
  wordlist = text.split()
  worddict = {}
  worddict = Counter(wordlist)
  worddict = dict(worddict.most_common())
  return render(request, 'count.html', {'counterdict':text, 'count':len(wordlist), 'worddict': worddict.items()})

def about(request):
  return render(request, 'about.html')