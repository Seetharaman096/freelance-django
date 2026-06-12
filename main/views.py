from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import threading

def send_email_async(subject, message, from_email, recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=True,
        )
    except Exception:
        pass

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()

            # Send email in background thread — won't block the response
            email_thread = threading.Thread(
                target=send_email_async,
                args=(
                    f'New Contact from {contact_msg.name}',
                    f'''
New contact form submission!

Name:    {contact_msg.name}
Email:   {contact_msg.email}
Service: {contact_msg.service}
Other:   {contact_msg.other_service}
Budget:  {contact_msg.budget}

Message:
{contact_msg.message}

Reply to: {contact_msg.email}
                    ''',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.NOTIFY_EMAIL],
                )
            )
            email_thread.daemon = True
            email_thread.start()

            return redirect('contact_success')

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')