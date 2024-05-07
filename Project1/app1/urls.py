# urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import signup



urlpatterns = [
    path("add/", views.details, name="add_patient"),
    path("patient/<str:Name>/", views.display, name="view_patient"),
    path('all/', views.view_all_patients, name='view_all_patients'),
    path('filter/', views.filter_patients, name='filter_patients'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('all/<slug:id>/',views.view_single, name='view_single'),
    path('view_patient/<slug:Name>/',views.view_patient,name="view_patient"),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    # Add other paths as needed
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
