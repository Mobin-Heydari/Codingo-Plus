from django.db import models
from Services.models import SubService, Feature

class MainPlans(models.Model):
    # Represents the main service plans available.
    name = models.CharField(max_length=255, verbose_name="اسم")  # Name of the main plan.
    slug = models.SlugField(max_length=255, unique=True, verbose_name="اسلاگ")  # Unique identifier for the plan.
    icon = models.ImageField(verbose_name="آیکون", upload_to="plans/icon/")  # Icon associated with the plan.
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")  # Timestamp for when the plan was created.
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")  # Timestamp for when the plan was last updated.

    def __str__(self):
        return self.name  # Returns the name of the plan for display.

    class Meta:
        verbose_name = "پلن اصلی"  # Persian for "Main Plan"
        verbose_name_plural = "پلن های اصلی"  # Persian for "Main Plans"


class ServicePlan(models.Model):
    # Represents a specific service plan that links a sub-service to a main plan.
    sub_service = models.ForeignKey(
        SubService, 
        on_delete=models.CASCADE, 
        verbose_name="سرویس"  # The sub-service associated with this service plan.
    )
    main_plan = models.ForeignKey(
        MainPlans, 
        on_delete=models.CASCADE, 
        verbose_name="پلن"  # The main plan associated with this service plan.
    )

    def __str__(self):
        return f"{self.main_plan.name} - {self.sub_service.name}"  # Returns a string representation of the service plan.

    class Meta:
        verbose_name = "پلن سرویس"  # Persian for "Service Plan"
        verbose_name_plural = "پلن های سرویس"  # Persian for "Service Plans"


class PlanSupport(models.Model):
    # Represents support details for a specific service plan.
    plan = models.ForeignKey(
        ServicePlan,
        on_delete=models.CASCADE,
        related_name="supports",  # Allows access to support details from the service plan.
        verbose_name="پلن",  # The service plan associated with this support.
    )
    free_support = models.IntegerField(default=6, verbose_name="پشتیبانی رایگان")  # Number of free support instances included.
    supporting_price_per_month = models.BigIntegerField(verbose_name="هزینه ی پشتیبانی ماهانه")  # Monthly cost for additional support.

    def __str__(self):
        return f"{self.plan} - Free Support: {self.free_support}"  # Returns a string representation of the support details.

    class Meta:
        verbose_name = "پشتیبانی"  # Persian for "Support"
        verbose_name_plural = "پشتیبانی ها"  # Persian for "Supports"


class PlansFeature(models.Model):
    # Represents features associated with a specific service plan.
    plan = models.ForeignKey(
        ServicePlan,
        on_delete=models.CASCADE,
        related_name="features",  # Allows access to features from the service plan.
        verbose_name="پلن",  # The service plan associated with this feature.
    )
    features = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        related_name='plan_features',  # Allows access to features from the feature model.
        verbose_name="امکانات"  # The specific feature associated with this service plan.
    )
    status = models.BooleanField(verbose_name="وضعیت", default=True)  # Indicates if the feature is active or not.

    def __str__(self):
        return f"{self.features.name} - Status: {'Active' if self.status else 'Inactive'}"  # Returns a string representation of the feature.

    class Meta:
        verbose_name = 'ویژگی سرویس'  # Persian for "Service Feature"
        verbose_name_plural = 'ویژگی های سرویس'  # Persian for "Service Features"


class PlanPrice(models.Model):
    # Represents pricing details for a specific service plan.
    plan = models.ForeignKey(
        ServicePlan,
        on_delete=models.CASCADE,
        related_name="prices",  # Allows access to pricing details from the service plan.
        verbose_name="پلن",  # The service plan associated with this pricing.
    )
    min_price = models.BigIntegerField(verbose_name="کف قیمت")  # Minimum price for the service plan.
    max_price = models.BigIntegerField(verbose_name="بالاترین قیمت")  # Maximum price for the service plan.
    payment_steps = models.IntegerField(verbose_name="تعداد مراحل پرداخت")  # Number of payment steps for the plan
    def __str__(self):
        return f"{self.plan} - Price Range: {self.min_price} to {self.max_price}"  # Returns a string representation of the pricing details.

    class Meta:
        verbose_name = "قیمت پلن"  # Persian for "Plan Price"
        verbose_name_plural = "قیمت های پلن"  # Persian for "Plan Prices"