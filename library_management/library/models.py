from django.db import models

# Create your models here.
class Author(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    country=models.CharField(max_length=200)
    date_joined=models.DateTimeField("Joining Date")
    def __str__(self):
        return self.full_name

class Book(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    isbn=models.CharField(max_length=200, unique=True)
    pub_date=models.DateTimeField("Publication Date")
    pages=models.IntegerField()
    price=models.DecimalField(decimal_places=2, max_digits=8)
    availability=models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Member(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=13)
    membership_date=models.DateTimeField("Membership Joining Date")
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.full_name

class BorrowRecord(models.Model):
    member=models.ForeignKey(Member, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date=models.DateTimeField("Date of Borrowing")
    return_date=models.DateTimeField(null=True, blank=True)
    returned=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.member} borrowed {self.book}"