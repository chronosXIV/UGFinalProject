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

s1.save()
s2.save()
s3.save()
s4.save()
s5.save()
s6.save()
s7.save()
s8.save()

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

[ p.delete() for p in Profile.objects.all() ]

p1 = Profile(image='', gender='F', job='Developer', role='TEE', about='Hi! I\'m Sheb!', birthdate='1997-04-15', givenname='Lili', familyname='Rochefort', city='London', accountid=a1)
p1.save()

p2 = Profile(image='', gender='F', job='Teacher', role='TOR', about='Hi! I\'m Nina', birthdate='1997-04-15', givenname='Nina', familyname='Williams', city='London', accountid=a2)
p2.save()

p3 = Profile(image='', gender='M', job='Martial Artist', role='TOR', about='Hi! I\'m Hwoarang', birthdate='1997-04-15', givenname='Hwoa', familyname='Rang', city='London', accountid=a3)
p3.save()

p4 = Profile(image='', gender='M', job='Student', role='TEE', about='Armourrrr kiiiingggg', birthdate='1997-01-19', givenname='Armour', familyname='King', city='London', accountid=a4)
p4.save()

p5 = Profile(image='', gender='M', job='Student', role='TEE', about='idkwhothisiswaitforitlol', birthdate='1997-01-19', givenname='Sergei', familyname='Dragunov', city='London', accountid=a5)
p5.save()

p6 = Profile(image='', gender='F', job='Student', role='TEE', about='do i like my cousin hmmm', birthdate='1997-01-19', givenname='Asuka', familyname='Kazama', city='London', accountid=a6)
p6.save()

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

p1.subjects.add(s1, s5)
p2.subjects.add(s4, s3, s2)
p3.subjects.add(s2, s1)
p4.subjects.add(s3, s4, s6)
p5.subjects.add(s8, s5, s2)
p6.subjects.add(s6, s7)

## remove all profiles
[ m.delete() for m in Message.objects.all() ]

m1 = Message(sender=p1, receiver=p2, content="Private Hey!", public=False)
m2 = Message(sender=p1, receiver=p2, content="Public Hello!", public=True)
m3 = Message(sender=p2, receiver=p3, content="Private Hi!", public=False)
m4 = Message(sender=p2, receiver=p3, content="Public Wassup!", public=True)
m5 = Message(sender=p5, receiver=p6, content="Private Hi!", public=False)
m6 = Message(sender=p6, receiver=p4, content="Public Wassup!", public=True)

m1.save()
m2.save()
m3.save()
m4.save()
m5.save()
m6.save()

[ e.delete() for e in Event.objects.all() ]

e1 = Event(image='', date='2019-04-15', time='16:00', public=True, name='Meet and Greet', about='I need to meet with all my potential pupils at once.', host=p2, location='Hyde Park', city='London')
e1.save()
e1.subjects.add(s4)
e1.attendees.add(p1, p4)
e1.invitees.add(p1, p4, p5)

e2 = Event(image='', date='2019-01-20', time='12:00', public=True, name='Demonstration and FAQ', about='Holding a public Dojo session for your questions.', host=p3, location='KTigers Dojo', city='Seoul')
e2.save()
e2.subjects.add(s2)
e2.attendees.add(p4)
e2.invitees.add(p4, p6)

e3 = Event(image='', date='2019-12-04', time='10:00', public=False, name='Coffee Meet', about='Meet me, your mentor, for a coffee so we can talk about stuff.', host=p2, location='Starbucks', city='London')
e3.save()
e3.subjects.add(s4,s6)
e3.attendees.add(p1)
e3.invitees.add(p1, p5)

with open('mentorsforall/static/images/eventimg/hydepark.jpg', 'rb') as img:
    e1.image.save('', img)

with open('mentorsforall/static/images/eventimg/dojo.jpg', 'rb') as img:
    e2.image.save('', img)

with open('mentorsforall/static/images/eventimg/cafe.jpeg', 'rb') as img:
    e3.image.save('', img)

User.objects.create_superuser(username='admin', password='password', email='admin@test.com')
print("\nAdmin user created: admin/admin (email: admin@test.com)\n")
