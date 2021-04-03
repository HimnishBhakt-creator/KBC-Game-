from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.home_page, name='home_page'),
    path('2',views.Q2,name='Q2'),
    path('3',views.Q3,name='Q3'),
    path('4',views.Q4,name='Q4'),
    path('5',views.Q5,name='Q5'),
    path('6',views.Q6,name='Q6'),
    path('7',views.Q7,name='Q7'),
    path('8',views.Q8,name='Q8'),
    path('9',views.Q9,name='Q9'),
    path('10',views.Q10,name='Q10'),
    path('index',views.home_page, name='home_page'),
    path('lost',views.lost,name='lost'),
    path('win',views.win,name="win"),
    path('quit',views.quit,name="quit")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)