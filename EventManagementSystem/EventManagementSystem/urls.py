"""
URL configuration for EventManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from EventManagementSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name='landing'),
    path('signup/',views.signup, name='signup'),
    path('success/',views.success, name='success'),
    path('login/',views.login,name='login'),
    path('forgot-password/',views.forgot_password,name='forgot_password'),
    path('thank-you/',views.thank_you,name='thank_you'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('attendees/',views.attendees,name='attendees'),
    path('events/',views.events,name='events'),
    path('overview/',views.overview,name='overview'),
    path('settings/',views.settings,name='settings'),
    path('ticket_sales/',views.ticket_sales,name='ticket_sales'),
    path('add_events/',views.add_event,name='add_event'),
    path('logout/', views.logout, name='logout'),
    path('view_event/<str:event_name>/',views.view_event,name='view_event'),
    path('edit_event/<str:event_name>/',views.edit_event,name='edit_event'),
    path('delete_event/<str:event_name>/', views.delete_event, name='delete_event'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

