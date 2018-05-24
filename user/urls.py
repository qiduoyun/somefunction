from django.urls import path

from .import views
app_name='user'
urlpatterns=[
    path('',views.UserBlogview.as_view(),name='index'),
    path('bloglist/<id>',views.BlogListview.as_view(),name='article'),
    path('upload/',views.UserFileview,name='upload'),
    path('download/<id>',views.download,name="download"),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('downloadlist/',views.dowmload_list.as_view(),name='download1')

]