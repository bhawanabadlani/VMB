from django.db import models

# GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))

# SIKSHA_STATUS_CHOICES = (
#     ("A", "Aspiring"),
#     ("Z", "Shelter"),
#     ("D1", "Harinam"),
#     ("D2", "Brahmin"),
# )
# # Create your models here.
# class People(models.Model):
#     name = models.CharField(max_length=250, "Name")
#     gender = CharField(max_length=1, choices=GENDER_CHOICES, "Gender")
#     photo = ImageField(max_length=100, "Photo", null=True)
#     dob = DateTimeField("Date and Time of birth")
#     s_status = CharField(max_length=50, choices=SIKSHA_STATUS_CHOICES)
    
#     def __str__(self):
#         return self.name

#     @property
#     def age(self):
#         if self.dob:
#             return int((datetime.datetime.now() - self.dob).days / 365.25)