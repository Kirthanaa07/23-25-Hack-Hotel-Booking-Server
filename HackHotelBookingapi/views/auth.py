from datetime import datetime
from HackHotelBookingapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'email': user.email,
            'uid': user.uid
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    # Now save the user info in the levelupapi_gamer table
    user = User.objects.create(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        bio=request.data["bio"],
        email=request.data["email"],
        uid=request.data["uid"]
        
    )

    # Return the gamer info to the client
    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'bio': user.bio,
        'email': user.email,
        'uid': user.uid
    }
    return Response(data)
