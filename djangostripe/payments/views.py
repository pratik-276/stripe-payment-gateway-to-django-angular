import re
from django.http import JsonResponse
import stripe # new

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render # new
from django.views.decorators.csrf import csrf_exempt
import json

stripe.api_key = settings.STRIPE_SECRET_KEY # new


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def createCharge(token):
    charge = stripe.Charge.create(
        amount=500,
        currency='usd',
        description='A Django charge',
        source=token,
        shipping={
            "name": "Jenny Rosen",
            "address": {
            "line1": "510 Townsend St",
            "postal_code": "98140",
            "city": "San Francisco",
            "state": "CA",
            "country": "US",
            },
        }
    )
    return charge

@csrf_exempt
def generateToken(request):
    if request.method == "POST":
        body = json.loads(request.body)
        doe = body['doe']
        month = int(doe.split('/')[0])
        year = int('20{0}'.format(doe.split('/')[1]))
        cardData = {
                "number": body['card'],
                "exp_month": month,
                "exp_year": year,
                "cvc": body['cvc'],
            }
        print(cardData)
        token = stripe.Token.create(
            card=cardData
        )
        charge = createCharge(token.id)
        return JsonResponse({
            "status": charge.status
        })




def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken'],
            shipping={
                "name": "Jenny Rosen",
                "address": {
                "line1": "510 Townsend St",
                "postal_code": "98140",
                "city": "San Francisco",
                "state": "CA",
                "country": "US",
                },
            }
        )
        print(charge.status)
        return render(request, 'charge.html')