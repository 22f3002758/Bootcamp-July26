from flask import Flask
from backend.models import *
from datetime import datetime

def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydb.sqlite3"
    db.init_app(app)
    app.app_context().push()
    return app

app=create_app()
# db.create_all()
from backend.routes import *
from backend.create_initial_data import *

# if Admin.query.first() is None:
#     admin=Admin(email='admin@gmail.com', password="pass")
#     db.session.add(admin)

# if Professional.query.first() is None:
#     prof1=Professional(email='prof1@gmail.com', password='asdf',name='john', address='wert',mobile='98986763',experience='3',status='registered')
#     prof2=Professional(email='prof2@gmail.com', password='asdf',name='jenny', address='wert',mobile='9898676453',experience='4',status='registered')   
#     db.session.add_all([prof1,prof2])

# if Package.query.first() is None:
#     pack1=Package(title='Home Cleaning', price='500', description="afdyewhgfekfh", prof_id=1,status='approved',start_date=datetime(2026,8,2),end_date=datetime(2026,9,2))    
#     pack2=Package(title='Gardening', price='500', description="afdyewhgfekfh", prof_id=1,status='approved',start_date=datetime(2026,8,2),end_date=datetime(2026,9,2))    
#     pack3=Package(title='Kitchen Cleaning', price='500', description="afdyewhgfekfh", prof_id=2,status='approved',start_date=datetime(2026,8,2),end_date=datetime(2026,9,2))    
#     db.session.add_all([pack1,pack2,pack3])
# db.session.commit()    

# prof_obj=db.session.query(Professional).filter_by(id=1).first()
# print(prof_obj)
# print(prof_obj.name)


# pack_obj=db.session.query(Package).filter_by(id=1).first()
# print(pack_obj)
# print(pack_obj.professional)
# print(pack_obj.professional.name)

if __name__=="__main__":
    app.run(debug=True)