from django.db import models




class Project(models.Model):
    
    class ProjectStatus(models.TextChoices):
        IN_PROGRESS = 'In Progress', 'In Progress'
        COMPLETED = 'Completed', 'Completed'
        PENDING = 'Pending', 'Pending'
        CANCELED = 'Canceled', 'Canceled'
        
    
    title = models.CharField(max_length=200)
    
    slug = models.SlugField(max_length=200)
    
    description = models.TextField()
    
    image = models.ImageField(upload_to='Projects/Images/')
    
    url = models.URLField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    
    def __str__(self):
        return self.title
    
