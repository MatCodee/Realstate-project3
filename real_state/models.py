from django.db import models
import boto3
from app.settings import AWS_STORAGE_BUCKET_NAME,DEBUG


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    

class Property(models.Model):
    SALE = 'sale'
    RENT = 'rent'

    CATEGORIES_CHOICES = (
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('office', 'Office'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=(
        (SALE, 'Sale'),
        (RENT, 'Rent'),
    ))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    square_meters = models.DecimalField(max_digits=10, decimal_places=2)
    bathrooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    car_parking = models.PositiveBigIntegerField(default=0)
    main_image = models.ImageField(upload_to='property_images')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_popular = models.BooleanField(default=False)

    # Add other additional fields as needed, such as specific property features (pool, garage, etc.)

    def __str__(self):
        return self.title
    
    
    def delete(self, *args, **kwargs):
        # Eliminar la imagen principal de S3
        self.delete_s3_image(self.main_image)
        super().delete(*args, **kwargs)

    def delete_s3_image(self, image_field):
        if image_field and not DEBUG:
            s3 = boto3.resource('s3')
            bucket = AWS_STORAGE_BUCKET_NAME  
            s3_key = image_field.name

            s3.Object(bucket, s3_key).delete()
    
    


class AdditionalImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='property_images')

    def __str__(self):
        return f"Additional Image for {self.property.title}"
    
    def delete(self, *args, **kwargs):
        # Eliminar la imagen adicional de S3
        self.delete_s3_image(self.image)

        super().delete(*args, **kwargs)

    def delete_s3_image(self, image_field):
        if image_field and not DEBUG:
            s3 = boto3.resource('s3')
            bucket = AWS_STORAGE_BUCKET_NAME  
            s3_key = image_field.name

            s3.Object(bucket, s3_key).delete()