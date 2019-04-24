import os
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "find-a-mentor.settings")

django.setup()

from mentorsforall.models import Account, Profile, Message, Subject, Event
from django.contrib.auth import get_user_model

User = get_user_model()

## remove all subjects

[ s.delete() for s in Subject.objects.all() ]

s1 = Subject(name='Travelling', category='L')
s2 = Subject(name='Taekwondo', category='HANDF')
s3 = Subject(name='Dancing', category='HANDF')
s4 = Subject(name='Astronomy', category='AC')
s5 = Subject(name='French', category='LANG')
s6 = Subject(name='German', category='LANG')
s7 = Subject(name='Communication', category='L')
s8 = Subject(name='Confidence', category='L')
s9 = Subject(name='Ballet', category='AR')
s10 = Subject(name='Film Making', category='AR')
s11 = Subject(name='Acting', category='AR')
s12 = Subject(name='Gardening', category='L')
s13 = Subject(name='Project Management', category='P')
s14 = Subject(name='Architecture', category='P')
s15 = Subject(name='Pottery', category='L')
s16 = Subject(name='Piano', category='I')
s17 = Subject(name='Violin', category='I')
s18 = Subject(name='Viola', category='I')
s19 = Subject(name='Tennis', category='HANDF')
s20 = Subject(name='Yoga', category='HANDF')
s21 = Subject(name='Korean', category='LANG')
s22 = Subject(name='Presentation', category='P')
s23 = Subject(name='Environmental Science', category='AC')
s24 = Subject(name='Dentistry', category='AC')

s1.save()
s2.save()
s3.save()
s4.save()
s5.save()
s6.save()
s7.save()
s8.save()
s9.save()
s10.save()
s11.save()
s12.save()
s13.save()
s14.save()
s15.save()
s16.save()
s17.save()
s18.save()
s19.save()
s20.save()
s21.save()
s22.save()
s23.save()
s24.save()

#Delete all accounts
[ a.delete() for a in Account.objects.all() ]

#Recreate test accounts
a1 = Account(username='test1', email='test1@test.com')
a1.set_password('test')
a1.save()

a2 = Account(username='test2', email='test2@test.com')
a2.set_password('test')
a2.save()

a3 = Account(username='test3', email='test3@test.com')
a3.set_password('test')
a3.save()

a4 = Account(username='test4', email='test4@test.com')
a4.set_password('test')
a4.save()

a5 = Account(username='test5', email='test5@test.com')
a5.set_password('test')
a5.save()

a6 = Account(username='test6', email='test6@test.com')
a6.set_password('test')
a6.save()

a7 = Account(username='test7', email='test7@test.com')
a7.set_password('test')
a7.save()

a8 = Account(username='test8', email='test8@test.com')
a8.set_password('test')
a8.save()

a9 = Account(username='test9', email='test9@test.com')
a9.set_password('test')
a9.save()

a10 = Account(username='test10', email='test10@test.com')
a10.set_password('test')
a10.save()

a11 = Account(username='test11', email='test11@test.com')
a11.set_password('test')
a11.save()

a12 = Account(username='test12', email='test12@test.com')
a12.set_password('test')
a12.save()

[ p.delete() for p in Profile.objects.all() ]

p1 = Profile(image='', gender='F', job='Developer', role='TEE', about='Hi! I\'m Sheb!', birthdate='1997-04-15', givenname='Lili', familyname='Rochefort', city='London', accountid=a1)
p1.save()

p2 = Profile(image='', gender='F', job='Teacher', role='TOR', about='Hi! I\'m Nina', birthdate='1997-04-15', givenname='Nina', familyname='Williams', city='London', accountid=a2)
p2.save()

p3 = Profile(image='', gender='M', job='Martial Artist', role='TOR', about='Hi! I\'m Hwoarang', birthdate='1997-04-15', givenname='Hwoa', familyname='Rang', city='London', accountid=a3)
p3.save()

p4 = Profile(image='', gender='M', job='Student', role='TEE', about='Hi! I\'m Armour King. The less cool of the kings.', birthdate='1997-01-19', givenname='Armour', familyname='King', city='London', accountid=a4)
p4.save()

p5 = Profile(image='', gender='M', job='Architect', role='TOR', about='Hi! I\'m Dragunov!', birthdate='1997-01-19', givenname='Sergei', familyname='Dragunov', city='London', accountid=a5)
p5.save()

p6 = Profile(image='', gender='F', job='Teacher', role='TOR', about='Hi! I\'m Asuka!', birthdate='1997-01-19', givenname='Asuka', familyname='Kazama', city='London', accountid=a6)
p6.save()

