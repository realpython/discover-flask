from app import db
from models import User

# insert data
# db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
# db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("michael", "michael@mherman.org", "i'll-never-tell"))

# commit the changes
db.session.commit()
