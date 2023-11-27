from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:my_id>', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:my_id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:my_id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    # path('<int:my_id>/', dynamic_lookup_view, name='product'),
    # path('<int:my_id>/delete/', product_delete_view, name='delete'),
    # path('all-list/', product_list_view, name='product_list'),
    # path('', product_detail_view, name='detail'),
    # path('create/', product_create_view, name='create'),
]