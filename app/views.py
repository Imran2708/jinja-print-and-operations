from django.shortcuts import render

def jinja_print(request):
    d={'name':'Imran', 'age':22}
    return render(request, 'h1.html', context=d)


def operations(request):
    d={'a':10,'b':20}
    return render(request,'h1.html', context=d)

