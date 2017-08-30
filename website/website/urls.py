
from django.conf.urls import include, url
from django.contrib import admin

# use regular expression

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls'))
]
