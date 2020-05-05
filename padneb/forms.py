from django import forms
from .models import Member, Contribution


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('chapter', 'first_name', 'middle_initial', 'last_name', 'email', 'admission_date', 'gender',
                  'marital_status', 'in_pad_social', 'date_admitted', 'cellPhone', 'homePhone', 'address',
                  'city', 'state', 'zip')


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ('member', 'date', 'amount', 'type', 'comments')
