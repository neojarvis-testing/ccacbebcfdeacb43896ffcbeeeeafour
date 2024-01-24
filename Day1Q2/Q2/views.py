from django.shortcuts import render

# Create your views here.
def greet_user(request):
    
    name = request.GET.get('name', 'Guest')
    return render(request, './greet_user.html', {'name': name})
