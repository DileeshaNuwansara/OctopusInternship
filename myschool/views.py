from django.shortcuts import render
import csv
import os
from myschool.models import School, Class, Student, Assessment_Areas, Answers, Awards, Subject, Summary

def load_data_from_csv(request):
    directory = '/Octopus/Ganison_dataset/'
    
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Populate all models now
                    school_obj, created = School.objects.get_or_create(
                        School_Id=row.get('School_Id', None),
                        defaults={'school_name': row.get('school_name')}
                    )

                    class_obj, created = Class.objects.get_or_create(
                        Class_Id=row.get('Class_Id', None),
                        defaults={'class_name': row.get('Class')}
                    )

                    student_obj, created = Student.objects.get_or_create(
                        Student_Id=row.get('Student_Id', None),
                        defaults={
                            'first_name': row.get('first_name'),
                            'last_name': row.get('last_name'),
                            'year_level': row.get('year_level')
                        }
                    )

                    assessment_area_obj, created = Assessment_Areas.objects.get_or_create(
                        assessment_areas=row.get('assessment_areas', None)
                    )

                    answers_obj, created = Answers.objects.get_or_create(
                        Answers=row.get('Answers', None),
                        Correct_Answers=row.get('Correct_Answers', None)
                    )

                    awards_obj, created = Awards.objects.get_or_create(
                        Name=row.get('Name', None)
                    )

                    subject_obj, created = Subject.objects.get_or_create(
                        Subject=row.get('Subject', None),
                        Subject_score=row.get('Subject_score', None)
                    )

                    summary_obj = Summary.objects.create(
                        School_Id=school_obj,
                        sydney_participants=row.get('sydney_participants', None),
                        sydney_percentile=row.get('sydney_percentile', None),
                        Assessment_Areas_Id=assessment_area_obj,
                        Award_Id=awards_obj,
                        Class_Id=class_obj,
                        Correct_answer_percentage_per_class=row.get('Correct_answer_percentage_per_class', None),
                        Correct_Answer=row.get('Correct_Answer', None),
                        Student_Id=student_obj,
                        Participant=row.get('Participant', None),
                        Student_score=row.get('Student_score', None),
                        Subject_Id=subject_obj,
                        Category_Id=row.get('Category_Id', None),
                        Year_Level_name=row.get('Year_Level_name', None),
                        Answer_Id=answers_obj,
                        Correct_Answer_Id=row.get('Correct_Answer_Id', None)
                    )


    print("Database populated successfully.")



