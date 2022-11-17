from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, RoomForm
from .models import Reply, Room, User


## Account creation with CreateView but I won't use any more than this
class SignUp(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'create_account.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = authenticate(email=email, password=password)
        login(self.request, new_user)
        return valid


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(name__icontains=q)
    return render(request, 'home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    replies = room.reply_set.all()
    participants = room.participants.all()

    if request.method == "POST":
        reply = Reply.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body'),
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    return render(request, 'room.html', {'room': room, 'replies': replies, 'participants': participants})

@login_required
def roomCreate(request):
    form = RoomForm()
    if request.method == 'POST':
        Room.objects.create(
            host = request.user,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
        )
        return redirect('home')

    return render(request, 'room_create.html', {'form': form})

@login_required
def roomEdit(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("Hey don't cheat, you do not have this permission")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'room': room}
    return render(request, 'edit_room.html', context)

@login_required
def roomDelete(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Hey don't cheat, you do not have this permission")

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'delete_room.html', {'delRoom': room})

@login_required
def replyEdit(request, pk):
    reply = Reply.objects.get(id=pk)

    if request.user != reply.user:
        return HttpResponse("Hey don't cheat, you do not have this permission")

    if request.method == 'POST':
        reply.body = request.POST.get('body')
        reply.save()
        return redirect('home')

    return render(request, 'reply_edit.html', {'reply' : reply})

@login_required
def replyDelete(request, pk):
    reply = Reply.objects.get(id=pk)

    if request.method == 'POST':
        reply.delete()
        return redirect('home')

    return render(request, 'reply_delete.html', {'delreply': reply})
