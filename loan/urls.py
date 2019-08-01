from django.urls import path

from loan import views

app_name = 'loan'
urlpatterns = [
    path('', views.loan, name='loan'),
    path('signup/', views.signup, name="signup"),
    path('submit/', views.submit, name='submit'),
    path('homepage/<int:id>/', views.homepage, name='homepage'),
    path('chooseLoan/<int:id>', views.choose_loan, name='chooseLoan'),
    path('pay/<int:id>', views.pay, name='pay'),
    path('allocate/<int:Id>', views.allocate, name='allocate')
]
