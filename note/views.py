from django.shortcuts import render

from .models import Note
def index(request):
    list = Note.objects.all()
    context = {'list': list}
    return render(request, 'note/index.html', context)