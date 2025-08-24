# Blog Project using Google Blogger API

## Project Overview

This project is a Django-based web application that serves as a modern blogging platform. It integrates with the Google Blogger API to fetch, display, and manage blog posts, providing a seamless and visually appealing experience for users.

## Features

- Responsive homepage displaying a list of blog articles
- Individual article detail pages with clean design
- Integration with Google Blogger API for fetching blog data
- Modern UI with custom CSS for a professional look

## Technologies Used

- Python 3
- Django Web Framework
- Google Blogger API
- HTML5 & CSS3 (custom responsive design)

## Google Blogger API

The project uses the Google Blogger API to:

- Fetch blog posts and their details
- Display content dynamically on the site

You need to set up API credentials from the Google Cloud Console and configure them in your Django project settings or environment variables.

## How to Run the Project

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd <project-folder>
   ```
2. **Create a virtual environment and activate it**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Set up Google Blogger API credentials**

   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project and enable the Blogger API
   - Create OAuth 2.0 credentials and download the JSON file
   - Add your credentials/configuration to your Django settings or as environment variables

5. **Apply migrations**
   ```
   python manage.py migrate
   ```
6. **Run the development server**
   ```
   python manage.py runserver
   ```
7. **Open your browser and visit**
   ```
   http://127.0.0.1:8000/
   ```

## What We Use

- **Django** for backend and routing
- **Google Blogger API** for blog data
- **HTML/CSS** for frontend
- **SQLite** as the default database (can be changed)

---

## the results shown in Output file

For any issues or contributions, please open an issue or submit a pull request.
