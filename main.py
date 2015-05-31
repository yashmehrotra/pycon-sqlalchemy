from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
 
engine = create_engine('sqlite:///:memory:') # Add echo=True for viewing SQL Queries
Session = sessionmaker(bind=engine)
Base = declarative_base()
 
 
class User(Base):
    __tablename__ = 'users'
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
 
    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)
 
 
# import pdb;pdb.set_trace()
Base.metadata.create_all(engine)

# Creating multiple users
user = [ User(name='Yash', email='yashmehrotra95@gmail.com'),
         User(name='Avijit', email='526avijit@gmail.com'),
         User(name='Bruce', email='bruce@wayne.com') ]

session = Session()
# add_all is used for adding a list
session.add_all(user)
session.commit()

query = session.query(User)
print 'All users so far:'
for row in query:
    print row.name, row.email

# Updating a user through filtering
query = session.query(User).filter(User.email == 'yashmehrotra95@gmail.com')[0]
query.name = 'Yash Mehrotra'
session.add(query)
session.commit()

query = session.query(User)
print '\nAll users after update:'
for row in query:
    print row.name, row.email

# Deleting a user through filtering
query = session.query(User).filter(User.email == 'yashmehrotra95@gmail.com')[0]

session.delete(query)
query = session.query(User)
print '\nAll users after delete:'
for row in query:
    print row.name, row.email
session.close()
