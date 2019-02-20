from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
import portfolio.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/',include('blogapp.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('admin/portfolio/portfolio/add/', portfolio.views.newone, name="newone"),
    path('accounts/', include('accounts.urls')),
    path('accounts/social/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 이라고써도됨