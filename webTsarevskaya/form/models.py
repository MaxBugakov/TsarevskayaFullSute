from django.db import models


class Feedback(models.Model):

    # Выбор размера
    size_choices = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )

    surname = models.CharField("Фамилия", max_length=50)
    name = models.CharField("Имя", max_length=50)
    patronymic = models.CharField("Отчество", max_length=50)
    email = models.EmailField("Почта")
    height = models.IntegerField("Рост")
    weight = models.IntegerField("Вес")
    clothes_size = models.CharField(max_length=50, choices=size_choices)
    foot_size = models.IntegerField("Размер ноги")

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
