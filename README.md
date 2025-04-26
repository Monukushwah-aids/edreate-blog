# Edreate Blog - Project README

## Project Overview
Edreate Blog is a Django-based blogging platform where users can read, write, and share blog posts on various topics. The website is designed to empower voices and build a creative community.

---

## Prerequisites
- **Python** (version 3.10 or above)
- **pip** (Python package manager)
- **Virtual Environment** (recommended)

---

## Installation Steps

1. **Clone or Download the Project**
   - Download the project files to your computer.

2. **Set Up a Virtual Environment**
   - Open a terminal in the project folder.
   - Run: `python -m venv env`
   - Activate it:
     - On Windows: `env\Scripts\activate`

3. **Install Django**
   - Run: `pip install django`

4. **Other Installations**
   - No extra packages are required unless you add more features.

5. **Apply Migrations**
   - Run: `python manage.py migrate`

6. **Create a Superuser (for admin access)**
   - Run: `python manage.py createsuperuser`
   - Follow the prompts to set username and password.

7. **Run the Development Server**
   - Run: `python manage.py runserver`
   - Open your browser and go to `http://127.0.0.1:8000/`

---

## Project Structure
- `manage.py` - Django project management script
- `iblogs/` - Main project settings and configuration
- `blog/` - Main app containing models, views, forms, URLs, etc.
- `template/` - HTML templates for the website
- `media/` - Uploaded images and files
- `static/` - CSS, JS, and images for styling
- `db.sqlite3` - SQLite database file
- `env/` - Virtual environment (not needed for deployment)

---

## Main Features & Pages
- **Home Page**: Lists blog posts
- **About Page**: Info about the blog and its vision
- **Signup/Login**: User registration and authentication
- **Add Post**: Create new blog posts (after login)
- **Update/Delete Post**: Edit or remove your posts only that user we are create post
- **Categories**: Browse posts by category
- **Admin Panel**: Manage users and posts (for superuser)

---

## Notes
- All static files (CSS, JS, images) are in the `static/` folder.
- Uploaded images are stored in the `media/` folder.
- Templates are in the `template/` folder.
- The project uses Django’s built-in authentication system.

---

## How to Contribute
1. Fork the repository
2. Make your changes
3. Submit a pull request

---

## Contact
For questions or suggestions, please open an issue or contact the project maintainer.
