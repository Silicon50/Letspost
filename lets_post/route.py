from flask import render_template, url_for, flash, redirect
from lets_post import app, db, bcrypt 
from lets_post.form import RegistrationForm, LoginForm #for forms
from lets_post.models import User, Post #for database settings
from flask_login import login_user, current_user, logout_user#loggin user,check if the current user is logged in,logout user



posts = [
    {
        'author':'Silicon',
        'title':'Blog1',
        'content':'first post',
        'date':'April 1'
    },
    {
        'author':'Alaska',
        'title':'Blog2',
        'content':'second post',
        'date':'April 2'
    }
]

@app.route("/", strict_slashes = False)
@app.route("/home", strict_slashes = False)
def home():
    '''my home route rendering the content of my home page'''
    return render_template("home.html", posts= posts)

@app.route("/about", strict_slashes = False)
def about():
    '''my about page route rendering content of the about page'''
    return render_template("about.html", title = "About")

@app.route("/register", strict_slashes = False, methods=['GET','POST'])
def register():
    '''this page render the registration page.'''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():# confirm if the form was valid after submission
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #the hashed password keeps your password coded incase of any attach of your database
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)#pushing into database
        db.session.add(user)
        db.session.commit()
        flash('Account has been created. You can now Login', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title = "Register", form = form)

@app.route("/login", strict_slashes = False, methods=['GET', 'POST'])
def login():
    '''gives access to the login page and allow user to login'''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            #flash(f'You have successfully logged In', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Enter the correct email and password', 'danger')
    return render_template("login.html", title = "Login", form = form)

@app.route("/logout", strict_slashes = False)
def logout():
    logout_user()
    return redirect(url_for('home'))
    
@app.route("/account", strict_slashes = False)
def account():
    return render_template("account.html", title = "Account")