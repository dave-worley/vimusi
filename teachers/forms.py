from django import forms

class TeacherProfileForm(forms.Form):
    availability = forms.CharField(max_length = 200)
    about = forms.CharField(widget=forms.Textarea)
    audio_sample = forms.FileField(required = False)
    profile_photo = forms.FileField(required = False)
    profile_video = forms.FileField(required = False)
