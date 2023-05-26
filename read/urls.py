from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from read import views

# from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

print(router.urls)

urlpatterns = router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     # FUNCTION BASE VIEW URLS
#     # path('authors/', views.display_authors),
#     # # path('response', views.welcome),
#     # path('authors/<int:pk>/', views.author_detail, name='author-detail'),
#     # path('authors/', views.AuthorList.as_view()),
#     # path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
#     #  BOOKS::::::
#     path('books/<int:pk>', views.book_detail),
#     path('books/', views.BookList.as_view()),

#     ]
# Django Debug Toolbar helps with speed Install it
