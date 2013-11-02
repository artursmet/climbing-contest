#coding: utf-8
from django import forms

from contest.models import Contestant, Group
from captcha.fields import ReCaptchaField


class ContestantForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
        empty_label=u"Wybierz grupę", label="Grupa")
    captcha = ReCaptchaField()

    class Meta:
        model = Contestant

    def __init__(self, contest, *args, **kwargs):
        super(ContestantForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.filter(contest=contest)

    def clean_group(self):
        group = self.cleaned_data['group']
        if group.contestants_count + 1 > group.capacity:
            raise forms.ValidationError(u"Ta grupa jest już pełna!")
        
        return group
