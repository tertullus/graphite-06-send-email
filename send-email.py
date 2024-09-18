import smtplib
import ssl


class UserClass:
    def __init__(self, name, age, location, email):
        self.__name = name
        self.__age = age
        self.__location = location
        self.__email = email

    def view_user_data(self):
        print("User's name:", self.__name)
        print("User's age:", self.__age)
        print("User's location:", self.__location)
        print("User's email:", self.__email)

    def change_user_data(self):
        self.__name = input("Change the user's name: ")
        self.__age = input("Change the user's age: ")
        self.__location = input("Change the user's location: ")
        self.__email = input("Change the user's email: ")

    def send_email_to(self):
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = self.__email
        receiver_email = input(
            "Enter your email address, and I'll text you now: ")
        password = "vkyf qrbe brmi apgk"
        message = """\
        Subject: User Class with Email Functionality

        Implemented successfully with great help from my mentor, Toyin."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


user_01 = UserClass("Chi", 23, "Lagos", "apoklips3797@gmail.com")
user_01.send_email_to()
