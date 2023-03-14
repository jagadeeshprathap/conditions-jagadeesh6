from django.shortcuts import render

# Create your views here.
def ammu(request):
    d={'a':122,'b':336,'c':332}
    return render(request,'condition.html',d)