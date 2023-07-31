from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# from .forms import *

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.http import JsonResponse

from .forms import * 
import stripe
# This is your test secret API key.
STRIPE_PUBLISHABLE_KEY = 'pk_test_51LEQ0KSHpJyK15aUlAXrZGxY2TCPa7gTOUOjAgz5VDTOgFVgyZEvJtNalzEGhYNI5ifJlrnu0N28UdjNxMizSgtx00m9kIwFnk'
STRIPE_SECRET_KEY = 'sk_test_51LEQ0KSHpJyK15aUH8YCofLvHxVgRR8L3Zv134gt5MDONfnLvKRqxGcfJnNI8zSDslhm6VUbV203v8mfFxc85cT300q6OPKP3h'
stripe.api_key = STRIPE_SECRET_KEY

YOUR_DOMAIN = 'http://127.0.0.1:8000'

# Create your views here.
def shop(request):
    data1 = Products.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 6)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context ={
        'data':data,
    }
    return render(request, 'shop.html', context)


def addtocart(request):
    if request.method == "GET":
        user =request.user
        idd = request.GET.get('name')
        product = Products.objects.get(id=idd)
        count = Cart.objects.filter(user=user,product=product).count()
        if count > 0:
            cart = Cart.objects.get(user=user,product=product)
            qty = int(cart.qty) + 1
            print(qty)
            cart.qty = qty
            data = int(cart.qty)
            cart.save()
            idd = str(idd) 
            
        else:
            Cart.objects.create(user=user, product=product, qty = 1)
            data = 1
            idd = str(idd) 
            
        
        return JsonResponse({'data':data, 'idd': idd})


def minus(request):
    if request.method == "GET":
        user =request.user
        idd = request.GET.get('name')
        product = Products.objects.get(id=idd)
        cart = Cart.objects.get(user=user,product=product)
        if int(cart.qty) > 1:
            qty = int(cart.qty) - 1
            print(qty)
            cart.qty = qty
            data = int(cart.qty)
            cart.save()
            idd = str(idd) 
            
        else:
            cart.delete()
            data = 0
            idd = str(idd) 
            
        
        return JsonResponse({'data':data, 'idd': idd})



def plus(request):
    if request.method == "GET":
        user =request.user
        idd = request.GET.get('name')
        product = Products.objects.get(id=idd)
        cart = Cart.objects.get(user=user,product=product)
        if int(cart.qty) > 0:
            qty = int(cart.qty) + 1
            print(qty)
            cart.qty = qty
            data = int(cart.qty)
            cart.save()
            idd = str(idd) 
            
        else:
            pass 
            
        
        return JsonResponse({'data':data, 'idd': idd})



def cart(request):
    data = Cart.objects.all().order_by('id')
    if data:
        total = 0
        for ie in data:
            prod = Products.objects.get(id=ie.product.id)
            to = int(prod.sp) * int(ie.qty)
            total = to + total
        total = int(total) + 19
        context ={
            'data':data,
            'total':total,
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('home:home')

def shopd(request, pk):
    data = Products.objects.get(slug=pk)
    context ={
        'data':data,
    }
    return render(request, 'shopd.html', context)

def dashboard(request):
    context ={
    }
    return render(request, 'dashboard.html', context)

def paymentMethodSelected(request):
    if request.method == 'POST':
        print('aa')
        form = OrderForm(request.POST)
        if form.is_valid():
            data22 = form.save(commit=False)
            data = Cart.objects.all().order_by('id')
            item = []
            total = 0
            for ie in data:
                prod = Products.objects.get(id=ie.product.id)
                to = int(prod.sp) * int(ie.qty)
                total = to + total
                item.append(prod.product_name + '*' + str(ie.qty) +',')

            total = int(total) + 19
            data22.total_amount = int(total)
            data22.bill = item
            form.save()
            return render(request, 'stripe/payment.html')
        else:
            print(form.errors)
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@csrf_exempt
def payWithStripe(request):
    uid = request.user.id
    mydata = Order.objects.filter(user_id=uid).last()
    # print(request.POST)
    amount = int(mydata.total_amount)*100
    
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'inr',
        'product_data': {
          'name': 'Cart Checkout',
        },
        'unit_amount': amount,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url= YOUR_DOMAIN + "/shop/pay-with-stripe-confirmation?session_id={CHECKOUT_SESSION_ID}",
    cancel_url=YOUR_DOMAIN + '/',
    )
    return JsonResponse({'id': session.id})


@csrf_exempt
@api_view(['GET'])
def payWithStripeConfirmation(request):
    q = request.GET.get('session_id')
    uid = request.user.id
    session = stripe.checkout.Session.retrieve(q)
    customer = stripe.Customer.retrieve(session.customer)
    print(session)
    for key, val in session.items():
        print(key,'-->',val)
        if key == 'payment_intent':
            order_id = val
        if key == 'amount_total':
            amount = val
    print(order_id)
    amount = int(amount)/100
    response = request.POST
    user = Order.objects.filter(user_id=uid, total_amount=amount).last()
    user.paid = True
    user.payment_id = order_id
    # uid = request.user.id
    # cart = Cart.objects.filter(user=uid)
    # cart_dict = {"name":[], "qty":[]}
    # a = cart_dict["name"]
    # for ie in cart:
    #     if a:
    #         for i in a:
    #             if ie.product.product_name in cart_dict["name"]:
    #                 pass
    #             else:
    #                 cart_dict["name"].append(ie.product.product_name)
    #                 cart_dict["qty"].append(ie.qty) 
                    
    #     else:
    #         cart_dict["name"].append(ie.product.product_name)
    #         cart_dict["qty"].append(ie.qty)     
    #     ie.delete()    

    # print(cart_dict)
    # user.bill = cart_dict    
    cart = Cart.objects.filter(user=uid)
    for ie in cart:
        ie.delete()
    user.save() 
    # VERIFYING SIGNATURE
    try:
        # status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'stripe/order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'stripe/order_summary.html', {'status': 'Payment Faliure!!!'})



