from django.urls import path
from .views import BookClass,aClass,bClass,cClass,dClass,eClass,fClass,gClass,hClass,iClass,jClass,kClass
urlpatterns = [
    # path('bookurl/', bookfunc),
    path('c1/', BookClass.as_view(),name="c1"),
    path('confirm/', aClass.as_view(),name="confirm"), 
    path('contact/', bClass.as_view(),name="contact"),    
    path('discography/', cClass.as_view(),name="discography"),    
    path('event/', dClass.as_view(),name="event"),    
    path('finish/', eClass.as_view(),name="finish"),    
    path('form/', fClass.as_view(),name="form"),    
    path('index/', gClass.as_view(),name="index"),    
    path('index2/', hClass.as_view(),name="index2"),    
    path('news/', iClass.as_view(),name="news"),    
    path('profile/', jClass.as_view(),name="profile"),    
    path('readme/', kClass.as_view(),name="readme"),    
]