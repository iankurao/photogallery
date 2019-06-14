from django.shortcuts import render

# Create your views here.
# Create your views here.

def home(request):
    message='My Photos'
    try:
        images=Image.get_images()

    except Exception as e:
        raise  Http404()

    locations=Location.get_location()
    return render(request,"index.html",{'message':message})
