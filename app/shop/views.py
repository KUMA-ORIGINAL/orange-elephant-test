from django.contrib import messages
from django.shortcuts import render, redirect

from shop.forms import UserForm, OrderForm
from shop.utils import send_websocket_notification


def index(request):
    if request.method == 'POST':
        if 'user_form' in request.POST:
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                send_websocket_notification(
                    "users", "user_created", {"user": user.username}
                )
                messages.success(request, f'Пользователь {user.username} успешно создан!')
                return redirect('index')
        elif 'order_form' in request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save()
                send_websocket_notification(
                    "orders", "order_created", {"order": order.id}
                )
                messages.success(request, f'Заказ #{order.id} успешно создан!')
                return redirect('index')
    user_form = UserForm()
    order_form = OrderForm()
    context = {'user_form': user_form, 'order_form': order_form}
    return render(request,'shop/index.html', context)
