from django.urls import path

from accounts.views import profile_view

from .views import home, add_vacancy, edit_vacancy, delete_vacancy, \
    VacancyListView, VacancyDetailView, apply_to_vacancy, vacancy_applications , \
        update_application_status, notification_list, mark_as_read, edit_employer_profile_view, \
            chat_view, add_comment, SearchResultView

urlpatterns = [
    path('', home, name="home"),
    path('company/employer/profile/<int:user_pk>/edit/', edit_employer_profile_view, name="edit_employer_profile"),
    path('company/employer/profile/<int:user_pk>/vacancies/add/', add_vacancy, name="add_vacancy"),
    path('company/employer/profile/<int:user_pk>/vacancies/<int:pk>/edit/', edit_vacancy, name='edit_vacancy'),
    path('company/employer/profile/<int:user_pk>/vacancies/<int:pk>/delete/', delete_vacancy, name='delete_vacancy'),
    
    path('company/vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('company/vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('company/vacancies/<int:pk>/comment/', add_comment, name="add_comment"),
    path('company/vacancies/<int:pk>/apply/', apply_to_vacancy, name='apply_to_vacancy'),
    path('company/vacancies/<int:pk>/applications/', vacancy_applications, name='vacancy_applications'),
    path('company/application/<int:pk>/status/<str:status>/', update_application_status, name='update_status'),
    
    path('profile/<int:user_pk>/', profile_view, name='profile'),
    path('profile/<int:user_pk>/notifications/', notification_list, name='notification_list'),
    path('profile/<int:user_pk>/notifications/read/<int:pk>/', mark_as_read, name='mark_as_read'),
    path("chat/<int:application_pk>/", chat_view, name="chat_view"),
    
    path('search-results/', SearchResultView.as_view(), name="search_result"),
]