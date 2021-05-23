import stripe
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render 

from rest_framework import serializers, status,authentication,permissions
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from stripe.api_resources import charge, source    
from .models import Order,OrderItem
from .serializers import OrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])

def checkout(request):
    serializer= OrderSerializer(data=request.data)# form we fillout in the checkout page
    if serializer.is_valid():
        stripe.api_key =settings.STRIPE_SECRET_KEY
        #calculating the paying amount by saying sum, then we take the item quantity multiply with price
        #and we do this for every item in the serializer.validated_data(item) which we get from the post form.
        paid_amount= sum(item.get('quantity')* item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount *100),
                currency='USD',
                description='Charge from EcomDj',
                #source is a stripe token which  we get from the front-end so that everything is connected.
                source= serializers.validated_data['stripe_token']
            ) 
            serializer.save(user=request.user,paid_amount=paid_amount)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    
