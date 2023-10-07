# BlogAppBack-End

This is the back-end component of the BlogApp project, which provides a platform for creating and managing blog posts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Introduction

The BlogAppBack-End is built using Django and the Django REST framework. It serves as the back-end for a blog application, providing APIs for creating, retrieving, and managing blog posts, categories, and topics.

## Features

- Create and manage blog posts with titles, content, and topics.
- Assign blog posts to categories.
- View popular and new blog posts.
- Increment view counts when a user reads a blog post.
- API endpoints for accessing blog data.

## Requirements

To run this application, you need the following:

- Python (3.6 or higher)
- Django (3.0 or higher)
- Django REST framework (3.0 or higher)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sabakhupenia/BlogAppBack-End.git
   cd BlogAppBack-End
2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
3. Install the required packages:

```
pip install -r requirements.txt
```
4. Run migrations:

```
python manage.py migrate
```
5. Create a superuser for admin access:

```
python manage.py createsuperuser
```
6. Start the development server:
```
python manage.py runserver
```
## Usage


1. Access the admin interface by visiting http://localhost:8000/admin/. Log in with
   the superuser credentials created earlier to manage blog posts, categories, and topics.

2. Use the provided API endpoints to interact with the blog data.

## API Endpoints


/api/popular-blogs/: Get popular blog posts.
/api/new-blogs/: Get new blog posts.
/api/blog-posts/: List and create blog posts.
/api/blog-posts/{id}/: Retrieve, update, or delete a specific blog post.
