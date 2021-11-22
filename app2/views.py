from django.shortcuts import render

def jinja1(request):
    d={'a':290, 'b':34, 'c':23}
    return render(request, 'h2.html', context=d)
