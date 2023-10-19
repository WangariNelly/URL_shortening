from django.db import models

# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=255, )
    shortcode = models.CharField(max_length=15, unique=True)
    
    def _str_(self):
        return str(self.url)
    
    def _unicode(self):
        return str(self.url)