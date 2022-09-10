### Hi In this page i am workig on it - chinmay

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File

def index(request):
    mydic={'name':'Chinmay','place':'Pune'}
    return render(request,'index.html',mydic)
    # return HttpResponse('''<center>Home Page</center>''')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')

    # Check this values in checkbox
    removepunc=request.POST.get('removepunc','default')
    fullcaps=request.POST.get('fullcaps','default')
    newlineremover=request.POST.get('newlineremover','default')
    spaceremover=request.POST.get('spaceremover','default')
    charcount=request.POST.get('charcount','default')
    strslice=request.POST.get('strslice','default')

    # Check which checkbox is on
    if removepunc =="on":
        analyzed =""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed= analyzed + char.upper()

        params = {'purpose': 'UPPER CASE The Text', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New LineRemoved', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover =="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]== " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space is removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount=="on":
        analyzed=len(djtext)
        params = {'purpose': 'Total Count', 'analyzed_text': analyzed}
        djtext = analyzed

    if strslice=="on":
        try:
            analyzed = ""
            start=request.POST.get('start','default')
            end=request.POST.get('end','default')
            analyzed=djtext[int(start):int(end)+1]
            params ={'purpose': 'String Slicing', 'analyzed_text': analyzed}
        except Exception as e:
            print(e)

    if removepunc !="on" and fullcaps !="on" and newlineremover !="on" and spaceremover !="on" and charcount !="on" and strslice !="on":
        return HttpResponse("Please select any one option for execution")

    return render(request, 'analyze.html', params)
