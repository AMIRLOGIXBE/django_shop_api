from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="دسته‌بندی"
    )
    title = models.CharField(max_length=64, verbose_name="عنوان")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="products/%Y/%m", verbose_name="تصویر")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    discount_price = models.PositiveBigIntegerField(
        null=True, blank=True, verbose_name="قیمت با تخفیف"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title