from django.db import models
class blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to=' post_images',blank=True)
    body=models.TextField()

    def summary (self):
         return self.body[:100]



# Create your models here.
#title
#date
#image
#body
#add the blog appo to the setting
#create migration
#migrate
#add app to admin
