from flask import render_template, url_for, flash, redirect, request #request is a query parameter
from lets_post import app, db, bcrypt 
from lets_post.form import RegistrationForm, LoginForm, UpdateAccountForm #for forms
from lets_post.models import User, Post #for database settings
from flask_login import login_user, current_user, logout_user, login_required
#loggin user,check if the current user is logged in,logout user, allow user access a page only when loggedin



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
            next_page = request.args.get('next')
            flash(f'You have successfully logged In', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))    
        else:
            flash(f'Enter the correct email and password', 'danger')
    return render_template("login.html", title = "Login", form = form)

@app.route("/logout", strict_slashes = False)
def logout():
    logout_user()
    return redirect(url_for('home'))
    
@app.route("/account", strict_slashes = False, methods =['GET','POST'])
@login_required #this decorator shows that we need to login to access this route. we also need to show it where the login is located
def account():
    '''returns the account detail of individual user'''
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data =  current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pic/' + current_user.image_file)
    return render_template("account.html", title = "Account", image_file = image_file, form = form)