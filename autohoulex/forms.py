from django import forms
from .models import Orders, ContactMessage, Comment, Post, Orders, Make, Model, Year


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'pick_up_location', 'delivery_location', 'open_enclosed', 'operable',
            'make', 'model', 'year', 'name', 'email', 'phone_number', 'date', 'condition'
        ]

    # Customizing widgets if needed
    pick_up_location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter pick-up city or ZIP code'
    }))

    delivery_location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter delivery city or ZIP code'
    }))

    make = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Car make (company)'
    }))

    model = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Car model'
    }))

    year = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Car year'
    }))
    
    operable = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=Orders.OPERABLE
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your full name'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your email address'
    }))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your phone number'
    }))

    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the date (YYYY-MM-DD)',
        'type': 'date'
    }))

    condition = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }), required=False)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'message', 'condition']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Leave us a message...',
                'rows': 4,
            }),
            'condition': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'publish', 'image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title here',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the slug here',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the post content here',
            }),
            'publish': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment',
            }),
        }
