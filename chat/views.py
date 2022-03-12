from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Seller
from .models import Message

# Create your views here.

@login_required(login_url='/login')
def index(request):
    try:
        seller = Seller.objects.get(user=request.user)
    except:
        return redirect('/shop')
    messages = Message.objects.all()
    context = {
        'msgs': messages
    }
    return render(request, 'chat/chatbox2.html', context = context)