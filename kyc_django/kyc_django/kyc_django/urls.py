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
    
    # update display function of records
    path('update', update, name="update"),

    # defined for  developing purposes
    path('select/', productList, name="select"),

    # get the selected user details in table of update.html
    path("update/<int:id>", update_data),

    #defined for backend data verification by admin reject or accept data
    path('edit/<int:id>', edit_val),


    path('insertkyc', insertkyc),
    #path('insertkyc1', insertkyc1)
    path('upload/', views.image_upload_view),

    # verify the email otp function in views
    path('verify/', views.verify, name="verify" ),
    
    # including url in kyc to kyc_djago
    path('', include("kyc.urls")),

    # diplay reject list in the html file
    path('reject/', views.reject, name="reject"),
    path('edit_reject/<int:id>', views.edit_val1, name="edit_reject"),
    path('update_history', update_history, name="update_history"),
    path('front', views.front),

    # new customer form set
    path('new_cus_form2', views.new_cus_form2),
    path('new_cus_form3', views.new_cus_form3),
    path('new_cus_form4', views.new_cus_form4),
    path('new_cus_form5', views.new_cus_form5),
    path('new_cus_form6', views.new_cus_form6),
    path('new_cus_form7', views.new_cus_form7),


    # exist_cus form set
    path('exist_cus_otp', views.exist_cus_otp),
    path('exist_cus_update_info', views.exist_cus_update_info),
    path('exist_cus_form', views.exist_cus_form),


    # social_score form set
    path('social_score', views.social_score)

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
