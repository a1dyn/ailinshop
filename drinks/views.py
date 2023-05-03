from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from .models import Drink

class DrinkPage(ListView):
    model = Drink
    template_name = "drink_list.html"


class Success(TemplateView):
    template_name = "success.html"


def purchase(request, drink_id):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))
        drink = get_object_or_404(Drink, pk=drink_id)
        if drink.amount < amount:
            return HttpResponseBadRequest('Not enough stock available.')
        Drink.objects.filter(pk=drink_id).update(amount=drink.amount-amount)
        return HttpResponseRedirect(reverse('success'))
    else:
        return render(request, 'purchase.html', {'drink_id': drink_id})
