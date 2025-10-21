from students.models import Student
from decimal import Decimal

def load_sample_student():
    if not Student.objects.filter(umis_id="9002480387").exists():
        Student.objects.create(
            emis_no="1003435859",
            umis_id="9002480387",
            name="SAKTHIBALAN S",
            dob="2006-08-09",
            gender="Male",
            blood_group="A+ve",
            religion="Hindu",
            nationality="Indian",
            caste="Adi Dravida",
            aadhar_no="625953698759",
            father_name="SANKAR G",
            mother_name="Prema C",
            annual_income=Decimal("64000.00"),
            income_cert_no="",
            mobile_no="9345985367",
            email="sakthibalan1406@gmail.com",
            address="413, East St, Kanarai Nagar, Seplanatham, Virudhachalam, Cuddalore Dist",
            bank_name="CANARA BANK",
            bank_city="CUDDALORE",
            bank_branch="SEPLANATHAM",
            ifsc_code="CNRB0010420",
            account_no="362120000857",
            account_type="Savings",
            academic_year="2023–2024",
            branch="Computer Science",
            course="B.Sc",
            medium="English",
            mode_of_study="Regular",
            year_of_study=1,
        )
        print("✅ Sample student 'SAKTHIBALAN S' added successfully!")
    else:
        print("ℹ️ Sample student already exists.")
