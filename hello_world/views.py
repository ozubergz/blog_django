from django.shortcuts import render
# from django.http import HttpResponse

# data
posts = [
    {
      'author': 'CoreyMS',
      'title': 'Blog Post 1',
      'content': 'First post content',
      'date_posted': 'August 27, 2018'
    },
    {
      'author': 'Jane Doe',
      'title': 'Blog Post 2',
      'content': 'August post content',
      'date_posted': 'August 28, 2018'
    }
]


def home(request):

    context = {
        'posts': posts
    }

    return render(request, 'hello/home.html', context)


def about(request):

    return render(request, 'hello/about.html', {'title': 'About'})