#OWN...
from django.shortcuts import render
from django.http import HttpResponse
# def index(request):
#     params = {'name':'your_name'}
#     return render(request, 'index.html', params)
def index(request):
    return render(request, 'index.html')


def eg(request):
    text = request.POST.get('textarea', 'default')
    j = 0
    var = ''
    for i in text:
        if i == '\n':
            j += 1
            var += '\n'
        else:
            var += i
    params = {'purpose': 'testing', 'x': j, 'y': text, 'z': var}
    return render(request, 'analyze.html', params)


def remove(string):
    var = ''
    punc = '''.,?!:;-_()[]{}"'./\&*$%#@+-=><~|^•©®™'''
    for i in string:
        if punc.find(i) == -1:
            var += i
    return var

def caps(string):
    return string.upper()

def count(string):
    var = 'Character Count = '+str(len(string))
    return var
    


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    
    # print(djtext)
    if removepunc == 'on' and fullcaps == 'on' and charcount == 'on':
        params = {'purpose':'Remove Punctuations, Capitalization & Character Counter', 'x': remove(djtext), 'y': caps(djtext), 'z': count(djtext)}
        return render(request, 'analyze.html', params)
    
    elif removepunc == 'on' and fullcaps == 'on':
        params = {'purpose': 'Remove Punctuation & Capitalization', 'x': remove(djtext), 'y': caps(djtext)}
        return render(request, 'analyze.html', params)
    
    elif removepunc == 'on' and charcount == 'on':
        params = {'purpose': 'Remove Punctuation & Character Counter', 'x': remove(djtext), 'y': count(djtext)}
        return render(request, 'analyze.html', params)
    
    elif fullcaps == 'on' and charcount == 'on':
        params = {'purpose': 'Capitalization & Character Counter', 'x': caps(djtext), 'y': count(djtext)}
        return render(request, 'analyze.html', params)

    elif removepunc == 'on':
        params = {'purpose':'Remove Punctuation', 'x': remove(djtext)}
        return render(request, 'analyze.html', params)
       
    elif fullcaps == 'on':
        params = {'purpose':'Capitalization', 'x': caps(djtext)}
        return render(request, 'analyze.html', params)
        
    elif charcount == 'on':
        params = {'purpose': 'Character Counter', 'x':count(djtext)}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Error")

# def str(request):
#     return HttpResponse("<form>"
#                         "<input placeholder='Enter the string'>"
#                         "<button>generate</button>"
#                         "</form>")