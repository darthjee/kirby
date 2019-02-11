from django.db import models

class Recipe(Base):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
