from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse
from django.conf import settings
import uuid

# Create your models here.
class Genre(models.Model):
  name = models.CharField(
    max_length=200,
    unique=True,
    help_text="Enter the book genre"
  )

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("genre_detail", args=[str(self.id)])
  
  class Meta:
     constraints = [
        UniqueConstraint(
           Lower('name'),
           name='genre_name_case_insensitive_unique',
           violation_error_message='This genre already exists.'
        )
     ]

###################################################################
class Image(models.Model):
   url = models.CharField(max_length=350)
   alt = models.CharField(max_length=200)

   def __str__(self) -> str:
      return self.alt

###################################################################
class Language(models.Model):
   description = models.CharField(max_length=100, unique=True)
   abbrev = models.CharField(max_length=5)

   def __str__(self) -> str:
      return f"{self.description} - {self.abbrev}"
   
   def get_absolute_url(self):
      return reverse("lang_detail", args=[str(self.id)])
   
   class Meta:
    constraints = [
            UniqueConstraint(
              Lower('description'),
              name='genre_description_unique',
              violation_error_message='This language already exists.'
            )
        ]

###################################################################
class Author(models.Model):
   fname= models.CharField('First Name',max_length=200)
   lname= models.CharField('Last Name',max_length=200)
   date_birth= models.DateField('Date of Birth', null=True, blank=True)
   date_death= models.DateField('Date of Death', null=True, blank=True)

   def __str__(self) -> str:
      return f"{self.fname} {self.lname}"
   
   def get_absolute_url(self):
      return reverse("author_detail", args=[str(self.id)])
   
   class Meta:
     ordering = ['lname','fname']
  
###################################################################
class Book(models.Model):
  title = models.CharField(max_length=200)

  author = models.ForeignKey(
    Author,
    on_delete=models.RESTRICT,
    null=True
  )

  summary = models.TextField(
    max_length=1000,
    help_text="Enter brief book description",
    null=True
  )

  isbn = models.CharField(
    'ISBN',
    max_length=13,
    unique=True,
    help_text='13 characters ISBN for more info:'
  )

  genre = models.ManyToManyField(
    Genre,
    related_name='books',
    help_text="Select a genre for this book"
  )

  image = models.ImageField(
    # upload_to= 'catalog/static',
    default='not-available.jpg',
    null=True,
    blank=True
  )

  language = models.ForeignKey(
    Language,
    on_delete=models.RESTRICT,
    null=True,
    blank=True
  )

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("book_detail", args=[str(self.id)])

###################################################################
class Status(models.Model):
   name=models.CharField(
      max_length=80,
      unique= True
    )
   
   def __str__(self):
    return self.name
   
   def get_absolute_url(self):
      return reverse("status_detail", args=[str(self.id)])
   
   class Meta:
     constraints = [
        UniqueConstraint(
           Lower('name'),
           name='genre_name_unique',
           violation_error_message='This status already exists.'
        )
     ]
   
###################################################################
class BookInstance(models.Model):
  id = models.UUIDField(primary_key=True, default= uuid.uuid4)
  book=models.ForeignKey(
    Book,
    on_delete= models.RESTRICT,
    null= True
  )
  imprint=models.CharField(max_length=200, null=True)
  due_back=models.DateField(blank=True, null=True)
  status=models.ForeignKey(
    Status,
    on_delete= models.RESTRICT,
    null= True
  )
  
  def __str__(self):
    return f"{self.id} - {self.book.title}"
   
  class Meta:
     ordering = ['due_back']
