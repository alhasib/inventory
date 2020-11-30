from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 


class SubCategory(models.Model):
    name = models.CharField(max_length = 250)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 


class Item(models.Model):
    name = models.CharField(max_length = 250)
    invoice = models.CharField(max_length = 250, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE, blank = True, null = True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    expense_quantity = models.IntegerField(default=0)
    available_quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 
    

class ProposeItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank = True, null = True)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    checked_in_status = models.BooleanField(default = 0)
    admin_approval = models.BooleanField(default=0)
    delivery_status = models.BooleanField(default=0)
    
    def __str__(self):
        return str(self.id)


class Assign(models.Model):
    date = models.DateField(auto_now_add=True)
    proposal = models.OneToOneField(ProposeItem, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


class AssignItem(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE, blank=True, null=True)
    invoice = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.item)
