from django.core.mail import EmailMessage
import os


class Util:
    @staticmethod
    def send_email(data,name=None,resetpassword=None):
        link = data['body']
        email = EmailMessage(
            subject=data['subject'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )

        if resetpassword == None:
            with open('account\\email_static_files\\verify.html', 'r') as file:
                html_content = file.read()
 
            html_content = html_content.replace('Hey SmilesDavis',f'Hey {name}')
            html_content = html_content.replace('href="#"',f'href="'+link+'"')
            email.content_subtype = "html"
            email.body = html_content
            email.send()

        if resetpassword == True:
            with open('account\\email_static_files\\verify.html', 'r') as file:
                html_content = file.read()
 
            html_content = html_content.replace('Hey SmilesDavis',f'Hey {name}')
            html_content = html_content.replace('>Verify Email</a>','>Password = <b>'+link+'</b></a>')
            html_content = html_content.replace('Wowwee! Thanks for registering an account with Impala! We are Waiting for you.',"A request has been received to change the password for your impala account")
            html_content = html_content.replace("Before we get started, we'll need to verify your email.","Here is your new password you can login with this password")
            email.content_subtype = "html"
            email.body = html_content
            email.send()
            