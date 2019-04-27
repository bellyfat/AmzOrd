from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.db.models import Count

from .forms import OrderForm
from .models import Order

def orderCreateView(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()

    context = {
        'form': form
    }
    return render(request, "TrackAmzOrd/order_create.html", context)

def index(request):
    latest_order = Order.objects.order_by('-ord_date')
    template = loader.get_template('TrackAmzOrd/index.html')
    context = {
        'latest_order': latest_order,
    }
    return HttpResponse(template.render(context, request))


def orderCount(request):
    order_count = Order.objects.values('ord_name').annotate(Ct = Count('ord_name'))
    order_names = list(order_count.values_list('ord_name', flat=True))
    order_count = list(order_count.values_list('Ct', flat=True))
    context = {
        'order_names': order_names,
        'order_count': order_count
    }
    return render(request, 'TrackAmzOrd/OrderTotal.html',context)



def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'TrackAmzOrd/detail.html', {'order': order})


def result(request, order_id):
    return HttpResponse("You're looking at the reuslts view - question %s." % order_id)
