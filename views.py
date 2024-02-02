from django.shortcuts import render
from django.views.generic import TemplateView

class BookClass(TemplateView):
    template_name = 'book/c1.html'

class aClass(TemplateView):
    template_name = 'book/confirm.html'

class bClass(TemplateView):
    template_name = 'book/contact.html'

class cClass(TemplateView):
    template_name = 'book/discography.html'

class dClass(TemplateView):
    template_name = 'book/event.html'

class eClass(TemplateView):
    template_name = 'book/finish.html'

class fClass(TemplateView):
    template_name = 'book/form.html'

class gClass(TemplateView):
    template_name = 'book/index.html'

class hClass(TemplateView):
    template_name = 'book/index2.html'

class iClass(TemplateView):
    template_name = 'book/news.html'

class jClass(TemplateView):
    template_name = 'book/profile.html'

class kClass(TemplateView):
    template_name = 'book/readme.html'


# Create your views here.
