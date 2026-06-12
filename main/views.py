from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings    
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_msg = form.save()

            # Send email notification
            try:
                send_mail(
                    subject=f'New Contact from {contact_msg.name}',
                    message=f'''
You have a new contact form submission!

Name:    {contact_msg.name}
Email:   {contact_msg.email}
Service: {contact_msg.service}
Other:   {contact_msg.other_service}
Budget:  {contact_msg.budget}

Message:
{contact_msg.message}

---
Reply directly to: {contact_msg.email}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.NOTIFY_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email error: {e}")

            return redirect('contact_success')

    return render(request,'contact.html', {'form':form})

def contact_success(request):
    return render(request, 'contact_success.html')