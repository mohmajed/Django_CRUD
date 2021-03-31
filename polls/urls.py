from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #path('', views.index, name='index'),
    path('register/',views.register_page,name="register"),
    path('login/',views.login_page, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('', views.home,name="home"),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create_vacation/',views.create_vacation,name="create_vacation"),
    path('update_vacation/<str:pk>/',views.update_vacation,name="update_vacation"),
]
