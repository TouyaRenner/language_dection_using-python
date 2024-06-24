import imaplib
import email
from email.header import decode_header
import os

# Email account credentials
username = "tuf1440@gmail.com"
password = "touya_2004"

# IMAP settings
imap_server = "imap.example.com"
imap_port = 993

# Function to decode email subject
def decode_subject(subject):
    decoded_subject = ""
    if subject:
        decoded_parts = decode_header(subject)
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                if encoding:
                    decoded_subject += part.decode(encoding)
                else:
                    decoded_subject += part.decode()
            else:
                decoded_subject += part
    return decoded_subject

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imap_server, imap_port)
mail.login(username, password)
mail.select("inbox")

# Search for all emails
result, data = mail.search(None, "ALL")
if result == "OK":
    for num in data[0].split():
        result, data = mail.fetch(num, "(RFC822)")
        if result == "OK":
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            # Get email subject
            subject = msg["Subject"]
            decoded_subject = decode_subject(subject)
            
            # Get email body
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
            else:
                body = msg.get_payload(decode=True).decode()
            
            # Store email in a text file
            email_id = num.decode("utf-8")
            filename = f"{email_id}_{decoded_subject}.txt"
            with open(filename, "w") as f:
                f.write(f"Subject: {decoded_subject}\n\n")
                f.write(body)
            
            print(f"Email {email_id} saved as {filename}")

# Logout and close connection
mail.logout()
