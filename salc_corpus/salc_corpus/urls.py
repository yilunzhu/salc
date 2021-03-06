"""salc_corpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from login import views as login_views
from login import urls as login_urls
from corpus import views as corpus_views
from corpus import urls as corpus_urls
from django.views.generic import RedirectView

# url for admin
urlpatterns = [
    path('admin/', admin.site.urls),
]

# add first app
# urlpatterns += [
#     path('login/',include(login_urls))
# ]
urlpatterns += [
    path('index/', login_views.index, name='index'),
    path('login/', login_views.login, name='login'),
    path('login_corpus/', login_views.login_corpus, name='login_corpus'),
    path('logout/', login_views.logout, name='logout'),
]

# redirect the home url to login index
urlpatterns += [
    path('', RedirectView.as_view(url='index/')),
]

# add second app
# urlpatterns += [
#     path('corpus/',include(corpus_urls))
# ]