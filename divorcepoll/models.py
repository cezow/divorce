from django.db import models


class Question(models.Model):
    name = models.TextField(max_length=255, blank=True)
    text = models.TextField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.text
