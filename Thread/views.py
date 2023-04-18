from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Thread.models import Thread, Message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def thread_view(request, thread):
    participant2_name = request.GET.get('participant2')
    participant2 = User.objects.get(username=participant2_name)
    thread_details = Thread.objects.get(participant1__username=thread)

    return render(request, 'thread.html', {
        'participant2': participant2,
        'thread': thread,
        'thread_details': thread_details
    })


def checkview(request):
    participant1_name = request.GET['participant1']
    participant2_name = request.GET['participant2']

    participant1 = User.objects.get(username=participant1_name)
    participant2 = User.objects.get(username=participant2_name)

    if Thread.objects.filter(participant1=participant1, participant2=participant2).exists():
        return redirect('/' + participant1_name + '/?participant2=' + participant2_name)
    else:
        new_thread = Thread.objects.create(participant1=participant1, participant2=participant2)
        new_thread.save()
        return redirect('/' + participant1_name + '/?participant2=' + participant2_name)


@login_required
def send(request):
    if request.method == 'POST':
        message_text = request.POST['message']
        thread_id = request.POST['thread_id']

        thread = Thread.objects.get(id=thread_id)

        message = Message.objects.create(sender=request.user, text=message_text, thread=thread)
        message.save()

        return HttpResponse('Message sent successfully')
    else:
        return HttpResponse('Message sent is not successfully')


def getMessages(request, thread):
    thread_details = Thread.objects.get(participant1__username=thread)

    messages = Message.objects.filter(thread=thread_details.id)

    messages_data = []
    for message in messages:
        sender = User.objects.get(id=message.sender_id)
        if message.sender_id != request.user.id and not message.is_read:
            message.is_read = True
            message.save()
        messages_data.append({
            'sender_name': sender.username,
            'text': message.text,
            'created': message.created.strftime('%Y-%m-%d %H:%M:%S'),
            'is_read': message.is_read,
        })
    return JsonResponse({'messages': list(messages_data)})


def delete_thread(request, thread):
    thread_details = Thread.objects.get(participant1__username=thread)
    thread = Thread.objects.get(id=thread_details.id)
    thread.delete()
    return redirect('/')
