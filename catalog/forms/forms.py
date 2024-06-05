from django.forms import ModelForm
from ..models import *
from django.contrib.auth import get_user_model

# Create the form class.
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genre", "language", ""]

class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model(),
        fields = ["username", "email", "password"]

# Creating a form to add an article.
book_form = BookForm()
register_form = RegisterForm()

# # Creating a form to change an existing article.
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)