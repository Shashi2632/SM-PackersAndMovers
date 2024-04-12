from django.shortcuts import render, redirect
from django.conf import settings
from smtplib import SMTPException
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_notification(data):
    user_subject = "Thank You for Contacting smpackersandmovers.com"
    company_subject = "New Inquiry - smpackersandmovers.com"
    
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email_user = data['email']
    to_email_company = 'rahul35895@gmail.com'

    # Load the HTML templates for user and company emails
    html_message_user = render_to_string('Admin_App/thankyou-email.html', {'data': data})
    html_message_company = render_to_string('Admin_App/inquiry-email.html', {'data': data})

    try:
        # Send the email to the user
        email_user = EmailMultiAlternatives(user_subject, strip_tags(html_message_user), from_email, [to_email_user])
        email_user.attach_alternative(html_message_user, "text/html")
        email_user.send()

        # Send the email to the company
        email_company = EmailMultiAlternatives(company_subject, strip_tags(html_message_company), from_email, [to_email_company])
        email_company.attach_alternative(html_message_company, "text/html")
        email_company.send()

    except SMTPException as e:
        # Handle SMTPException
        print(f"Error sending email: {e}")

    except Exception as e:
        # Catch any other exceptions
        print(f"Unexpected error: {e}")

    # Any cleanup or additional actions you want to perform
    pass

def email_inquiry(request):
    pass
    return render(request, 'thankyou-email.html')

