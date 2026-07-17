from .models import db , Admin , Customer , Professional , Package , Booking
from flask import current_app as app
from datetime import datetime

with app.app_context():
    db.create_all()
    if Admin.query.first() is None: 
        admin=Admin(email="admin@gmail.com",password="admin123")
        db.session.add(admin)
    if Professional.query.first() is None:
        prof1=Professional(email="prof1@gmail.com",password="prof123",name="John Doe",address="123 Main St",mobile="1234567890",experience="5 years",status="Active",resume_url="https://example.com/resume1.pdf")
        prof2=Professional(email="prof2@gmail.com",password="prof123",name="Jane Smith",address="456 Elm St",mobile="9876543210",experience="3 years",status="Active",resume_url="https://example.com/resume2.pdf")
        db.session.add(prof1)
        db.session.add(prof2)
    if Customer.query.first() is None:
        cust1=Customer(email="cust1@gmail.com",password="cust123",name="Alice Brown",address="789 Oak St",mobile="5555555555",status="Active")
        cust2=Customer(email="cust2@gmail.com",password="cust123",name="Bob Green",address="321 Pine St",mobile="4444444444",status="Active")
        db.session.add(cust1)
        db.session.add(cust2)

    if Package.query.first() is None:
        pack1=Package(title="Basic Package",price="100",description="Basic service package",prof_id=1,status="Active",start_date=datetime(2024,1,1),end_date=datetime(2024,12,31))
        pack2=Package(title="Premium Package",price="200",description="Premium service package",prof_id=2,status="Active",start_date=datetime(2024,1,1),end_date=datetime(2024,12,31))
        pack3=Package(title="Deluxe Package",price="300",description="Deluxe service package",prof_id=1,status="Active",start_date=datetime(2024,1,1),end_date=datetime(2024,12,31))
        db.session.add(pack1)
        db.session.add(pack2)
        db.session.add(pack3)
    db.session.commit()