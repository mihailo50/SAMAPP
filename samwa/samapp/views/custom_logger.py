# custom_logging.py
import logging
from django.core.mail import mail_admins

class EmailNotificationHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        subject = f'Error occurred in application: {record.levelname}'
        message = self.format(record)
        mail_admins(subject, message)
