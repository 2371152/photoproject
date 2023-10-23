from django.urls import path
from .import views

app_name = 'photo'

urlpatterns = [path('', views.IndexView.as_view(), name='index'),
               # p446
               path('post/', views.CreatePhotoView.as_view(), name='post'),
               path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
               # p475
               path('photos/<int:category>',
                    views.CategoryView.as_view(), name='photos_cat'),
               # p481
               path('user-list/<int:user>',
                    views.UserView.as_view(), name='user_list'),
               # p488
               path('photo-detail/<int:pk>',
                    views.DetailView.as_view(), name='photo_detail'),
               # p497
               path('mypage/', views.MypageView.as_view(), name='mypage'),
               # p505
               path('photo/<int:pk>/delete/',
                    views.PhotoDeleteView.as_view(), name='photo_delete'),
               ]
