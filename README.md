                                Letspost

Letspost is a platform designed to help users build and maintain strong writing habits. By providing room for a user to post, update or delete post and also allow user to view other people's post.

Features

User Authentication: Secure login and registration system.
Post Management: Create, update, and delete your posts easily.
Community Interaction

Prerequisites

Python 3.8+
Flask
SQLAlchemy
Flask-WTF
Flask-Login
Flask-Mail
Flask-Migrate
itsdangerous
Installation

1. Clone the repository:
    git clone https://github.com/Silicon50/Letspost.git

2. Move into Letspost directory
    cd Letspost

3. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Linus

4. Install the requirement.txt file
    pip install -r requirements.txt

5. Set environment variables for email configuration and secret key: # this can be skipped
    export MAIL_USERNAME='your-email@example.com'
    export MAIL_PASSWORD='your-email-password'

6. Run u application
    python3 run.py
    Open your browser and navigate to http://127.0.0.1:5000


Usage

User Registration
Register a new account by providing a username, email, and password.
Verify your email address using the confirmation link sent to your email.
Creating Posts
Log in to your account.
Navigate to the "Create Post" section.
Enter your post title and content, then submit.
Updating and Deleting Posts
Log in to your account.
Navigate to "My Posts" to view your existing posts.
Select a post to edit or delete.
Password Reset
Click on "Forgot Password" on the login page.
Enter your registered email to receive a password reset link.
Follow the instructions in the email to reset your password.

Contributing
We welcome contributions to improve Letspost! To contribute, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.



Acknowledgments
Thanks to ALx and Flask community for providing excellent resources and support.
