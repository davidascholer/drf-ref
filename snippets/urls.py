from django.urls import path, include
from snippets import views
# added for formatting
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# refactor our snippets/urls.py slightly now that we're using class-based views.

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

# added for formatting
urlpatterns = format_suffix_patterns(urlpatterns)