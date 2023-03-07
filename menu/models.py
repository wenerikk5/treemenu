from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True)
    slug = models.SlugField(
        max_length=255,
        verbose_name='Slug',
        null=True,
    )
    named_url = models.CharField(
        max_length=255,
        verbose_name='Named URL',
        blank=True,
    )

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'
       
    def get_full_path(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = f'/{self.slug}/'
        return url

    def __str__(self) -> str:
        return self.name
    

class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='menu',
        verbose_name='Menu item',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Item name'
    )
    parent = models.ForeignKey(
        'self',
        related_name='item',
        verbose_name='Parent item',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    named_url = models.CharField(
        max_length=255,
        verbose_name='Named URL',
        blank=True,
        unique=True,
    )
    lft = models.PositiveIntegerField(
        default=0,
        verbose_name='Left key*',
        help_text='*Do not fill. Will be calculated automatically.',
    )
    rht = models.PositiveIntegerField(
        default=0,
        verbose_name='Right key*',
        help_text='*Do not fill. Will be calculated automatically.',
    )
    level = models.PositiveIntegerField(
        default=0,
        verbose_name='Nesting level*',
        help_text='*Do not fill. Will be calculated automatically.',
    )

    class Meta:
        ordering = ('level', 'lft', 'id',)
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
    
    def __str__(self) -> str:
        return self.name 

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = '/'
        return url
