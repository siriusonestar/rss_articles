from django.contrib import admin
from django.urls import path
from rss_feed import views

urlpatterns = [

    path('articles/', views.ArticlesFeed()),

]
