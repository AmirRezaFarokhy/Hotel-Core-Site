from django.db import models
from base.mixin import BaseDateMixin
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    separator = "-"

    def __str__(self):
        return self.id.__str__() + self.separator + str(self.created_at)

    def soft_delete(self, save=True):
        self.deleted_at = timezone.now()
        if save:
            self.save()