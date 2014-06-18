from app import db
from models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "I\'m okay."))

# commit the changes
db.session.commit()
