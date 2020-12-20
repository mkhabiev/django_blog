from django.forms import ModelForm
from users.models import Profile

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = [
            'name',
            'sex',
            'age',
            'hobby',
            'image',
            'about',
        ]