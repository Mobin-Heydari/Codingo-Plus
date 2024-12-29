from django.db import models



class MainServices(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام سرویس")
    slug = models.SlugField(max_length=255, verbose_name="اسلاگ")
    
    imgae = models.ImageField(verbose_name="تصویر ", upload_to="services/images")
    description = models.TextField(verbose_name="توضیحات")
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "سرویس اصلی"
        verbose_name_plural = "سرویس های اصلی"
        


class SubService(models.Model):
    name = models.CharField(verbose_name="نام", max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="اسلاگ")
    
    description = models.TextField(verbose_name="توضیحات")
    sub_content = models.CharField(verbose_name="محتوای مخصر", max_length=100)
    
    image = models.ImageField(upload_to="services/images", verbose_name="تصویر")
    icon = models.ImageField(verbose_name="آیکوهن", upload_to="Sub-services/icons")
    


class SubServiceFeatures(models.Model):
    
    sub_service = models.ForeignKey(
        SubService,
        on_delete=models.CASCADE,
        verbose_name="خدمت",
    )
    
    title = models.CharField(max_length=255, verbose_name="عنوان")
    
    icon = models.ImageField(verbose_name="آیکون", upload_to="Sub-services/Features/icons")