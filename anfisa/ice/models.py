from django.db import models


class Player(models.Model):
    player_id = models.CharField(
        max_length=100,
        verbose_name='id игрока',
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя игрока',
    )
    entrance_date = models.DateTimeField(
        verbose_name='Время входа игрока',
        auto_now_add=True,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.name


class Boost(models.Model):
    boost_id = models.CharField(
        max_length=100,
        verbose_name='id бонуса',
    )
    boost_type = models.CharField(
        max_length=100,
        verbose_name='Тип бонуса',
    )
    player = models.ManyToManyField(
        Player,
        related_name='pleer',
        verbose_name='Владелец бонуса',
        through='PlayerBoost',
    )

    class Meta:
        ordering = ['boost_type']
        verbose_name = 'Игровой бонус'
        verbose_name_plural = 'Игровые бонусы'

    def __str__(self):
        return self.boost_type


class PlayerBoost(models.Model):
    player_boost = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        verbose_name='Участник',
    )
    boost = models.ForeignKey(
        Boost,
        on_delete=models.CASCADE,
        verbose_name='Бонусы участника',
    )

    class Meta:
        ordering = ['player_boost']
        verbose_name = 'Полученый игровой бонус'
        verbose_name_plural = 'Полученые игровые бонусы'

    def __str__(self):
        return self.player_boost.name, self.boost.boost_type
