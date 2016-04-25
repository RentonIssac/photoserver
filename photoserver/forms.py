from django import forms

class CheckMediaFileExistForm(forms.Form):
    owner = forms.CharField(label='Mediafile Owner')
    mediafile_size = forms.IntegerField(label='Mediafile Size')
    mediafile_name = forms.CharField( label='Mediafile Name' )

class MediaFileForm(forms.Form):
    owner = forms.CharField(label='Mediafile Owner')
    mediafile_size = forms.IntegerField(label='Mediafile Size')
    mediafile = forms.FileField( label='Mediafile' )
