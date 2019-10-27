from datetime import datetime, timedelta
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    link = models.TextField()
    # Placeholder
    img = models.TextField()

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=100)
    pfp = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRulunu8E-aVZNgnnTzrxHScCIraIHL0sqfX4v1BF94yqZe97x2&s"
    last_delivered = datetime.now().date()
    interval = timedelta(weeks=1)
    items = [Item(), Item()]
    associated = []

    def add_associated(self, name):
        self.associated += [name]
        return

    def set_name(self, name):
        self.name = name
        return

    def set_pfp(self, pic):
        self.pfp = pic
        return

    def add_item(self, item):
        self.items += [item]
        return

    def delete_item(self, item):
        new_items = []
        for obj in items:
            if obj != item:
                new_items += [obj]
        self.items = new_items
        return

    def set_item_count(self, item, count):
        self.items_dict[item] = count
        return

    def __str__(self):
        return self.name
