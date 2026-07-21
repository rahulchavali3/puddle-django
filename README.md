# 🛍️ Puddle

### A modern local marketplace built with Django

Puddle is a full-stack marketplace web application that allows users to discover, search, and list items within their local community.

The goal of Puddle is to create a simple and intuitive platform where people can find items they need and sell things they no longer use.
<p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" /> <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" /> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" /> </p>
---

## ✨ Features

* 🔐 User authentication with signup and login
* 🛍️ Create and list items for sale
* 🖼️ Upload product images
* 🔍 Search for items
* 🗂️ Browse items by category
* 📄 View detailed item pages
* ✏️ Edit your own listings
* 🗑️ Delete your own listings
* 💬 User-to-user conversations
* 📥 Inbox for conversations
* 🏷️ Mark items as sold
* 📱 Responsive user interface
* 🎨 Clean and modern UI built with Tailwind CSS

---

## 🖥️ Screenshots

### Home Page

<img width="1900" height="875" alt="image" src="https://github.com/user-attachments/assets/65f1975c-3683-4ef1-baf8-9ab3707b5c43" />

![Home Page](screenshots/home.png)

### Browse Items

<img width="1887" height="870" alt="image" src="https://github.com/user-attachments/assets/1d6a4bb1-d848-487a-92af-b61e188d66c1" />

![Browse Items](screenshots/browse.png)

### Item Details

<img width="1896" height="900" alt="image" src="https://github.com/user-attachments/assets/3d0fc057-9a9c-4d4e-8b34-22cf0c2624ce" />

![Item Details](screenshots/item-details.png)

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Django**
* **Django ORM**
* **SQLite**

### Frontend

* **HTML5**
* **Tailwind CSS**
* **JavaScript**

### Tools

* **Git**
* **GitHub**
* **Visual Studio Code**

---

## 📂 Project Structure

```text
PuddleDjango/
│
├── puddle/
│   │
│   ├── manage.py
│   │
│   ├── core/
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── item/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── conversation/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   └── puddle/
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/puddle-django.git
```

Navigate into the project:

```bash
cd puddle-django
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Navigate to the Django project

```bash
cd puddle
```

---

### 5. Apply database migrations

```bash
python manage.py migrate
```

---

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

---

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

Puddle uses Django's built-in authentication system to provide:

* User registration
* Login and logout
* Protected user functionality
* User-specific item management
* Ownership-based edit and delete permissions

Users can only manage the listings that they own.

---

## 🏗️ How It Works

The application is organized into multiple Django applications, each responsible for a specific part of the platform.

### Core

Handles:

* Home page
* General website pages
* Navigation
* Authentication-related pages

### Item

Handles:

* Item creation
* Item editing
* Item deletion
* Item browsing
* Search
* Categories
* Item details

### Conversation

Handles:

* Starting conversations
* Sending messages
* User inbox
* Communication between buyers and sellers

---

## 🧠 What I Learned

Building Puddle helped me gain practical experience with:

* Building a full-stack application using Django
* Django models and relationships
* Django ModelForms
* User authentication
* Handling file uploads
* Django templates and template inheritance
* URL routing
* CRUD operations
* Querying data using the Django ORM
* Search and filtering
* User permissions and ownership
* Database migrations
* Building responsive interfaces with Tailwind CSS
* Git and GitHub workflow

---

## 🔮 Future Improvements

Some features planned for future versions include:

* 💳 Online payments
* ⭐ Seller ratings and reviews
* 🔔 Notifications
* ❤️ Wishlist and saved items
* 📍 Location-based item discovery
* 🧠 AI-powered item recommendations
* 🔎 Advanced filtering
* 📸 Multiple images per listing
* ☁️ Cloud image storage
* 🚀 Production deployment

---

## 📌 Project Status

🚧 **Actively under development**

Puddle is currently being developed and improved with new features and refinements.

---

## 👨‍💻 Author

### Rahul Chavali

B.Tech Information Technology graduate and aspiring Java Full Stack Developer passionate about building practical web applications and learning modern software development technologies.

---

## ⭐ Support

If you find this project interesting, consider giving it a ⭐ on GitHub!

---

<p align="center">
  Built with ❤️ using Django
</p>
