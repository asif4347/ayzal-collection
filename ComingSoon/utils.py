from django.core.mail import EmailMultiAlternatives


def send_email(subject, text_content, html_content, to):

    from_email = 'test_from@gmail.com'
    subject = 'New Project Created'
    text_content = 'A Test'
    html_content = """
        <h3 style="color: #0b9ac4>email received!</h3>
    """
    email_body = html_content
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(email_body, "text/html")
    msg.send()
