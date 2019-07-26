from django.urls import path

from loan import views

app_name = 'loan'
urlpatterns = [
    path('', views.loan, name='index'),
    path('signup/', views.signup, name="signup"),
    path('submit/', views.submit, name='submit'),
    path('homepage/<int:id>/', views.homepage, name='homepage')
]
