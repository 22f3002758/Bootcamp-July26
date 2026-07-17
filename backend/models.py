from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    email = db.Column(db.String, unique=True , nullable=False)
    password = db.Column(db.String , nullable=False)
    

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    email = db.Column(db.String, unique=True , nullable=False)
    password = db.Column(db.String , nullable=False)
    name = db.Column(db.String , nullable=False)
    address = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    bookings = db.relationship("Booking", backref="customer",cascade="all, delete-orphan", lazy=True)
    


class Professional(db.Model): # table name professional
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    email = db.Column(db.String, unique=True , nullable=False)
    password = db.Column(db.String , nullable=False)
    name = db.Column(db.String , nullable=False)
    address = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    experience = db.Column(db.String,nullable = False)
    status = db.Column(db.String, nullable=False)
    resume_url = db.Column(db.String)
    packages = db.relationship("Package", backref="professional",cascade="all, delete-orphan", lazy=True) # backref is used to access parent table information from child table
    bookings = db.relationship("Booking", backref="professional",cascade="all, delete-orphan", lazy=True)
    
    
class Package(db.Model):# table name package
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    title = db.Column(db.String, unique=True , nullable=False)
    price = db.Column(db.String , nullable=False)
    description= db.Column(db.String , nullable=False)
    prof_id = db.Column(db.Integer ,db.ForeignKey("professional.id") , nullable=False ) # db.ForeignKey("tablename.attribute")
    status = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date , nullable =False)
    end_date = db.Column(db.Date , nullable =False)
    bookings = db.relationship("Booking", backref="package",cascade="all, delete-orphan", lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key =True , autoincrement=True)
    
    total_price = db.Column(db.String , nullable=False)
    start_time = db.Column(db.Time , nullable =False)
    end_time = db.Column(db.Time) 
    date = db.Column(db.Date , nullable =False)
    status = db.Column(db.String, nullable=False)
    prof_id = db.Column(db.Integer ,db.ForeignKey("professional.id") , nullable=False )
    pack_id =  db.Column(db.Integer ,db.ForeignKey("package.id") , nullable=False )
    cust_id = db.Column(db.Integer ,db.ForeignKey("customer.id") , nullable=False)