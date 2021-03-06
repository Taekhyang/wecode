from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta(object):
        db_table = 'menus'


class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    
    class Meta(object):
        db_table = 'categories'


class Drink(models.Model):
    korean_name  = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description  = models.TextField(max_length=1000)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)

    allergy_drink = models.ManyToManyField(
                                           'Allergy',
                                           through='AllergyDrink',
                                         # through_fields=('drink', 'allergy'),
                                           blank=True
                                          )

    class Meta(object):
        db_table = 'drinks'


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta(object):
        db_table = 'allergies'


class AllergyDrink(models.Model):
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE, null=True)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE, null=True)

    class Meta(object):
        db_table = 'allergies_drinks'


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta(object):
        db_table = 'images'


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg        = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g  = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g         = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g        = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg      = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml          = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)
    drink            = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta(object):
        db_table = 'nutritions'