p7 = Profile(image='', gender='M', job='Project Manager', role='TOR', about='Hi! I\'m Jin!', birthdate='1997-01-19', givenname='Jin', familyname='Kazama', city='London', accountid=a7)
p7.save()

p8 = Profile(image='', gender='F', job='Store Manager', role='TOR', about='Hi! I\'m Anna!', birthdate='1997-01-19', givenname='Anna', familyname='Williams', city='London', accountid=a8)
p8.save()

p9 = Profile(image='', gender='M', job='Student', role='TEE', about='Hi! I\'m Paul!', birthdate='1997-01-19', givenname='Paul', familyname='Phoenix', city='London', accountid=a9)
p9.save()

p10 = Profile(image='', gender='F', job='Unemployed', role='TEE', about='Hi! I\'m Xiaoyu!', birthdate='1997-01-19', givenname='Ling', familyname='Xiaoyu', city='London', accountid=a10)
p10.save()

with open('mentorsforall/static/images/profileimg/id1.png', 'rb') as img:
    p1.image.save('', img)

with open('mentorsforall/static/images/profileimg/id2.png', 'rb') as img:
    p2.image.save('', img)

with open('mentorsforall/static/images/profileimg/id3.png', 'rb') as img:
    p3.image.save('', img)

with open('mentorsforall/static/images/profileimg/id4.png', 'rb') as img:
    p4.image.save('', img)

with open('mentorsforall/static/images/profileimg/id5.png', 'rb') as img:
    p5.image.save('', img)

with open('mentorsforall/static/images/profileimg/id6.png', 'rb') as img:
    p6.image.save('', img)

with open('mentorsforall/static/images/profileimg/id7.png', 'rb') as img:
    p7.image.save('', img)

with open('mentorsforall/static/images/profileimg/id8.png', 'rb') as img:
    p8.image.save('', img)

with open('mentorsforall/static/images/profileimg/id9.png', 'rb') as img:
    p9.image.save('', img)

with open('mentorsforall/static/images/profileimg/id10.png', 'rb') as img:
    p10.image.save('', img)

p1.subjects.add(s1, s15, s12)
p2.subjects.add(s4, s3, s2, s16)
p3.subjects.add(s2, s1, s14)
p4.subjects.add(s3, s4, s6)
p5.subjects.add(s11, s15, s12, s17, s14)
p6.subjects.add(s6, s7, s5)
p7.subjects.add(s7, s12, s18)
p8.subjects.add(s8, s15, s9, s16, s17, s19)
p9.subjects.add(s9, s15, s17, s19, s18, s3)
p10.subjects.add(s6, s15, s16, s17, s11, s9, s5)

## remove all profiles
[ m.delete() for m in Message.objects.all() ]

m1 = Message(sender=p1, receiver=p2, content="Private Hey!", public=False)
m2 = Message(sender=p1, receiver=p2, content="Public Hello!", public=True)
m3 = Message(sender=p2, receiver=p3, content="Private Hi!", public=False)
m4 = Message(sender=p2, receiver=p3, content="Public Wassup!", public=True)
m5 = Message(sender=p5, receiver=p6, content="Private Hi!", public=False)
m6 = Message(sender=p6, receiver=p4, content="Public Wassup!", public=True)
m7 = Message(sender=p8, receiver=p10, content="Private Hi!", public=False)
m8 = Message(sender=p4, receiver=p10, content="Private Hi!", public=False)
m9 = Message(sender=p1, receiver=p10, content="Public Wassup!", public=False)
m10 = Message(sender=p9, receiver=p10, content="Public Wassup!", public=True)
m11 = Message(sender=p4, receiver=p10, content="Private Hi!", public=False)
m12 = Message(sender=p2, receiver=p8, content="Public Wassup!", public=True)
m13 = Message(sender=p5, receiver=p8, content="Public Wassup!", public=True)
m14 = Message(sender=p1, receiver=p8, content="Public Wassup!", public=True)
m15 = Message(sender=p6, receiver=p3, content="Public Wassup!", public=True)
m16 = Message(sender=p2, receiver=p7, content="Public Wassup!", public=True)
m17 = Message(sender=p6, receiver=p9, content="Public Wassup!", public=True)
m18 = Message(sender=p1, receiver=p6, content="Public Wassup!", public=True)

m1.save()
m2.save()
m3.save()
m4.save()
m5.save()
m6.save()
m7.save()
m8.save()
m9.save()
m10.save()
m11.save()
m12.save()
m13.save()
m14.save()
m15.save()
m16.save()
m17.save()
m18.save()

[ e.delete() for e in Event.objects.all() ]

