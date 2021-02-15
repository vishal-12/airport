# from django.urls import path

from django.conf.urls import url
from Lounge import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'Lounge'

urlpatterns = [
    url(r'^delhi/', views.LoungeListView.as_view()),
    url(r'^add-airport/', views.LoungeView.as_view()),
    url(r'^delete/(?P<pk>\d+)', views.LoungeView.as_view(), name='delete_event'),
    url(r'^update/(?P<pk>[0-9]+)$', views.LoungeView.as_view()),
    url(r'^delete-all/', csrf_exempt(views.delete_all)),
]
