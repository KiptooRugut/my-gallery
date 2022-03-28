from django.db import models
import datetime as dt


# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.firstname
    
    def save_user(self):
        self.save()
    
    def delete_user(self):
        self.delete()


class Category(models.Model):
    name=models.CharField(max_length=30)
   
    
    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__name__icontains=search_term)
        return gallery
    
class Location(models.Model):
    location=models.CharField(max_length=30)
    user = models.ForeignKey('User',on_delete=models.CASCADE,)
     
    def __str__(self):
        return self.location

class Image(models.Model):
    title = models.CharField(max_length=60)
    description= models.TextField(blank=False,default="Image description")
    #image field
    image=models.ImageField(upload_to='images/',default="Image")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,title,description):
        self.title = title
        self.description = description
        self.category = Category
        self.save()

    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.get(id=id)
        return image

    @classmethod
    def filter_by_location(cls,search_location):
        gallery = cls.objects.filter(location__name__icontains=search_location).all()
        return gallery
        
    @classmethod
    def search(cls,search_term):
        gallery=cls.objects.filter(title__icontains=search_term)
        return gallery


