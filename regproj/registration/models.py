from django.db import models

# Create your models here.
class reg_table(models.Model):
      name=models.CharField(max_length=200)
      image=models.ImageField(upload_to='images')
      phone=models.CharField(max_length=200)
      def __str__(self):
            return self.name
