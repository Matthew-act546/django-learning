from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    
    my_context = {
        "my_text": "This is a homepage",
        "my_number": 314156,
        "my_list": [1234, 4321, 1342, "string!"],
        "my_html": "<h1>Hello World</h1>",
        "my_title": "matthew david title"
    }
    return render(request, 'home.html', my_context)

def contact_view(request,*args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})