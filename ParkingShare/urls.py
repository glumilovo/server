from django.conf.urls import url, include
from django.contrib import admin
from ParkingShare.views import RegisterUser, loginUser, logautUser

urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^register/', RegisterUser),
      url(r'^login/', loginUser),
      url(r'^logout/', logautUser),
]



