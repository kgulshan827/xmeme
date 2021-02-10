	
from django.urls import path
from .views import MemeAPIView, MemeDetails
from .import views
urlpatterns = [
    path('meme_input',views.meme_input,name="meme_input"),
    path('',views.meme_list,name="list"),
    path('memes/',MemeAPIView.as_view(),name="meme"),
    path('memes/<int:id>/', MemeDetails.as_view()),
    path('search',views.search,name="search")
 
    
]
