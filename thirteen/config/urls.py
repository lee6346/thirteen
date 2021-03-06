"""thirteen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),

    # by default, django.contrib.auth.views.login tries to render /registration/login.html,
    # so we specify explicitly the template we'd like to use
    url(r'^login/', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/login'}, name='logout'),

    # angular partial/template URLs
    url(r'^partials/lobby/', views.lobby_partial, name='lobby'),
    url(r'^partials/table/', views.table_partial, name='table'),

    # angular modal partials
    url(r'^partials/CreateTableModal/', views.create_table_modal_partial, name='create_table_modal'),

   # post urls
    url(r'^CreateTable/', views.create_table, name='create_table'),

    #test
    url(r'^gettable/', views.get_tables, name='gettable'),
]
