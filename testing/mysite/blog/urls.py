from django.urls import path
from blog import views
urlpatterns = [
    path('',views.PostListview.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>',views.PostDEtailView.as_view(),name='post_detail'),
    path('post/new/<int:pk>',views.PostCreateView.as_view(),name='post_new'),
    path('post/edit/<int:pk>',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/remove/<int:pk>',views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
    
]
