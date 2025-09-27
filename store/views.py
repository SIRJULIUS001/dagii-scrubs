
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GalleryImage
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home(request):
    images = GalleryImage.objects.all()[:4]  # show latest 4
    return render(request, "home.html", {"images": images})
def about(request):
    return render(request, 'about.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Add success message
        messages.success(request, "✅ Your message was sent successfully! We’ll get back to you soon.")
        return redirect("home")  # redirect to clear form data

    return render(request, "contact.html")

def blog_list(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "blog_list.html", {"posts": posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "blog_detail.html", {"post": post})

# Create your views here.
