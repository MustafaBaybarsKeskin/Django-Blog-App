from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 80,verbose_name = "Başlık")
    content = models.TextField(verbose_name= "İçerik")
    summary = models.TextField(verbose_name="Özet")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    image = models.ImageField(blank = True,null = True,verbose_name="Fotoğraf Ekleyin")
    post_views = models.IntegerField(default=0, null=True, blank=True)

    category_choices = (
    ("GENEL", "Genel"),
    ("ELEKTRONIK", "Elektronik"),
    ("YAZILIM", "Yazılım"),
    ("EGLENCE", "Eğlence"),

    )

    category = models.CharField(max_length=20, null=True, blank=True, choices=category_choices)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']