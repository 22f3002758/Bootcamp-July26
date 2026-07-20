from flask import current_app as app
from flask import request, render_template,redirect
from .models import*
from flask_login import login_user, logout_user,login_required,current_user

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register',methods=['POST','GET'])
def register():
    if request.args.get("role")=='customer' and request.method=='GET':
        return render_template('customer/register.html')
    if request.args.get("role")=='professional' and request.method=='GET':
        return render_template('professional/register.html')
    elif request.method=='POST' and request.args.get("role")=='customer':
        fname=request.form.get("cust_name")
        femail=request.form.get("cust_email")
        fpwd=request.form.get("cust_pwd")
        fadd=request.form.get("cust_address")
        fmobile=request.form.get("cust_mobile")
        cust=db.session.query(Customer).filter_by(email=femail).first()   
        if cust:
            return "Customer already exist!"
        else:
            newcust=Customer(name=fname,email=femail, password=fpwd,address=fadd,mobile=fmobile,status='registered')
            db.session.add(newcust)
            db.session.commit() 
        return redirect("/login")    
    elif request.method=='POST' and request.args.get("role")=='professional':
        fname=request.form.get("p_name")
        femail=request.form.get("p_email")
        fpwd=request.form.get("p_pwd")
        fadd=request.form.get("p_address")
        fmobile=request.form.get("p_mobile")
        fexp=request.form.get("p_exp")
        resume=request.files.get("resume")
        prof=db.session.query(Professional).filter_by(email=femail).first()   
        if prof:
            return "Professional already exist!"
        else:
            newprof=Professional(name=fname,email=femail, password=fpwd,address=fadd,mobile=fmobile,experience=fexp,status='registered',resume="#")
            db.session.add(newprof)
            db.session.commit() 
        return redirect("/login")    

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        femail=request.form.get("email")
        fpwd=request.form.get("pwd")
        user= db.session.query(Professional).filter_by(email=femail).first() or \
            db.session.query(Customer).filter_by(email=femail).first() or \
            db.session.query(Admin).filter_by(email=femail).first() 
        
        if user:
            print("hello")
            if user.password==fpwd:
                if isinstance(user, Professional):
                    login_user(user)
                    return redirect("professional/dashboard")
                
                elif isinstance(user, Customer):
                    login_user(user)
                    return redirect(f"customer/dashboard") 
                elif isinstance(user, Admin):
                    login_user(user)
                    return redirect(f"admin/dashboard") 
                    
            else:
                return "check your credentials"
        else:
            return "user not found"    


@app.route('/admin/dashboard',methods=['GET','POST'])  
@login_required
def admin_dash():
    return f"Welcome to admin dashboard{current_user.email}"     

@app.route('/professional/dashboard',methods=['GET','POST'])  
@login_required
def prof_dash():
    return "Welcome to professional dashboard"   

@app.route('/customer/dashboard',methods=['GET','POST'])  
@login_required
def cust_dash():
    
    return f"Welcome to customer dashboard{current_user.email}"    


