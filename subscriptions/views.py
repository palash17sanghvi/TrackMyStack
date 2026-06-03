from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Subscription
from .forms import SubscriptionForm


@login_required
def dashboard_view(request):
    # CASE 1: User submitted the form to add a new subscription
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)  # Load form with submitted data

        if form.is_valid():  # Trigger automatic validation & data cleaning
            new_subscription = form.save(commit=False)  # Hold the save process
            new_subscription.user = request.user       # Lock current user as the owner
            new_subscription.save()                    # Write row to SQLite database

            # Refresh page to reset request to GET
            return redirect('dashboard')

    # CASE 2: User is just loading or refreshing the page
    else:
        form = SubscriptionForm()  # Generate an empty form for the UI

    # Always pull current user's data and load the interface
    user_subscriptions = Subscription.objects.filter(user=request.user)
    context = {
        'subscriptions': user_subscriptions,
        'form': form
    }
    return render(request, 'subscriptions/dashboard.html', context)
