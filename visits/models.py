import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Worker(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} ph:{self.phone}'

class RetailPoint(BaseModel):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.worker})'


class Visit(BaseModel):
    datetime = models.DateTimeField(auto_now_add=True)
    retail_point = models.ForeignKey(RetailPoint, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.worker.name} visited {self.retail_point.name} @ {self.datetime}'