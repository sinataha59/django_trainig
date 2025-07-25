from django.db import models

class product(models.Model):
    name = models.CharField( max_length=250)
    description = models.TextField()
    slug = models.SlugField()
    datetime_created = models.DateTimeField( auto_now=False, auto_now_add=True)
    datetime_modified = models.DateTimeField( auto_now=True, auto_now_add=False)
    inventory = models.IntegerField(default =0)
    price = models.DecimalField( max_digits=6, decimal_places=2)
    category = models.ForeignKey(category)

class category (models.Model) :
    title = models.CharField(max_length = 250)
    discription = models.SlugField(blank = True)


class customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField( max_length=254)
    phone_number = models.CharField( max_length=50)
    birth_date = models.DateField(null = True , blank = True)
    
class order(models.Model):
    PAIDORDER = "P"
    UNPAIDORDER = "U"
    CANCELEDORDER = 'C'
    
    ORDERSTATUS =[
        
        (PAIDORDER,"paid"),
        (UNPAIDORDER,"unpaid"),
        (CANCELEDORDER,"canceled"),
       
    ]
    
    customer_name = models.ForeignKey(customer)
    datetime_creat = models.DateTimeField(auto_now =False , auto_now_add = True) 
    status = models.CharField(max_length = 255 , choices = ORDERSTATUS , default = UNPAIDORDER)
    product = models.ForeignKey(product)
 
 
class coment(models.Model):
     name = models.ForeignKey(customer)
     text = models.models.CharField( max_length=500)
     datetime_created = models.DateTimeField(auto_now_add =True)
     product = models.ForeignKey(product)