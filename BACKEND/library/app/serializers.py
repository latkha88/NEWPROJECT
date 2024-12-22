from rest_framework import serializers
from .models import Book, Member, Transaction


# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model


# Member Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'  # Include all fields of the Member model


# Transaction Serializer
class TransactionSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)  # Nested serializer to show member details
    book = BookSerializer(read_only=True)  # Nested serializer to show book details

    class Meta:
        model = Transaction
        fields = '__all__'  # Include all fields of the Transaction model


# Serializer for creating transactions (optional)
class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['member', 'book', 'transaction_type', 'transaction_date', 'due_date']  # You can omit return_date and fine_amount for creation
