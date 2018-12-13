from django.shortcuts import render

# Create your views here.
def signup_view(request):
    render(request, 'accounts/signup.html')
