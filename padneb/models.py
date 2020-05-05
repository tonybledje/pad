from django.db import models
from django.utils import timezone
# Create your models here.


class Chapter(models.Model):
    code_chapter = models.CharField(max_length=3)
    chapter_name = models.CharField(max_length=150)
    updated_date = models.DateTimeField(auto_now_add=True)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.chapter_name)


class Member(models.Model):
    Marital_Status = (
        ('M', 'Married'),
        ('W', 'Widowed'),
        ('S', 'Single'),
    )
    Gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=35)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=254)
    admission_date = models.DateField('Admitted on:')
    gender = models.CharField(max_length=1, choices=Gender, blank=False)
    marital_status = models.CharField(max_length=1, choices=Marital_Status)
    in_pad_social = models.BooleanField()
    date_admitted = models.DateField()
    cellPhone = models.CharField(max_length=12)
    homePhone = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.last_name)


class Contribution(models.Model):
    type = (
        ('MC', 'Monthly'),
        ('SC', 'Special'),
        ('AC', 'Annual Convention'),
        ('EY', 'End of Year Celebration')
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=2, choices=type)
    comments = models.TextField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.member)


class Guardian(models.Model):
    Relation = (
        ('F', 'Father'),
        ('M', 'Mother'),
        ('S', 'Spouse'),
        ('O', 'Other'),
    )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    fist_name = models.CharField(max_length=35)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=35)
    relation_to_member = models.CharField(max_length=1, choices=Relation)
    comments = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.member)
