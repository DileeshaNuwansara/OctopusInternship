from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import School, Class, Student, Assessment_Areas, Answers, Awards, Subject, Summary


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('School_Id', 'school_name')

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('Class_Id', 'Class_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('Student_Id', 'first_name', 'last_name', 'year_level', 'fullname')

@admin.register(Assessment_Areas)
class AssessmentAreasAdmin(admin.ModelAdmin):
    list_display = ('assessment_areas',)

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('Answers', 'Correct_Answers')

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('Subject', 'Subject_score')

@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('School_Id', 'sydney_participants', 'sydney_percentile', 'Assessment_Areas_Id', 'Award_Id', 'Class_Id', 'Correct_answer_percentage_per_class', 'Correct_Answer', 'Student_Id', 'Participant', 'Student_score', 'Subject_Id', 'Category_Id', 'Year_Level_name', 'Answer_Id', 'Correct_Answer_Id')

# admin.site.register(School)
# admin.site.register(Class)
# admin.site.register(Student)
# admin.site.register(Assessment_Areas)
# admin.site.register(Answers)
# admin.site.register(Awards)
# admin.site.register(Subject)
# admin.site.register(Summary)
