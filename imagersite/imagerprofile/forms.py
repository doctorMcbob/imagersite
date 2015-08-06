from django import forms
from imagerprofile.models import ImagerProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ImagerProfile
        fields = ['fav_camera', 'address', 'url', 'photo_type']
