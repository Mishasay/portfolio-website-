#  Personal Portfolio Website

A personal portfolio website built with **Python and Django** to showcase my skills, projects, and background as an aspiring software developer.

🌐 **Live Website:** [portfolio-website-nzrc.onrender.com](https://portfolio-website-nzrc.onrender.com)

---

##  About

This is my personal portfolio website, designed and developed from scratch using **Python and Django**.

The website introduces me, showcases my technical skills, and provides visitors with an easy way to get in touch with me.

I created this project to gain practical experience with Django, improve my programming skills, and build a real project that I can use as part of my developer portfolio.

---

##  Features

*  Home page
*  About Me page
*  Skills page
*  Contact form
*  Email notifications via Brevo
*  Social media links
*  Responsive design
*  CSRF protection
*  Custom HTML & CSS design

---

##  Tech Stack

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **SQLite**
* **Brevo**
* **Git**
* **GitHub**

---

##  Project Structure

```text
webnew/
│
├── main/
│   ├── templates/
│   │   └── main/
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── skills.html
│   │       ├── contact.html
│   │       └── layout.html
│   │
│   ├── static/
│   ├── urls.py
│   └── views.py
│
├── webnew/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── static/
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## Contact Form

The website includes a contact form that allows visitors to send me a message directly.

The form collects:

- **Name**
- **Email**
- **Subject**
- **Message**

Messages are delivered to my email using Django and the Brevo email service.

The sender's email address is included in the message, making it easy to identify and respond to visitors.

---

##  Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Mishasay/portfolio-website.git
cd portfolio-website
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the website in your browser:

```text
http://127.0.0.1:8000/
```

---

##  Environment Variables

Sensitive information such as Django's secret key and email service credentials should not be stored directly in the source code.

For production, these values should be stored as environment variables.

The `.env` file is excluded from Git using `.gitignore`.

---

##  Screenshots

### Home

<img width="1918" height="945" alt="image" src="https://github.com/user-attachments/assets/d2725cd7-d079-4386-8c6f-0fc22d58a7d5" />

### About

<img width="1903" height="946" alt="image" src="https://github.com/user-attachments/assets/2a0bb72e-6b44-4669-af8e-8673a210ccdd" />

### Skills

<img width="1905" height="954" alt="image" src="https://github.com/user-attachments/assets/cf9a5082-7bce-4f5e-bfe1-c17824e0380f" />

### Contact

<img width="1903" height="952" alt="image" src="https://github.com/user-attachments/assets/6abc4734-bf96-4145-9e15-c86e8ffa1c21" />

---

##  What I Learned

Building this project allowed me to gain practical experience with:

* Creating a Django project from scratch
* Working with Django URL routing
* Creating and organizing templates
* Working with static files
* Handling POST requests
* Building a contact form
* Integrating email delivery using Brevo
* Organizing a real-world project structure
* Using Git and GitHub
* Deploying a Django application

---

## 👤 Author

**Mykhailo**

Aspiring software developer passionate about programming, problem-solving, and continuously improving my skills through personal projects and learning new technologies.

### Connect with me

* **GitHub:** https://github.com/Mishasay
* **Instagram:** https://www.instagram.com/smertvnishite/
* **Telegram:** https://t.me/akus4yan
* **Email:** [mykhailosharov@gmail.com](mailto:mykhailosharov@gmail.com)

---

##  License

This project was created as a personal portfolio project.
