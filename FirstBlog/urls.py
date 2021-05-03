from django.urls import path
#from . import views
from .views import HomeView
from .views import ArticleDetailView
from .views import AddPostView
from .views import UpdatePostView
from .views import DeletePostView
from .views import AddCategoryView, CategoryView
from .views import AddCommentView

#urlpatterns = [
    
 #   path ('', views.home, name="home"),
#]


urlpatterns = [
    
    path ('', HomeView.as_view(), name="home"),
    path ('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path ('add_post/', AddPostView.as_view(), name='add_post'),
    path ('add_category/', AddCategoryView.as_view(), name='add_category'),
    path ('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path ('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/',CategoryView,name='category'),
   	path ('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),

]

