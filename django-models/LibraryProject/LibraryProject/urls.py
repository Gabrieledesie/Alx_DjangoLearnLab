from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # This connects the app URLs
    path('', RedirectView.as_view(url='/bookshelf/', permanent=False)),
]
