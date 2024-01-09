from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
import smtplib, ssl
from email.message import EmailMessage
# from django.core.mail import send_mail



def message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["message"]
            user_email = form.cleaned_data["email"]
            obj = Message(text=text, email=user_email)
            obj.save()

            messages.success(request, "your message has been sent successfuly!")
        else:
            messages.warning(request, "somthing went wrong!")
    else:
        form = MessageForm()
    return render(request, 'message.html', {'form':form})


@receiver(post_save, sender=Message)
def print_message_created_or_updated(sender, instance, created, **kwargs):
    if not created and (instance.respond_title or instance.respond_text):
        port = 465
        sender, password = "artinmohajeri@gmail.com", "iqxh ikau caba tyod"
        to = instance.email
        subject = instance.respond_title
        message = instance.respond_text
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.send_message(msg)
