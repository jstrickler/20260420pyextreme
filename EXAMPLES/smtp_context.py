import smtplib  # create context-aware class
from getpass import getpass

SMTP_HOST = 'smtp2go.com'
SMTP_PORT = 2525
SMTP_USER = 'pythonclass'
SMTP_PASSWORD = getpass("SMTP password: ")

SENDER = 'jstrickler@gmail.com'
RECIPIENTS = ['jstrickler@gmail.com']

MESSAGE = '''Subject: SMTP example
Hello hello?
Testing email from Python
'''


class SMTPOpener():  # create context-aware class

    def __init__(self, host, port, username, password, debug=False):  # __init__() accepts instance parameters
        self._smtpserver = smtplib.SMTP(host, port)
        self._smtpserver.login(username, password)
        self._smtpserver.set_debuglevel(debug)

    def __enter__(self):  # called at beginning of block; returns SMTP object
        return self._smtpserver

    def __exit__(self, exc_type, exc_value, tb):  # called at end of block
        self._smtpserver.quit()  # quit SMTP server object


with SMTPOpener(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, True) as so:  # create SMTPOpener object with a context block
    so.sendmail(
        SENDER,
        RECIPIENTS,
        MESSAGE
    )
# after last line, obj.__exit__() is called, which in turn calls quit() on SMTP object
