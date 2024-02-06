from django import forms 
from .models import Notes 

class new_note(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(new_note, self).__init__(*args, **kwargs)
        
        if user:
            self.fields['user'].initial = user
            
    class Meta: 
        model = Notes 
        fields = ('title', 'content' )

