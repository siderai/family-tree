from django.db import models


class Human(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mother_id = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mothers_children",
        verbose_name="mother",
    )
    father_id = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fathers_children",
        verbose_name="father",
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "people"
        verbose_name_plural = "people"
