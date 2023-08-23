from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
# ^using just "from models" doesn't work for some reason
from django.db.models import Avg

def index(request):
    try:
      book_list = Book.objects.all().order_by("-rating","title")
      book_count = book_list.count()
      average_rating = book_list.aggregate(Avg("rating"))

      return render(request, "book_outlet/index.html", {
        "book_list": book_list,
        "book_count": book_count,
        "average_rating": average_rating
      })
    except:
       raise Http404()

def book_detail(request, slug):
    # try:
    #   book = Book.objects.get(pk=id)
    #   # ^pk means primary key. you can still use id=id but this is more explicit
    #   return render(request, "book_outlet/book_detail.html", {"book": book})
    # except:
    #   raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {"book": book})