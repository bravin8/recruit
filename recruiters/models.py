from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Recruiter(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = PhoneNumberField()
	date_of_birth = models.DateField()
	location = models.CharField(max_length=100)
	image = models.ImageField(upload_to='recruiter/%Y/%m/%d')
	thumb = models.ImageField(upload_to='recruiter/%Y/%m/%d', blank=True)

	def __str__(self):
		return self.user.email

	def save(self, *args, **kwargs):
		from recruit.utils import generate_thumbnail
		thumb = generate_thumbnail(self.image)
		self.thumb=thumb
		super(Recruiter, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		from recruit.utils import delete_from_s3
		delete_from_s3([self.image, self.thumb])
		super(Recruiter, self).delete(*args, **kwargs)