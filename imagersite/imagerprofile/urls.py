from django.conf.urls import url
from .views import all_profiles_page, profile_page

urlpatterns = [
    url(r'^$', all_profiles_page),
    url(r'^(?P<user_id>\d+)$', profile_page)
]
