
from django.http import HttpResponse
from django.shortcuts import render 
import operator


def homepage(request):
	return render(request,'home.html')

def count(request):
	msg = request.GET['fulltext']
	worddict = {}
	wordlist = msg.split()
	#print(len(wordlist))

	for w in wordlist:
		if w in worddict:
			worddict[w] += 1
		else:
			worddict[w] = 1

	sortedwords = sorted(worddict.items(), key = operator.itemgetter(1) , reverse = True)
	return render(request,'count.html',{'msgkey':msg,'countkey':len(wordlist),'worddict':sortedwords})

def aboutpage(request):
	return render(request,'about.html')