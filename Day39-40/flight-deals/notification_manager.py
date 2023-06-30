from smtplib import SMTP
import os

class NotificationManager:
    
    def __init__(self):
        self.my_email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("PASSWORD")

    def send_email(self,emails,message, google_flight_link):
        
        for email in emails:
            with SMTP("smtp.gmail.com") as self.smtp:
                self.smtp = SMTP("smtp.gmail.com")
                self.smtp.starttls()
                self.smtp.login(user=self.my_email, password=self.password)    
                self.smtp.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode("utf8")
                )  
