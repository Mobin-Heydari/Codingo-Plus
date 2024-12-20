from django.db import models




class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="سوال")
    answer = models.TextField(verbose_name="جواب")
    
    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'
    
    def __str__(self):
        return self.answer
    