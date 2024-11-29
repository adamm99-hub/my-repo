from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Person
from django.shortcuts import render


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def person_list(request):
    # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
    persons = Person.objects.all()
    return render(request,
                  "myapp/person/list.html",
                  {'persons': persons})
