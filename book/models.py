import uuid

from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(verbose_name=_('Называние'), max_length=1000)
    description = models.TextField(verbose_name=_('Описание'))
    author = models.CharField(verbose_name=_('Автор'), max_length=1000)
    price = models.DecimalField(verbose_name=_('цена'), decimal_places=2, max_digits=6)
    cover = models.ImageField(verbose_name=_('Обложка'), upload_to='covers/', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index')
        ]
        permissions = [
            ('special_status', 'Can read all books')
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews', verbose_name=_('Обсуждаемая книга')
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("Автор коммента"))
    review = models.TextField(verbose_name=_('Comment'))

    def __str__(self):
        return self.review
