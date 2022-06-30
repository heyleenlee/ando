from datetime import datetime

from django.db import models


# Create your models here.
class AssetCash(models.Model):
    id = models.AutoField
    index = models.IntegerField(default=0)
    userId = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    remark = models.CharField(max_length=50)
    createdAt = models.DateTimeField(default=datetime.now(),)
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'AssetCash'  # 数据库表名
