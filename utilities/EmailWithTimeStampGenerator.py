from datetime import datetime


def get_new_email_with_timestamp():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "amotoori" + timestamp + "@gmail.com"
