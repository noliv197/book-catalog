from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as loginUser, get_user_model, logout as logoutUser
from django.contrib import messages
from .models import *
# from .forms import *

def home(request):
    try:
        books = Book.objects.all().count()
        instances = BookInstance.objects.all().count()
        available_instance = BookInstance.objects.filter(status__name='Available').count()
        authors = Author.objects.all().count()

        template = loader.get_template('home.html')
        context = {
        'book_amount': books,
        'authors_amount': authors,
        'instance_amount': instances,
        'available_instance_amount': available_instance,
        'menu_links': [
           {'href': '/', 'text': 'HOME', 'active': 'active'},
           {'href': '/catalog', 'text': 'CATALOG', 'active': ''},
           {'href': '/catalog/authors', 'text': 'AUTHORS', 'active': ''},
           {'href': '/admin', 'text': 'ADMIN', 'active': '', 'admin': True},
        ]
        }
        return HttpResponse(template.render(context, request))
    except Exception as err:
        print(err)

def catalog(request):
  try:
    books = Book.objects.all()
    genres = Genre.objects.all()

    template = loader.get_template('catalog.html')
    catalog = []
    for genre in genres:
       books = list(genre.books.all().values())
       book_count = len(books)
       catalog.append({'genreName': genre, 'books': books, 'book_count': book_count})
    
    context = {
      'catalog': catalog,
      'lenGenres': len(catalog),
      'menu_links': [
           {'href': '/', 'text': 'HOME', 'active': ''},
           {'href': '/catalog', 'text': 'CATALOG', 'active': 'active'},
           {'href': '/catalog/authors', 'text': 'AUTHORS', 'active': ''},
           {'href': '/admin', 'text': 'ADMIN', 'active': '', 'admin': True},
        ]
    }
    return HttpResponse(template.render(context, request))
  except Exception as err:
    print(err) 

def book_detail(request, id): 
  try:
    book = Book.objects.get(id=id)
    genres = Genre.objects.filter(books__id=id)
    template = loader.get_template('book_detail.html')

    context = {
      'book': book,
      'genres': genres,
      'menu_links': [
           {'href': '/', 'text': 'HOME', 'active': ''},
           {'href': '/catalog', 'text': 'CATALOG', 'active': ''},
           {'href': '/catalog/authors', 'text': 'AUTHORS', 'active': ''},
           {'href': '/admin', 'text': 'ADMIN', 'active': '', 'admin': True},
        ]
    }
    return HttpResponse(template.render(context, request))
  except Exception as err:
    print(err) 

def authors(request):
  try:
    template = loader.get_template('authors.html')
    authors = Author.objects.all().values()

    context = {
      'authors': authors,
      'menu_links': [
           {'href': '/', 'text': 'HOME', 'active': ''},
           {'href': '/catalog', 'text': 'CATALOG', 'active': ''},
           {'href': '/catalog/authors', 'text': 'AUTHORS', 'active': 'active'},
           {'href': '/admin', 'text': 'ADMIN', 'active': '', 'admin': True},
        ]
    }
    return HttpResponse(template.render(context, request))
  except Exception as err:
    print(err) 
        
def author_detail(request, id):
  
  try:
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author__id=id)
    template = loader.get_template('author_detail.html')

    context = {
      'author': author,
      'books': books,
      'menu_links': [
           {'href': '/', 'text': 'HOME', 'active': ''},
           {'href': '/catalog', 'text': 'CATALOG', 'active': ''},
           {'href': '/catalog/authors', 'text': 'AUTHORS', 'active': ''},
           {'href': '/admin', 'text': 'ADMIN', 'active': '', 'admin': True},
        ]
    }
    return HttpResponse(template.render(context, request))
  except Exception as err:
    print(err) 
      
def logout(request):
  try:
    logoutUser(request)
    return redirect("login")
  except Exception as err:
    print(err) 
  
def login(request):
  try:
    # if request.method == 'POST':
    #   form = LoginForm(request.POST)
    #   if form.is_valid():
    #     username = form.cleaned_data['username']
    #     password = form.cleaned_data['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #       login(request, user)    
    #       return redirect('home')
    # else:
    #   form = LoginForm()
    # return render(request, 'login.html', {'form': form})
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(username=username, password=password)

          if user is not None:
              loginUser(request, user)
              return redirect('home')
          else:
              messages.warning(request, "Invalid credentials", "alert-warning")
              return redirect('login')
      else:
          return render(request, 'login.html')
    
  except Exception as err:
    print(err) 

def register(request):
   try:
      if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        User = get_user_model()
        userExists = User.objects.filter(email=email)
      
        if (userExists):
            messages.warning(request, "Email already registered", "alert-warning")
            return redirect('register')
      
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        if user is not None:
            loginUser(request, user)
            return redirect('home')
        else:
            messages.warning(request, "unable to register", "alert-warning")
            return redirect('register')
      else:
        return render(request, 'register.html')
   except Exception as err:
    print(err)
