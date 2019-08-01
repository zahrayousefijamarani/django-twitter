from django.urls import path

from awesomeTwitter import views

app_name = 'twitter'
urlpatterns = [
    path('', views.main_page, name='main'),
    path('profile/<int:Id>/', views.go_profile, name='go_profile'),
    path('profile/message/<int:Id>', views.messaging, name="message"),
    path('profile/delete/<int:pId>/<int:mId>/',views.deleting,name="delete")

]
