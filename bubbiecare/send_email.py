import smtplib
import os
import ssl
from load_dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

username = "ameya23711@gmail.com"
pw = os.getenv("EMAIL_PW")
context = ssl.create_default_context()

def send_email(id: int, name: str, to_addr: str, content: str | None = None):
    msg = EmailMessage()
    msg["Subject"] = "BubbieCare: You have been shortlisted for an opportunity"
    msg["From"] = username
    msg["To"] = to_addr
    if content is None:
        msg.set_content(f"""Hi {name}
        
        Your profile on BubbieCare has been shortlisted as a 'Best/Potential' match for a new opportunity
        
        To move forward, please take the pre-interview questionnaire by clicking this LINK - http://localhost:5173/test?id={id}
        
        Once you submit your test, we will evaluate the same and connect on next steps!
        
        Thank you,
        Team BubbieCare""")
    else:
        msg.set_content(content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, pw)
            server.send_message(msg)
    except Exception as e:
        print(f"Error: {e}")
