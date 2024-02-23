from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books' : books,
    }
    return render(request, 'libraries/index.html', context)


def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    comments = book.review_set.all()
    review_form = ReviewForm(request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review_form.save()
        return redirect('libraries:detail', book.pk)
    else:
        review_form = ReviewForm()
    context = {
        'book' : book,
        'review_form' : review_form,
        'comments' : comments,
    }

    return render(request, 'libraries/detail.html', context)