from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required 
from . import models 
from . import forms 


@login_required 
def view_notes(request):
    user_notes = models.Notes.objects.filter(user = request.user)
    return render(request, 'templates/user/allNotes.html', {
        'user_notes':user_notes,
    })

@login_required
def new_notes(request):
    if request.method == 'POST':
        new_note_form = forms.new_note(request.POST)

        if new_note_form.is_valid:
            new_note = new_note_form.save(commit= False)
            new_note.user = request.user
            new_note.save()
            return redirect('/mynotes')
        
    new_note_form = forms.new_note()
    return render(request, 'templates/items/create.html', {
        'new_note':new_note_form, 
    })

def notes_details(request, id):
    note = get_object_or_404(models.Notes, pk =id)
    return render(request, 'templates/user/viewNotes.html',{
        'note':note,
    })