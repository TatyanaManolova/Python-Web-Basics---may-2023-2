from django import forms

from fruitexam.fruitexam_app.models import ProfileModel, FruitModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image_url', 'age']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }


class ProfileDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = ProfileModel
        fields = '__all__'

    # def save(self, commit=True):
    #     if self.instance:
    #         self.instance.delete()
    #
    #     return self.instance


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class FruitCreateForm(FruitBaseForm):

    labels = {
        'name': '',
        'image_url': '',
        'description': '',
        'nutrition': ''
    }
    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
        'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
        'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
        'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
    }


class FruitEditForm(FruitBaseForm):
    labels = {
        'image_url': 'Image URL'
    }


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
