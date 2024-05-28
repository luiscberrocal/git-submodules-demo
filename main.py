# This is a sample Python script.
import os

from config import load_environment_variables
from simple_mail.email.mailer import send_email
from simple_mail.email.schema import EmailMessage, SenderConfig

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == "__main__":
    load_environment_variables(environment_filename="email_vars.txt", source_folder_name=".secrets")
    username = os.getenv("EMAIL")
    pwd = os.getenv("PASSWORD")
    print(f"Username: {username}")  # noqa: T201

    sender_config = SenderConfig(email=username, password=pwd)
    email_message = EmailMessage(
        recipients=["luis.berrocal.1942@gmail.com"],
        subject="Submodule test",
        content="This is a test email from the submodule.",
        sender_config=sender_config
    )
    send_email(email_message=email_message)
    print("Email sent!")  # noqa: T201

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
