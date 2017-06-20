import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'project.settings')

import django
django.setup()
from project.models import User, MediaItem, MediaHistory, Topics

def populate():

    users = [
        {"user_id":"JByrnes",
         "first_name":"John",
         "last_name":"Byrnes"},
        {"user_id":"RMcGinley",
         "first_name":"Robert",
         "last_name":"McGinley"} ]

    topics = [
        {"topic": "Android Development"},
        {"topic": "Software Development"},
        {"topic": "JavaScript/jQuery"},
        {"topic": "Information Security"},
        {"topic": "Cyber Security"},
        {"topic": "Android Development"},
        {"topic": "Django"}
    ]

    media_items = [
        {"type":"Book",
         "title":"Introduction to Android Application Development: Android Essentials",
         "isbn":"978-0321940261",
         "author":"Annuzzi, Joseph Jr., Lauren Darcey and Shane Conder",
         "topic":"Android Development",
         "subtopic":"Software Development"},
        {"type":"Book",
         "title":"Murach's JavaScript and jQuery",
         "isbn":"978-1890774707",
         "author":"Murach, Mike and Zak Ruvalcaba",
         "topic":"JavaScript/jQuery",
         "subtopic":"Software Development"},
        {"type":"Book",
         "title":"Principles of Information Security",
         "isbn":"978-1111138219",
         "author":"Whitman, Michael E. and Herbert J. Mattord",
         "topic":"Information Security",
         "subtopic":"Cyber Security"},
        {"type":"Book",
         "title":"Tango With Django: A beginner's guide to web development",
         "isbn":"N/A",
         "author":"Azzopardi, Leif and David Maxwell",
         "topic":"Django",
         "subtopic":"Software Development"} ]

    item_history = [
        {"date_out":"2017-06-01",
         "date_due":"2017-06-15",
         "date_returned":"2017-06-19",
         "borrower":"JByrnes",
         "media":"Tango With Django: A beginner's guide to web development"},
        {"date_out": "2017-06-01",
         "date_due": "2017-06-15",
         "date_returned": "2017-06-14",
         "borrower": "RMcGinley",
         "media":"Murach's JavaScript and jQuery"} ]

    for topic in topics:
        add_topic(topic["topic"])

    for user in users:
        add_user(user["user_id"],user["first_name"],user["last_name"])

    for item in media_items:
        add_media(item["type"],item["title"],item["isbn"],item["author"],item["topic"],item["subtopic"])

    for history in item_history:
        add_media_history(history["date_out"],history["date_due"],history["date_returned"],history["borrower"],history["media"])

def add_topic(topic):
    t = Topics.objects.get_or_create(topic=topic)[0]
    t.save()
    return t

def add_user(user_id, first_name, last_name):
    u = User.objects.get_or_create(user_id=user_id, first_name=first_name, last_name=last_name)[0]
    u.save()
    return u

def add_media_history(date_out, date_due, date_returned, borrower, media):
    borrower_id = User.objects.get(user_id=borrower).id
    media = MediaItem.objects.get(title=media).id
    print(media)
    h = MediaHistory.objects.get_or_create(date_out=date_out, date_due=date_due,
                                           date_returned=date_returned, borrower_id=borrower_id, media_item_id=media)[0]
    h.save()
    return h

def add_media(type, title, isbn, author, topic, subtopic):
    m = MediaItem.objects.get_or_create(type=type, title=title, isbn=isbn, author=author)[0]
    m.topic = Topics.objects.get(topic=topic)
    # m.subtopic = Topics.objects.get(topic=subtopic)
    m.save()
    return m

if __name__ == '__main__':
    print("Starting Media Library population script...")
    populate()