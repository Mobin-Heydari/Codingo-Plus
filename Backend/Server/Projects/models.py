from django.db import models



class Category(models.Model):
    
    category = models.CharField(
        verbose_name="Category",
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



class Project(models.Model):
    
    class ProjectStatus(models.TextChoices):
        IN_PROGRESS = 'In Progress', 'در حال پیشرفت'
        COMPLETED = 'Completed', 'تکمیل شده'
        PENDING = 'Pending', 'در انتظار'
        CANCELED = 'Canceled', 'لغو شده'
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Category",
    )
        
    title = models.CharField(max_length=200, verbose_name="عنوان")
    
    slug = models.SlugField(max_length=200, verbose_name="اسلاگ")
    
    description = models.TextField(verbose_name="توضیحات")
    
    image = models.ImageField(upload_to='Projects/Images/', verbose_name="تصویر")
    
    url = models.URLField(blank=True, verbose_name="آدرس وب‌سایت")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="زمان به‌روزرسانی")
    
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING,
        verbose_name="وضعیت"
    )
    
    class Meta:
        verbose_name = "پروژه"  # Human-readable singular name in Persian
        verbose_name_plural = "پروژه‌ها"  # Human-readable plural name in Persian
    
    def __str__(self):
        return self.title