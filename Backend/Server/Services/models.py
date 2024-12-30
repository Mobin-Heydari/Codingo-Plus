from django.db import models

class MainServices(models.Model):
    # Name of the main service
    name = models.CharField(max_length=255, verbose_name="نام سرویس")
    # Slug for the main service, used in URLs
    slug = models.SlugField(max_length=255, verbose_name="اسلاگ")
    
    # Image associated with the main service
    image = models.ImageField(verbose_name="تصویر", upload_to="services/images", null=True)  # Fixed typo from 'imgae' to 'image'
    # Description of the main service
    description = models.TextField(verbose_name="توضیحات")
    
    def __str__(self):
        # String representation of the model
        return self.name
    
    class Meta:
        verbose_name = "سرویس اصلی"
        verbose_name_plural = "سرویس های اصلی"


class SubService(models.Model):
    # Name of the sub-service
    name = models.CharField(verbose_name="نام", max_length=255)
    # Slug for the sub-service, used in URLs
    slug = models.SlugField(max_length=255, verbose_name="اسلاگ")
    
    # Description of the sub-service
    description = models.TextField(verbose_name="توضیحات")
    # Short content related to the sub-service
    sub_content = models.CharField(verbose_name="محتوای مخصر", max_length=100)
    
    # Image associated with the sub-service
    image = models.ImageField(upload_to="services/images", verbose_name="تصویر")
    # Icon associated with the sub-service
    icon = models.ImageField(verbose_name="آیکون", upload_to="Sub-services/icons")
    
    def __str__(self):
        # String representation of the model
        return self.name
    
    class Meta:
        verbose_name = "سرویس زیر مجموعه"
        verbose_name_plural = "سرویس های زیر مجموعه"


class Feature(models.Model):
    # Foreign key linking to the SubService model
    sub_service = models.ForeignKey(
        SubService,
        on_delete=models.CASCADE,
        verbose_name="خدمت",
    )
    
    # Title of the feature
    title = models.CharField(max_length=255, verbose_name="عنوان")
    
    # Icon associated with the feature
    icon = models.ImageField(verbose_name="آیکون", upload_to="Sub-services/Features/icons")
    
    def __str__(self):
        # String representation of the model
        return self.title
    
    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"