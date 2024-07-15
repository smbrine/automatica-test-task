# visits/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Worker

class PhoneNumberAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Phone '):
            return None

        phone = auth_header.split(' ')[1]
        try:
            worker = Worker.objects.get(phone=phone)
        except Worker.DoesNotExist:
            raise AuthenticationFailed('Invalid phone number')

        return (worker, None)
