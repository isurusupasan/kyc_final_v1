"""kyc_django URL Configuration

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
from django.urls import path, include
from kyc import views
from kyc.views import index, update_history
from kyc.views import office, personal, account, insertkyc, update, edit_val, update_data, image_upload_view, productList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    path('office', office),
    path('personal', personal),
    path('account', account),
    path('update', update, name="update"),
    path('select/', productList, name="select"),
    path("update/<int:id>", update_data),
    path('edit/<int:id>', edit_val),
    path('insertkyc', insertkyc),
    #path('insertkyc1', insertkyc1)
    path('upload/', views.image_upload_view),
    path('verify/', views.verify, name="verify" ),
    
    path('', include("kyc.urls")),
    path('reject/', views.reject, name="reject"),
    path('edit_reject/<int:id>', views.edit_val1, name="edit_reject"),
    path('update_history', update_history, name="update_history"),
    path('front', views.front)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
