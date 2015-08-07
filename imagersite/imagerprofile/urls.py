from django.conf.urls import url
from .views import all_profiles_page, profile_page, edit_page

urlpatterns = [
    url(r'^$', all_profiles_page, name="profile_list"),
    url(r'^(?P<user_id>\d+)$', profile_page, name="profile_page"),
    url(r'^edit$', edit_page, name="profile_edit")
]
