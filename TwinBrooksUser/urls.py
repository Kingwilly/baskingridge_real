from django.conf.urls import url
from TwinBrooksUser.views import edit_profile_information, edit_profile_photo

urlpatterns = [
    url(r'^$', edit_profile_information, name='edit_profile_information'),
    url(r'^change-photo/$', edit_profile_photo, name='edit_profile_photo'),

]
