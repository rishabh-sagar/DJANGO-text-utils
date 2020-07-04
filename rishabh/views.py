# this is created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    rish = {'t1':"TEXT UTILS",'t2':'Rishabh sagar'}
    return render(request, 'index.html', rish)


def analyze(request):
    #return HttpResponse("hello1")
    #FOR GETTING TEXT
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    if removepunc=="on":
        analyzed_var=""
        punctuations='''!()-[]{};:'",<>./?@#$&_-%'''
        for a in djtext:
            if a not in punctuations:
                analyzed_var=analyzed_var+a
        param={'analyzed_text': analyzed_var}
        return render(request,'analyze.html',param)
        print(djtext)
        print(removepunc)
    elif(newlineremove=="on"):
        analyzed_var = ""
        for a in djtext:
            analyzed_var=analyzed_var+ a.upper()
        param = {'analyzed_text': analyzed_var}
        return render(request, 'analyze.html', param)

    elif (newlineremove == "on"):
        analyzed_var = ""
        for a in djtext:
            if(a!="\n"):
                analyzed_var = analyzed_var + a.upper()
        param = {'analyzed_text': analyzed_var}
        return render(request, 'analyze.html', param)

    else:
        return HttpResponse("<h3>ERROR Please Select One option </h3>")


# def capfirst(request):
#     return HttpResponse("hello2")
#
#
# def newlineremove(request):
#     return HttpResponse("hello3")
#
#
# def spaceremove(request):
#     return HttpResponse("hello4")
#
#
# def charcount(request):
#     return HttpResponse("hello5")
# # def about(request):
# #    return HttpResponse("hello about")
