from django.restframework.resources import ModelResource
from ParkingShare.models import User

class UserResource (ModelResource):
    model = User
    fields = ('phoneNumber', 'password', 'name', 'surname', 'city', 'sex', 'date_of_birth')
