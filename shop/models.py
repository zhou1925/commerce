from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)

    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,
                                                    self.slug])



