from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url('posts/', include('posts.urls')),
    url('admin/', admin.site.urls),
    url(r'^', include('posts.urls'))
]