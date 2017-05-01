from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from secret_note_sharing.models import Message
from secret_note_sharing.forms import SubmitForm

def index(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            message_text = request.POST.get('message_text', '')
            message_obj = Message(message_text = message_text)
            message_obj.save()
            message_id = message_obj.pk
        return HttpResponse(message_submitted(request, message_id))
    return render(request,'secret_note_sharing/index.html')

def message_submitted(request, message_id):
    message = Message.objects.get(pk=message_id)
    return render(request, 'secret_note_sharing/message_submitted.html', {'message': message})
    
def message_retrieve(request, message_id):
    #message = get_object_or_404(Message, pk=message_id)
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        return HttpResponse(no_message(request))
    Message.objects.filter(pk=message_id).delete()
    return render(request, 'secret_note_sharing/message_retrieve.html', {'message': message})
    
def no_message(request):
    return render(request, 'secret_note_sharing/no_message.html')
