from django.urls import path
from . import views

urlpatterns = [

    path('',views.Salah,name='salah'),
    ]


handler404 = 'Contact_Salah.views.custom_page_not_found_view'
handler500 = 'Contact_Salah.views.custom_error_view'
handler403 = 'Contact_Salah.views.custom_permission_denied_view'
handler400 = 'Contact_Salah.views.custom_bad_request_view'

