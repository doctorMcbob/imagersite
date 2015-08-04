from django import forms
from photo.models import Photos, Album
from imagerprofile.models import ImagerProfile


class ImagerForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.photo_owner = user
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        this = super(forms.ModelForm, self).save(*args, **kwargs)
        if self.Meta.model is Album:
            for photo in self.cleaned_data["photos"]:
                this.photos.add(photo)
        this.user = self.photo_owner
        this.save()

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
        fields = ["image", "title", "description", "published"]


class AlbumForm(ImagerForm):
    class Meta:
        model = Album
        fields = ["title", "description", "cover", "published", "photos"]

    def __init__(self, user, *args, **kwargs):
        super(AlbumForm, self).__init__(user, *args, **kwargs)
        self.fields["photos"] = forms.ModelMultipleChoiceField(
            queryset=user.profile.photos.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )
