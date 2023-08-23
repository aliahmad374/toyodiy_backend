from django.core.mail import EmailMessage
import os


class Util:
    @staticmethod
    def send_email(data,name,orderid,usertype):
        email = EmailMessage(
            subject=data['subject'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )

        with open('cartorder\\email_static_files\\verify.html', 'r') as file:
            html_content = file.read()

        if usertype != 'admin':
            try:
                html_content = html_content.replace('Hey SmilesDavis',f'Hey {name}')
                html_content = html_content.replace('Wowwee! Thanks for registering an account with Impala! We are Waiting for you.',"Thank You For Placing an Order with Impala Please Find Your Order ID Below")
                html_content = html_content.replace("Before we get started, we'll need to verify your email.",f"Oder#ID : {orderid}")
                email.content_subtype = "html"
                email.body = html_content
                email.send()
            except Exception as E:
                print(E)
                pass
        if  usertype == 'admin':
            try:
                html_content = html_content.replace('Hey SmilesDavis',f'Hey Admin')
                html_content = html_content.replace('Wowwee! Thanks for registering an account with Impala! We are Waiting for you.',f"A New Order has been placed by {name}")
                html_content = html_content.replace("Before we get started, we'll need to verify your email.",f"Oder#ID : {orderid}")
                email.content_subtype = "html"
                email.body = html_content
                email.send()
            except Exception as E:
                print(E)
                pass

            
            