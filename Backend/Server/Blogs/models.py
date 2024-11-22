from django.db import models




class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    image = models.ImageField(upload_to="blogs/main-images/")
    
    content = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        
    

class BlogSection(models.Model):
    
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="sections",
    )
    
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    
    image = models.ImageField(
        upload_to="blogs/section-images/",
        null=True,
        blank=True
    )
    
    video = models.FileField(
        upload_to="blogs/section-video/",
        null=True,
        blank=True
    )
    
    content = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Sections"
