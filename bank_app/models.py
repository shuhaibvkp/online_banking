from django.db import models

# Create your models here.


class reg1model1(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    file=models.FileField(upload_to="bank_app/static")
    pin=models.CharField(max_length=10)


class regmodel1(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    file = models.FileField(upload_to="bank_app/static")
    pin = models.CharField(max_length=10)
    balance=models.IntegerField()
    account=models.IntegerField()


class addamount(models.Model):
    uid=models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class withmoney(models.Model):
    uid = models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)



class ministatement(models.Model):
    choice = [
        ('withdraw', 'withdraw'),
        ('deposite', 'deposite'),
        ('all', 'all')
    ]
    statement = models.IntegerField(choices=choice)

class newsmodel(models.Model):
    topic=models.CharField(max_length=300)
    content=models.CharField(max_length=3000)
    date=models.DateField(auto_now=True)


class wishlist(models.Model):
    uid = models.IntegerField()
    newsid = models.IntegerField()

    topic = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)
    date = models.DateField()