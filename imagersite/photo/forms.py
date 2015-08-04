from django import forms
from photo.models import Photos, Album
from imagerprofile.models import ImagerProfile


class ImagerForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.photo_owner = user
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    def save(self):
        this = super(forms.ModelForm, self).save()
        profile = self.photo_owner.profile
        if self.Meta.model is Photos:
            profile.photos.add(this)
        elif self.Meta.model is Album:
            profile.albums.add(this)
        else:
            raise TypeError(
                "Cannot create ImagerForm with Meta class model of " + str(type(this))
            )
        ImagerProfile.save(profile)
        return this


class PhotoForm(ImagerForm):
    class Meta:
        model = Photos
        fields = ["image", "title", "description"]


class AlbumForm(ImagerForm):
    class Meta:
        model = Album
        fields = ["title", "description"]
