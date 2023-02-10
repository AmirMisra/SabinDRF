from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('wla/', include('WatchList_app.api.urls')),
    path('account/', include('user_app.api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
