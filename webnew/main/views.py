from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')

def contact(request):
    return render(request, 'main/contact.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

        send_mail(
            subject=f"Portfolio contact: {subject or 'No subject'}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        messages.success(request, "Your message was sent successfully.")
        return redirect("contact")

    return render(request, "main/contact.html")