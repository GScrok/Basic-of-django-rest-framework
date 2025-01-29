from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Skill: {self.name}>"
