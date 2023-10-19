from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from.models import Teacher,Student,Certificate
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# view for teacher
def teacherView(request):
    if request.method=='POST':
        teacher_id = request.POST.get("teacher")
        teacher = Teacher.objects.get(id=teacher_id)
        students = teacher.students.all()
        teachers = Teacher.objects.all()
        return render(request, 'teacher.html', {'teachers': teachers,'students': students})    
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})

# view for student
def studentView(request):
    if request.method=='POST':
        student_id = request.POST.get("student")
        student = Student.objects.get(id=student_id)
        teachers = student.teachers.all()
        students = Student.objects.all()
        return render(request, 'student.html', {'students': students,'teachers': teachers})  
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})


# view for creating certificates
def generate_certificate(request):
    if request.method == "POST":
        teacher_id = request.POST.get("teacher")
        student_id = request.POST.get("student")
        

        teacher = Teacher.objects.get(id=teacher_id)
        student = Student.objects.get(id=student_id)

        # Create a new certificate
        certificate = Certificate(teacher=teacher, student=student)
        certificate.save()

        # Generate a JWT token and associate it with the certificate
        token = AccessToken.for_user(request.user)  
        certificate.jwt_token = str(token)
        certificate.save()

        return render(request, "certificate.html", {"certificate": certificate})

    # Handle GET request, render form to generate certificate
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    return render(request, "generate_certificate.html", {"teachers": teachers, "students": students})



@permission_classes([IsAuthenticated])
def verify_certificate(request, id):
    try:
        certificate = Certificate.objects.get(id=id)
        return JsonResponse({"message": "Certificate is valid."}, status=200)
    except Certificate.DoesNotExist:
        return JsonResponse({"message": "Certificate not found."}, status=404)