e1 = Event(image='', date='2019-04-15', time='16:00', public=True, name='Meet and Greet', about='I would like to meet all my potential mentees altogether so we can spend time getting to know eachother.', host=p8, location='Hyde Park', city='London')
e1.save()
e1.subjects.add(s15)
e1.attendees.add(p1, p4, p9)
e1.invitees.add(p1, p4, p5)

e2 = Event(image='', date='2019-01-20', time='12:00', public=True, name='Demonstration and FAQ', about='Holding a public Dojo session for your questions.', host=p3, location='KTigers Dojo', city='Seoul')
e2.save()
e2.subjects.add(s2)
e2.attendees.add(p4)
e2.invitees.add(p4, p6)

e3 = Event(image='', date='2019-12-04', time='10:00', public=False, name='Coffee Meet', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='London')
e3.save()
e3.subjects.add(s4,s6)
e3.attendees.add(p8, p10)
e3.invitees.add(p1, p5)

e4 = Event(image='', date='2019-12-04', time='12:00', public=True, name='Park Meetup', about='Bring your snacks! We are going to talk about architecture!', host=p2, location='Hyde Park', city='London')
e4.save()
e4.subjects.add(s14)
e4.attendees.add(p1)
e4.invitees.add(p1, p5)

e5 = Event(image='', date='2019-12-04', time='10:00', public=True, name='Demonstration and FAQ', about='Holding a public Dojo session for your questions.', host=p7, location='KTigers Dojo', city='Seoul')
e5.save()
e5.subjects.add(s8, s15, s9, s16, s17, s19)
e5.attendees.add(p4, p3, p9)
e5.invitees.add(p1, p5)

e6 = Event(image='', date='2019-12-04', time='10:00', public=True, name='Coffee Meet 2', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='London')
e6.save()
e6.subjects.add(s4,s6)
e6.attendees.add(p1, p4, p3, p9)
e6.invitees.add(p1, p5)

e7 = Event(image='', date='2019-12-04', time='10:00', public=True, name='Coffee Meet 3', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='Paris')
e7.save()
e7.subjects.add(s8, s15, s9, s16, s17, s19)
e7.attendees.add(p8)
e7.invitees.add(p1, p5)

e8 = Event(image='', date='2019-12-04', time='10:00', public=False, name='Coffee Meet 4', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='London')
e8.save()
e8.subjects.add(s4,s6)
e8.attendees.add(p9, p4, p10)
e8.invitees.add(p1, p5)

e9 = Event(image='', date='2019-12-04', time='10:00', public=False, name='Coffee Meet 5', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='Paris')
e9.save()
e9.subjects.add(s8, s15, s9, s16, s17, s19)
e9.attendees.add(p4, p3, p9)
e9.invitees.add(p1, p5, p4, p3, p9)

e10 = Event(image='', date='2019-12-04', time='10:00', public=True, name='Coffee Meet 6', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='Seoul')
e10.save()
e10.subjects.add(s4,s6)
e10.attendees.add(p6)
e10.invitees.add(p1, p5)

e11 = Event(image='', date='2019-12-04', time='10:00', public=False, name='Coffee Meet 7', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='Paris')
e11.save()
e11.subjects.add(s8, s15, s9, s16, s17, s19)
e11.attendees.add(p7)
e11.invitees.add(p1, p5)

with open('mentorsforall/static/images/eventimg/hydepark.jpg', 'rb') as img:
    e1.image.save('', img)

with open('mentorsforall/static/images/eventimg/dojo.jpg', 'rb') as img:
    e2.image.save('', img)

with open('mentorsforall/static/images/eventimg/cafe.jpeg', 'rb') as img:
    e3.image.save('', img)

with open('mentorsforall/static/images/eventimg/hydepark2.jpeg', 'rb') as img:
    e4.image.save('', img)

with open('mentorsforall/static/images/eventimg/dojo2.jpeg', 'rb') as img:
    e5.image.save('', img)

with open('mentorsforall/static/images/eventimg/cafe2.jpeg', 'rb') as img:
    e6.image.save('', img)

with open('mentorsforall/static/images/eventimg/hydepark3.jpg', 'rb') as img:
    e7.image.save('', img)

with open('mentorsforall/static/images/eventimg/cafe3.jpeg', 'rb') as img:
    e8.image.save('', img)

with open('mentorsforall/static/images/eventimg/hydepark4.jpeg', 'rb') as img:
    e9.image.save('', img)

with open('mentorsforall/static/images/eventimg/cafe4.jpeg', 'rb') as img:
    e10.image.save('', img)

with open('mentorsforall/static/images/eventimg/cafe.jpeg', 'rb') as img:
    e11.image.save('', img)

User.objects.create_superuser(username='admin', password='password', email='admin@test.com')
print("\nAdmin user created: admin/admin (email: admin@test.com)\n")
