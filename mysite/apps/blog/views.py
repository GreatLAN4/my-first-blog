from django.http import HttpResponse
from django.shortcuts import render
def post_list(request):
    # return HttpResponse("Hello, World!!!")
    return render(request, 'blog/post_list.html', {})
