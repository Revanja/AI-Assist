import datetime

def get_name():
    return "My name is AI Operating System Assistant."

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def handle_invalid():
    return "I cannot perform this command right now, please try again."