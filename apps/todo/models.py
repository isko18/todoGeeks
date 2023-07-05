from django.db import models

# Create your models here.

class Task(models.Model):

    id = models.AutoField(
        primary_key=True,
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание",
        blank=True, null=True
    )
    completed = models.BooleanField(
        verbose_name="Статус",
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )


    def __str__(self):
        return f"{self.id} {self.title}"
    
    class Meta:
        verbose_name = "Такси"
        verbose_name_plural = "Таски"