from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from .models import Student
from .forms import StudentForm  # We'll create this next

# List all students
def student_list(request):
    students = Student.objects.all()

    # Get filter inputs from GET parameters
    name_query = request.GET.get('q', '')
    caste_query = request.GET.get('caste', '')
    religion_query = request.GET.get('religion', '')
    course_query = request.GET.get('course', '')
    year_query = request.GET.get('year_of_study', '')
    min_income = request.GET.get('min_income', '')
    max_income = request.GET.get('max_income', '')

    # Apply filters
    if name_query:
        students = students.filter(name__icontains=name_query)
    if caste_query:
        students = students.filter(caste=caste_query)
    if religion_query:
        students = students.filter(religion=religion_query)
    if course_query:
        students = students.filter(course=course_query)
    if year_query:
        students = students.filter(year_of_study=year_query)
    if min_income:
        students = students.filter(annual_income__gte=min_income)
    if max_income:
        students = students.filter(annual_income__lte=max_income)

    # Dropdown options (distinct values) - order and exclude blanks
    caste_options = Student.objects.order_by('caste').values_list('caste', flat=True).distinct()
    religion_options = Student.objects.order_by('religion').values_list('religion', flat=True).distinct()
    course_options = Student.objects.order_by('course').values_list('course', flat=True).distinct()
    year_options = Student.objects.order_by('year_of_study').values_list('year_of_study', flat=True).distinct()

    context = {
        'students': students,
        'name_query': name_query,
        'caste_query': caste_query,
        'religion_query': religion_query,
        'course_query': course_query,
        'year_query': year_query,
        'min_income': min_income,
        'max_income': max_income,
        'caste_options': [c for c in caste_options if c],
        'religion_options': [r for r in religion_options if r],
        'course_options': [c for c in course_options if c],
        'year_options': [y for y in year_options if y],
    }
    return render(request, 'students/student_list.html', context)

# Create student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# Update student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Delete student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})




