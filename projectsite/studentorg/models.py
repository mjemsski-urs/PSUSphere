# studentorg/models.py

from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class College(BaseModel):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name

class Program(BaseModel):
    prog_name = models.CharField(max_length=150)
    college = models.ForeignKey("College", on_delete=models.CASCADE)  # string reference works too

    def __str__(self):
        return self.prog_name


class Organization(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(College, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_number = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=25, blank=True, null=True)
    firstname = models.CharField(max_length=25, blank=True, null=True)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_number or 'NoNumber'} - {self.lastname}, {self.firstname}"

class OrgMember(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} in {self.organization}"