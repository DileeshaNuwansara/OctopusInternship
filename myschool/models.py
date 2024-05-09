from django.db import models

# Create your models here.
class School(models.Model):
    School_Id = models.CharField(max_length=20,primary_key=True)
    school_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.School_Id} {self.school_name}"
    
    
class Class(models.Model):
    Class_Id = models.CharField(max_length=20,primary_key=True)
    Class_name  = models.CharField(max_length=50)
       
class Student(models.Model):
    Student_Id = models.CharField(max_length=20,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_level = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


class Assessment_Areas(models.Model):
    assessment_areas = models.CharField(max_length=255)

class Answers(models.Model):
    Answers = models.CharField(max_length=1)
    Correct_Answers = models.CharField(max_length=1)
    
    
class Awards(models.Model):
    Name = models.CharField(max_length=100, default='participation')
    
class Subject(models.Model):
    Subject = models.CharField(max_length=100)
    Subject_score = models.FloatField()
    
    
class Summary(models.Model):
    School_Id = models.ForeignKey(School,on_delete=models.CASCADE)
    sydney_participants = models.IntegerField()
    sydney_percentile = models.FloatField()
    Assessment_Areas_Id = models.ForeignKey(Assessment_Areas,on_delete=models.CASCADE)
    Award_Id = models.ForeignKey(Awards,on_delete=models.CASCADE)
    Class_Id =  models.ForeignKey(Class,on_delete=models.CASCADE)
    Correct_answer_percentage_per_class = models.FloatField()
    Correct_Answer = models.CharField(max_length=255)
    Student_Id = models.ForeignKey(Student,on_delete=models.CASCADE)
    Participant = models.CharField(max_length=50)
    Student_score = models.FloatField()
    Subject_Id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    Category_Id = models.CharField(max_length=100)
    Year_Level_name = models.CharField(max_length=10)
    Answer_Id = models.ForeignKey(Answers,on_delete=models.CASCADE)
    Correct_Answer_Id = models.CharField(max_length=20)
    
    