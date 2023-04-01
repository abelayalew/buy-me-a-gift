from django.db import models
from django.utils import timezone
from uuid import uuid4

NULL = {'null': True, 'blank': True}


class BaseModelMixin(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created_at = models.DateTimeField(default=timezone.localtime, editable=False)
    updated_at = models.DateTimeField(**NULL)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = timezone.localtime()

        super().save(*args, **kwargs)
