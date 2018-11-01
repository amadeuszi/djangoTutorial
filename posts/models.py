from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %b %Y")

    def summary(self):
        return self.body[0:100] + "..." if len(self.body) > 100 else self.body

