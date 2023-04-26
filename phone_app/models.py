from django.db import models


# Create your models here.

class Phones(models.Model):
    MODEL_PHONE = (
        ('Простые', 'Простые'),
        ('Бюджетные', 'Бюджетные'),
        ('Высокого класса', 'Высокого класса'),
        ('Премиум класса', 'Премиум класса'),
        ('Элитные', 'Элитные')
    )

    title = models.CharField('Название телефона', max_length=100)
    description = models.TextField('Описание телефона', blank=True)
    image = models.ImageField('фото:', upload_to='')
    video = models.URLField('Видео')
    cost = models.CharField('Стоимость в $', max_length=100, null=True)
    model_phone = models.CharField('Модель телефонов', max_length=100, choices=MODEL_PHONE)
    сreated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


# для отзыва
class Reviews(models.Model):
    RATING = ((i, '*' * i) for i in range(1, 6))
    comment = models.CharField('Комментарий', max_length=500, null=True)
    choice_film = models.ForeignKey(Phones, on_delete=models.CASCADE, related_name='reviews', null=True)
    rate = models.IntegerField('Оценка', choices=RATING, null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment