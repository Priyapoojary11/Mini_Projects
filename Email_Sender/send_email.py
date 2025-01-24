import yagmail

#Set up the yagmail client
yag = yagmail.SMTP(user="softwaredevelopment.own.website@gmail.com", password="ualp jswb ctom pgfd")

#Compose and send the email
receiver_email = "softwaredevelopment.own.website@gmail.com"
subject = "Test Email from yagmail"
body = "Hello, this is a test email sent using yagmail in Python!"

# html_body = """
# <h1>Hello</h1><p>I'm writing html content text.</p>
# """

# Sending the email
yag.send(to=receiver_email, subject=subject, contents=body)

print("Email sent successfully!")