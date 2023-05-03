from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from .models import Chips

class ChipsPage(ListView):
    model = Chips
    template_name = "chips.html"


# class Success(TemplateView):
#     template_name = "success.html"
def success(request):
    return render(request, "success.html")

def purchase(request, chips_id):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))
        chips = get_object_or_404(Chips, pk=chips_id)
        if chips.amount < amount:
            return HttpResponseBadRequest('Not enough stock available.')
        Chips.objects.filter(pk=chips_id).update(amount=chips.amount-amount)
        return HttpResponseRedirect(reverse('success'))
    else:
        return render(request, 'purchase.html', {'chips_id': chips_id})
