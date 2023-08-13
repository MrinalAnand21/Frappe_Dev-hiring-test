from django import forms
from .models import Transaction


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['book', 'member', 'issued_date']
