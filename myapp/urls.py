from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('destination/', views.destination, name='destination'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login_page, name='login'),

    path('signup/', views.signup, name='signup'),

    path('logout/', views.logout_view, name='logout'),

    path('agra/', views.agra, name='agra'),

   path('jaipur/', views.jaipur, name='jaipur'),

   path('kashmir/', views.kashmir, name='kashmir'),

   path('varanasi/', views.varanasi, name='varanasi'),

    path('goa/', views.goa, name='goa'),

    path('kerala/', views.kerala, name='kerala'),

    path('submit-review/<str:place_key>/', views.submit_review, name='submit_review'),

    path('ai-planner/', views.ai_planner, name='ai_planner'),

    path('item/<str:item_key>/', views.item_detail, name='item_detail'),

]