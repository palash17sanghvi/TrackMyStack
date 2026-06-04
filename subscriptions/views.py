from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal  # for the mathematics precision
from .models import Subscription
from .forms import SubscriptionForm


@login_required
def dashboard_view(request):
    # THE NEW BOUNCER: Kick unverified users to the 2FA setup wizard
    if not request.user.is_verified():
        return redirect('two_factor:setup')

    # write
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            new_subscription = form.save(commit=False)
            new_subscription.user = request.user
            new_subscription.save()
            return redirect('dashboard')
    else:
        # read
        form = SubscriptionForm()

    user_subscriptions = Subscription.objects.filter(user=request.user)

    # mathematics
    total_monthly = Decimal('0.00')
    sub_count = user_subscriptions.count()

    for sub in user_subscriptions:
        if sub.billing_cycle == 'weekly':
            total_monthly += sub.cost * Decimal('52') / Decimal('12')
        elif sub.billing_cycle == 'monthly':
            total_monthly += sub.cost
        elif sub.billing_cycle == 'yearly':
            total_monthly += sub.cost / Decimal('12')

    annual_projection = total_monthly * Decimal('12')

    # rounding the decimal according to the format in the template
    total_monthly = round(total_monthly, 2)
    annual_projection = round(annual_projection, 2)

    context = {
        'subscriptions': user_subscriptions,
        'form': form,
        'sub_count': sub_count,
        'total_monthly': total_monthly,
        'annual_projection': annual_projection,
    }
    return render(request, 'subscriptions/dashboard.html', context)


@login_required
def delete_subscription_view(request, sub_id):
    # THE NEW BOUNCER: Kick unverified users to the 2FA setup wizard
    if not request.user.is_verified():
        return redirect('two_factor:setup')

    # find the subscription to delete
    chosen_sub = get_object_or_404(Subscription, id=sub_id, user=request.user)

    # 2. Destroy it
    chosen_sub.delete()

    # 3. refresh
    return redirect('dashboard')


@login_required
def update_subscription_view(request, sub_id):
    # THE NEW BOUNCER: Kick unverified users to the 2FA setup wizard
    if not request.user.is_verified():
        return redirect('two_factor:setup')

    # find the subscription
    sub_to_edit = get_object_or_404(Subscription, id=sub_id, user=request.user)

    # inside update
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=sub_to_edit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    # print out the current subscription we want to edit in a new form
    else:
        form = SubscriptionForm(instance=sub_to_edit)

    context = {
        'form': form,
        'subscription': sub_to_edit,
    }
    return render(request, 'subscriptions/update.html', context)


def register_view(request):
    # 1. The user hands in the filled paperwork
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('two_factor:login')  # Send them to the vault gate!

    # 2. The user walks up empty-handed
    else:
        form = UserCreationForm()

    # 3. Hand them the clipboard (render the template)
    return render(request, 'subscriptions/register.html', {'form': form})
