from django.db import models
from django.urls import reverse


class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField()
    main_image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_blog', args=[str(self.id)])


class BlogParagraph(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='paragraphs')
    paragraph = models.TextField()
    
    def __str__(self):
        return f"Paragraph {self.id} of {self.blog.title}"


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blogs/')
    
    def __str__(self):
        return f"Image {self.id} of {self.blog.title}"