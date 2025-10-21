from django.db import models

# Create your models here.

class Student(models.Model):
    # General Information
    emis_no = models.CharField(max_length=20, unique=True)
    umis_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    aadhar_no = models.CharField(max_length=12)

    # Family Information
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    income_cert_no = models.CharField(max_length=50, blank=True)

    # Contact Information
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    # Bank Information
    bank_name = models.CharField(max_length=100)
    bank_city = models.CharField(max_length=50)
    bank_branch = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    account_no = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)

    # Academic Info
    academic_year = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    medium = models.CharField(max_length=20)
    mode_of_study = models.CharField(max_length=20)
    year_of_study = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.emis_no})"
