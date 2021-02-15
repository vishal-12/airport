from django.db import models

# Create your models here.

class AirpotLoungeModel(models.Model):

    class Meta:
        db_table = 'tbl_Lounge1'
        verbose_name = "Lounge Data"
        verbose_name_plural = "LG Lounge Access"
        ordering = ("-created_at",)

    name = models.CharField(max_length=256, default="Delhi AirPort Lounge")
    price = models.CharField(max_length=256, default=5000)
    size = models.CharField(max_length=256, default=12)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}".format(self.name)
