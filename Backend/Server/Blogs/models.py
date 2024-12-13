from django.db import models

class Category(models.Model):
    
    category = models.CharField(
        verbose_name="دسته بندی",
        max_length=100,
        unique=True,
    )
    
    slug = models.SlugField(
        verbose_name="اسلاگ",
        max_length=100,
        unique=True,
    )
    
    image = models.ImageField(
        verbose_name="تصویر",
        upload_to="categories/images/",
        blank=True,
        null=True,
    )
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        
    def __str__(self):
        return self.category


class Blog(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="دسته بندی",
        related_name="Category"
    )
    title = models.CharField(max_length=255, verbose_name="عنوان")
    slug = models.SlugField(max_length=255, verbose_name="اسلاگ")
    
    image = models.ImageField(upload_to="blogs/main-images/", verbose_name="تصویر اصلی")
    
    content = models.TextField(verbose_name="محتوا")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان به‌روزرسانی")
    
    class Meta:
        verbose_name = "وبلاگ"  # Human-readable singular name in Persian
        verbose_name_plural = "وبلاگ‌ها"  # Human-readable plural name in Persian


class BlogSection(models.Model):
    
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name="وبلاگ"
    )
    
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="عنوان بخش"
    )
    
    image = models.ImageField(
        upload_to="blogs/section-images/",
        null=True,
        blank=True,
        verbose_name="تصویر بخش"
    )
    
    video = models.FileField(
        upload_to="blogs/section-video/",
        null=True,
        blank=True,
        verbose_name="ویدیو بخش"
    )
    
    content = models.TextField(null=True, blank=True, verbose_name="محتوای بخش")
    
    class Meta:
        verbose_name = "بخش وبلاگ"  # Human-readable singular name in Persian
        verbose_name_plural = "بخش‌های وبلاگ"  # Human-readable plural name in Persian