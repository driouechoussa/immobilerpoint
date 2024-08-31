from django.db import models

# Create your models here.

class Blog_table(models.Model):
    blog_title = models.CharField(max_length=250, null=False)
    blog_contentText = models.TextField()
    blog_title_image = models.ImageField(upload_to='blogs/')
    blog_TimeCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
    
    def DisplayOnlyDate(self):
        return self.blog_TimeCreated.strftime('%Y-%m-%d')

    class Meta:
        verbose_name_plural = "Blogs"













