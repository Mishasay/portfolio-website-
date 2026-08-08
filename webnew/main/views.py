import json
import os
import urllib.request
import urllib.error

from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def skills(request):
    return render(request, "main/skills.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")

        full_message = f"""
Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

        api_key = os.environ.get("BREVO_API_KEY")
        sender_email = os.environ.get(
            "BREVO_SENDER_EMAIL",
            "mykhailosharov@gmail.com"
        )
        contact_email = os.environ.get(
            "CONTACT_EMAIL",
            "mykhailosharov@gmail.com"
        )

        data = {
            "sender": {
                "name": "Portfolio Website",
                "email": sender_email,
            },
            "to": [
                {
                    "email": contact_email,
                    "name": "Misha",
                }
            ],
            "subject": f"Portfolio contact: {subject or 'No subject'}",
            "textContent": full_message,
            "replyTo": {
                "email": email,
                "name": name,
            },
        }

        req = urllib.request.Request(
            "https://api.brevo.com/v3/smtp/email",
            data=json.dumps(data).encode("utf-8"),
            headers={
                "accept": "application/json",
                "api-key": api_key,
                "content-type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                response.read()

            messages.success(
                request,
                "Your message was sent successfully."
            )

        except urllib.error.HTTPError as error:
            error_body = error.read().decode("utf-8", errors="ignore")
            print("Brevo API error:", error.code, error_body)

            messages.error(
                request,
                "Failed to send the message. Please try again later."
            )

        except Exception as error:
            print("Email error:", error)

            messages.error(
                request,
                "Failed to send the message. Please try again later."
            )

        return redirect("contact")

    return render(request, "main/contact.html")