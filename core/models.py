from django.db import models

# Create your models here.
class HomeGrid(models.Model):
    category = models.CharField(max_length=400)
    date = models.CharField(max_length=400)
    imageUrl = models.CharField(max_length=1000)
    title = models.CharField(max_length=400)
    details = models.CharField(max_length=5000, default='some strin')

    def _str_(self):
        return '%s' %(self.ename)
    class Meta:
        db_table = 'homeGrid'
