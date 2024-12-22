from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView, MemberListCreateAPIView, MemberDetailAPIView, TransactionListCreateAPIView, TransactionDetailAPIView

urlpatterns = [
    # Books
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    # Members
    path('members/', MemberListCreateAPIView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MemberDetailAPIView.as_view(), name='member-detail'),

    # Transactions
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),
]
