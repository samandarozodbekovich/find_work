from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views


from .views import register_view, profile_view,\
    edit_profile_view, CustomLoginView, CustomLogoutView,\
    add_skill_view, edit_skill_view, delete_skill_view, \
    add_portfolio_view, edit_portfolio_view, delete_portfolio_view, \
    add_certificate_view, edit_certificate_view, delete_certificate_view, \
    add_education_view, edit_education_view, delete_education_view, \
    add_experience_view, edit_experience_view, delete_experience_view,\
    add_language_view, edit_language_view, delete_language_view
from .views.posts import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
            
from .forms import CustomPasswordChangeForm, CustomSetPasswordForm
    

urlpatterns = [
    # registration
    path('register/', register_view, name="register"),
    path("profile/<int:user_pk>/", profile_view, name="profile"),
    path("profile/<int:user_pk>/edit/", edit_profile_view, name="edit_profile"),
    
    path('profile/<int:user_pk>/add/skill/', add_skill_view, name='add_skill'),
    path('profile/<int:user_pk>/edit/skill/<int:pk>/', edit_skill_view, name='edit_skill'),
    path('profile/<int:user_pk>/delete/skill/<int:pk>/', delete_skill_view, name='delete_skill'),
    
    path("profile/<int:user_pk>/add/language/", add_language_view, name="add_language"),
    path("profile/<int:user_pk>/edit/language/<int:pk>/", edit_language_view, name="edit_language"),
    path("profile/<int:user_pk>/delete/language/<int:pk>/", delete_language_view, name="delete_language"),
    
    path('profile/<int:user_pk>/add/portfolio/', add_portfolio_view, name='add_portfolio'),
    path('profile/<int:user_pk>/edit/portfolio/<int:pk>/', edit_portfolio_view, name='edit_portfolio'),
    path('profile/<int:user_pk>/delete/portfolio/<int:pk>/', delete_portfolio_view, name='delete_portfolio'),
    
    path('profile/<int:user_pk>/add/certificate/', add_certificate_view, name='add_certificate'),
    path('profile/<int:user_pk>/edit/certificate/<int:pk>/', edit_certificate_view, name='edit_certificate'),
    path('profile/<int:user_pk>/delete/certificate/<int:pk>/', delete_certificate_view, name='delete_certificate'),
    
    path('profile/<int:user_pk>add/education/', add_education_view, name="add_education"),
    path('profile/<int:user_pk>edit/education/<int:pk>/', edit_education_view, name="edit_education"),
    path('profile/<int:user_pk>delete/education/<int:pk>/', delete_education_view, name="delete_education"),
    
    path('profile/<int:user_pk>add/experience/', add_experience_view, name="add_experience"),
    path('profile/<int:user_pk>/edit/experience/<int:pk>/', edit_experience_view, name='edit_experience'),
    path('profile/<int:user_pk>/delete/experience/<int:pk>/', delete_experience_view, name='delete_experience'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    
    # passwords
    path('password-change/', auth_views.PasswordChangeView.as_view(
        form_class=CustomPasswordChangeForm,
    ), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
    ), name='password_change_done'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html',
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html',
    ), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        form_class=CustomSetPasswordForm
    ), name='password_reset_confirm'),

    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html',
    ), name='password_reset_complete'),
]

# posts
urlpatterns += [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('profile/<int:user_pk>/add/post/', PostCreateView.as_view(), name='add_post'),
    path('profile/<int:user_pk>/edit/post/<int:pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('profile/<int:user_pk>/delete/post/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
]
