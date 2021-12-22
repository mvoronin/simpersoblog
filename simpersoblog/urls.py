from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.views import RootView
from blog.urls import urlpatterns as blog_patterns
from users.views import LoginView, LogoutView, UserChangeView

admin.site.site_header = 'Blog Admin Panel'
admin.site.site_title = 'Blog Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', RootView.as_view(), name='root'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/user-<int:pk>/edit', UserChangeView.as_view(), name='user-update'),
    path('', include(blog_patterns)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
