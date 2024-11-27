# Flask Blog Application

This is a simple **Flask-based blog application** that allows users to create, view, update, and delete blog posts. The application also supports uploading and previewing images, displaying code snippets with syntax highlighting, and copying code snippets to the clipboard.

---

## Features  
- Create new blog posts with a title, content, code snippet, and image.  
- Display all blog posts on the home page with timestamps.  
- Live preview of uploaded images.  
- Code snippets are syntax-highlighted using **Prism.js** and can be copied to the clipboard.  
- Responsive design using **Bootstrap 5**.  
- Image uploads and static storage handling.  

---

## Technologies Used  
- **Python** (Flask framework)  
- **HTML5**, **CSS3**, **JavaScript**  
- **Bootstrap 5** for styling and layout  
- **Prism.js** for syntax highlighting of code snippets  
- **SQLite** for database management  

---

## Setup Instructions

### Prerequisites
- Python 3.x  
- Flask  
- Flask-SQLAlchemy  

### Installation Steps  

1. **Clone the repository**  
   ```bash  
   https://github.com/HarshVardhanLabs/Blog-post.git
   cd flask-blog

### File Descriptions
- **app.py**: Main Flask application file.
- **my_database.db**: SQLite database file (automatically created).
- **static/uploads/**: Directory for storing uploaded images.
- **templates/index.html**: Home page template for displaying posts.
- **templates/new_post.html**: Form for creating new posts.
- **README.md**: Documentation file for the project.

## Usage
1. Go to the homepage (`http://127.0.0.1:5000/`).
2. Click on **"Create New Post"** to add a new blog post.
3. Fill in the title, content, code snippet, and upload an image.
4. Click **Submit** to create the post.
5. View all posts on the homepage. Posts can be deleted using the **Delete** button.

## Contributions
Contributions are welcome! Fork this repository and submit a pull request with your improvements.

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Prism.js](https://prismjs.com/)

   
