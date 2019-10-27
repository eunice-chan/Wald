from datetime import datetime, timedelta
from django.db import models

# Create your models here.
class Account(models.Model):
    last_delivered = datetime.now().date()
    interval = timedelta(weeks=1)
    items_dict = {}

    def add_item(item):
        if item not in self.items_dict.keys():
            set_item_count(item, 1)
        return

    def delete_item(item):
        if item in self.items_dict.keys():
            del self.items_dict[item]
        return

    def set_item_count(item, count):
        self.items_dict[item] = count
        return
