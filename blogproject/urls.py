
from django.contrib import admin
from django.urls import path,include
import blog.views
from django.conf import settings #media 사용을 위해 외우기
from django.conf.urls.static import static #media사용을 위해 외우기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name ='home'),
    path('blog/',include('blog.urls')),
    path('accounts/', include('account.urls')),
]

