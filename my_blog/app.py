from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure image upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    code_snippet = db.Column(db.Text, nullable=True)  # Optional field for code snippets
    image_filename = db.Column(db.String(100), nullable=True)  # Optional field for uploaded image
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for posts

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all blog posts
@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.timestamp.desc()).all()  # Retrieve posts ordered by timestamp
    return render_template('index.html', posts=posts)

# Route to create a new blog post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        code_snippet = request.form.get('code_snippet', None)
        image_file = request.files.get('image_file')

        # Save uploaded image if provided
        image_filename = None
        if image_file and image_file.filename != '':
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            image_file.save(image_path)

        # Create a new blog post
        new_post = BlogPost(
            title=title,
            content=content,
            code_snippet=code_snippet,
            image_filename=image_filename
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_post.html')

# Route to delete a blog post
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.image_filename:  # Delete the associated image file if it exists
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], post.image_filename)
        if os.path.exists(image_path):
            os.remove(image_path)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
