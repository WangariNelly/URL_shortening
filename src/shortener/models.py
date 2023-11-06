from django.db import models

from .utils import code_generator
# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=255, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    
    def save(self, *args,  **kwargs):
        #   print("saved")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        super(KirrURL, self).save(*args,**kwargs)
    
    
    def _str_(self):
        return str(self.url)
    
    def _unicode(self):
        return str(self.url)
    




    #python manage.py makemigrations
    #python manage.py migrate
    #source .venv/bin/activate