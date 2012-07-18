from django.db import models
 

# Create your models here.
class SharedSite(models.Model):
    url = models.URLField()
    ip = models.IPAddressField()
    title = models.CharField(max_length = 200)
    user = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    
