from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from secret_note_sharing.models import Message
from secret_note_sharing.forms import SubmitForm

def index(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            message_text = request.POST.get('message_text', '')
            message_obj = Message(message_text = message_text)
            message_obj.save()
        return render(request, 'secret_note_sharing/message_submitted.html')
    return render(request,'secret_note_sharing/index.html')

def message_submitted(request):
    return render(request, 'secret_note_sharing/message_submitted.html')
    