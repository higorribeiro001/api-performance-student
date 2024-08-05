from django.db import models

class StudentPerformance(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.IntegerField(null=False, blank=False)
    ethnicity = models.IntegerField(null=False, blank=False)
    paramental_education = models.IntegerField(null=False, blank=False)
    study_time_weekly = models.FloatField(null=False, blank=False)
    absenses = models.IntegerField(null=False, blank=False)
    tutoring = models.IntegerField(null=False, blank=False)
    parental_suporte = models.IntegerField(null=False, blank=False)
    extracurricular = models.IntegerField(null=False, blank=False)
    sports = models.IntegerField(null=False, blank=False)
    music = models.IntegerField(null=False, blank=False)
    voluteering = models.IntegerField(null=False, blank=False)
    gpa = models.FloatField(null=False, blank=False)
    grade_class = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = 'student_performance'

    def __str__(self):
        return self.name
    