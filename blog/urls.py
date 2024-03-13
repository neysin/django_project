from django.urls import path
from . import views
from .views import PostList, PostDetail, PostCreate, PostUpdate, DeleteView, CommentUpdate

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='postlist'),
    path('<int:pk>/', PostDetail.as_view(), name='postdetail'),
    path('write/', PostCreate.as_view(), name='postwrite'),
    path('edit/<int:pk>', PostUpdate.as_view(), name='postedit'),
    path('delete/<int:pk>', DeleteView.as_view(), name='postdelete'),
    path('<int:pk>/new_comment/', views.new_comment, name='new_comment'),
    path('update_comment/<int:pk>/', CommentUpdate.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
]
