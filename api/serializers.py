from rest_framework import serializers
from lib.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField()
        model = Book
        fields = '__all__'
        
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
        

class BorrowSerializer(serializers.ModelSerializer):
    borrow_date = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    class Meta:
        model = Borrow
        fields = '__all__'