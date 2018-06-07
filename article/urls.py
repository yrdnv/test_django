from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<pk>', views.DetailArticleView.as_view(), name='article')
    path('<pk>', views.article, name='article')

]