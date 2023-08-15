from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name="home"),
    path('api/get-quiz/',views.get_quiz,name="get_quiz")
]
