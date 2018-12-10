from django.urls import  path
from   online  import  views


urlpatterns= [
    path('',views.mysite5,name='mysite5'),
    path('mysite5/',views.mysite5,name='mysite5'),

]