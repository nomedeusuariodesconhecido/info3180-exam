from app.models import Emails
from app import db

contact1 = Emails('Allan', 'Angus', 'allan.angus@flask.com')
contact2 = Emails('Barbara', 'Baggins', 'barbara.baggins@flask.com')
contact3 = Emails('Daniel', 'Dunn', 'daniel.dunn@flask.com')
contact4 = Emails('Carl', 'Cuff', 'carl.cuff@flask.com')
contact5 = Emails('Justine', 'Jetta', 'justine.jetta@flask.com')
contact6 = Emails('Elian', 'Elton' , 'elian.elton@flask.com')
contact7 = Emails('Francine', 'Ffrench', 'francine.ffrench@flask.com')
contact8 = Emails('Georgette', 'Glaxon', 'georgette.glaxon@flask.com')
contact9 = Emails('Harry', 'Houdini', 'harry.houdini@flask.com')
contact10 = Emails('Ilias', 'Ingram', 'ilias.ingram@flask.com')



db.session.add(contact1)
db.session.add(contact2)
db.session.add(contact3)
db.session.add(contact4)
db.session.add(contact5)
db.session.add(contact6)
db.session.add(contact7)
db.session.add(contact8)
db.session.add(contact9)
db.session.add(contact10)

db.session.commit()