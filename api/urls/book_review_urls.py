from django.urls import path

from api.views.book_review_views import *

app_name = 'book_review'

urlpatterns = [
    path('add/', add_review, name='add'),
    path('edit/<int:pk>/', edit_review, name='edit'),
    path('all/', get_all_reviews, name='all'),
    path('get/<int:pk>/', get_review, name="one"),
    path('delete/<int:pk>/', delete_review, name='delete'),
    #path('deletetag/<int:pk>/',delete_tag, naem='deletetag')
]
