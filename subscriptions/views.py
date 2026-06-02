from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Subscription


@login_required
def dashboard_view(request):
    user_subscriptions = Subscription.objects.filter(user=request.user)
    context = {
        'subscriptions': user_subscriptions
    }
    return render(request, 'subscriptions/dashboard.html', context)
