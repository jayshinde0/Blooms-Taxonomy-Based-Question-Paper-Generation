from django.db import models

# Create your models here.
class Subject_data(models.Model):
    college_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)

    qb = models.FileField()

    
    q1 = models.CharField(max_length=500)
    q2 = models.CharField(max_length=500)
    q3 = models.CharField(max_length=500)
    q4 = models.CharField(max_length=500)
    q5 = models.CharField(max_length=500)
    q6 = models.CharField(max_length=500)
    q7 = models.CharField(max_length=500)
    q8 = models.CharField(max_length=500)
    q9 = models.CharField(max_length=500)
    q10 = models.CharField(max_length=500)
    

    bl1 = models.CharField(max_length=50)
    bl2 = models.CharField(max_length=50)
    bl3 = models.CharField(max_length=50)
    bl4 = models.CharField(max_length=50)
    bl5 = models.CharField(max_length=50)
    bl6 = models.CharField(max_length=50)
    bl7 = models.CharField(max_length=50)
    bl8 = models.CharField(max_length=50)
    bl9 = models.CharField(max_length=50)
    bl10 = models.CharField(max_length=50)
    

    m1 = models.IntegerField()
    m2 = models.IntegerField()
    m3 = models.IntegerField()
    m4 = models.IntegerField()
    m5 = models.IntegerField()
    m6 = models.IntegerField()
    m7 = models.IntegerField()
    m8 = models.IntegerField()
    m9 = models.IntegerField()
    m10 = models.IntegerField()


    date = models.DateField()

    def __str__(self):
        return self.branch_name + " - " + self.semester + " - " + self.subject_name