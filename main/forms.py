from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'service', 'budget', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Name',
                'id' : 'name'
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder' : 'you@gmail.com',
                'id' : 'email'
            }),
            'service' : forms.Select(attrs={
                'id' : 'service'
            }, choices = [
                ('','-- Select a service --'),
                ('ui', 'UI / UX Design'),
                ('web', 'Web Development'),
                ('django', 'SEO & Performance'),
                ('other', 'Other'),
            ]),          
            'budget' : forms.Select(attrs={
                'id' : 'budget'
            }, choices=[
                ('','-- Select budget range --'),
                ('5k', 'Under ₹5,000'),
                ('10k', '₹5,000 - ₹10,000'),
                ('25k', '₹10,000 - ₹25,000'),
                ('25k+', 'Above ₹25,000'),
            ]),
            'message' : forms.Textarea(attrs={
                'placeholder': 'Tell me about your project...',
                'rows': 5,
                'id': 'message'
            })
        }