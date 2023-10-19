from django.db import models

# Teacher model
class Teacher(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
# Student model
class Student(models.Model):
    name = models.CharField(max_length=150)
    course=models.CharField(max_length=200)
    teachers = models.ManyToManyField(Teacher, related_name='students')

    def __str__(self):
        return self.name
    
    def taughtby(self):
        return ",".join([str(teacher) for teacher in self.teachers.all()])
    
# Certificate model
class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    jwt_token = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return f'{self.teacher.name} - {self.student.name}'


  