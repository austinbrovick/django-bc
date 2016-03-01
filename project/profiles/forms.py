from django import forms
from .models import UserProfile



class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30,
                                label="First Name",
                                required=True,
                                widget=forms.TextInput(attrs={"type" : "text",
                                                              "size" : "20",
                                                              "placeholder" : "First Name"}))
    last_name = forms.CharField(max_length=30,
                                label="Last Name",
                                required=True,
                                widget=forms.TextInput(attrs={"type" : "text",
                                                              "size" : "20",
                                                              "placeholder" : "Last Name"}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "profile_picture",
            "major",
            "grade"
        ]
