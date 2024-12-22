from django.db import models
import uuid  # For generating unique ids
from django.contrib.auth.models import AbstractUser


# Book Model
class Book(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Unique identifier for the book
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN is usually unique
    genre = models.CharField(max_length=100)
    published_year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    location = models.CharField(max_length=255)  # Location in the library
    cover_image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.title} by {self.author}'


# Member Model
class Member(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    MEMBERSHIP_STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    member_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Unique member identifier
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    membership_date = models.DateField()
    membership_type = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    membership_status = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Transaction Model
class Transaction(models.Model):
    ISSUE = 'issue'
    RETURN = 'return'
    TRANSACTION_TYPE_CHOICES = [
        (ISSUE, 'Issue'),
        (RETURN, 'Return'),
    ]

    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Unique transaction ID
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateTimeField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True, blank=True)  # Allow null if no fine
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')

    def __str__(self):
        return f'Transaction {self.transaction_id} for {self.book.title}'

