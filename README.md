# Diwan Ghimire's Portfolio Website

> ✅ **STATUS: COMPLETE & OPERATIONAL**  
> Your website is live at http://127.0.0.1:8000  
> Admin panel: http://127.0.0.1:8000/admin/ (diwan / password123)

A modern Django-based portfolio website showcasing projects and skills in AI, Data Analytics, and Backend Development.

## 🚀 QUICK START - READ THESE FIRST!

Your server is already running! Read these files:
1. **COMPLETION_REPORT.md** - Summary of what's complete & next steps
2. **QUICKSTART.md** - Quick reference guide
3. **SETUP_GUIDE.md** - Detailed setup documentation

## 📋 What To Do Now

1. **Add Projects** - Most important!
   - Go to http://127.0.0.1:8000/admin/
   - Login: `diwan` / `password123`
   - Click Projects → Add Project

2. **Upload Resume** - Make it downloadable
   - In admin: Resumes → Add Resume

3. **Test Everything** - Visit all pages and features

4. **Deploy** - When ready to go live

## Features

- **Home Page**: Hero section with featured projects
- **About Page**: Personal background and achievements
- **Skills Page**: 6 categories with progress bars
- **Portfolio Page**: Database-driven project showcase
- **Contact Page**: Interactive contact form with email
- **Resume Download**: CV download button
- **Admin Panel**: Easy content management
- **Responsive Design**: Mobile-friendly layout
- **Modern UI**: Dark theme with cyan accents

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- pip (Python package manager)

### 2. Installation Steps

#### Create Virtual Environment
```bash
cd myportfolio
python -m venv venv
venv\Scripts\activate  # On Windows
# or: source venv/bin/activate  # On macOS/Linux
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Configure Environment Variables
```bash
cp .env.example .env
# Edit .env and add your configuration:
# - SECRET_KEY (generate one using: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
# - EMAIL settings for contact form
```

#### Run Migrations
```bash
python manage.py migrate
```

#### Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 3. Running the Development Server
```bash
python manage.py runserver
```
Visit: http://localhost:8000

### 4. Email Configuration

**For Development (Console Output):**
Default console backend prints emails to console.

**For Production (Gmail SMTP):**
Update `.env` with:
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## File Structure

```
myportfolio/
├── home/                          # Main app
│   ├── static/
│   │   ├── css/style.css         # All styles
│   │   ├── js/script.js          # JavaScript
│   │   └── images/               # Images
│   ├── templates/
│   │   ├── index.html            # Home page
│   │   ├── about.html            # About page
│   │   └── contact.html          # Contact page
│   ├── views.py                  # View logic
│   ├── urls.py                   # URL routing
│   └── models.py
├── myportfolio/
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL config
│   └── wsgi.py                  # WSGI config
├── manage.py                    # Django CLI
├── requirements.txt             # Dependencies
└── .env                        # Environment variables (not in git)
```

## Security Features

✅ **Fixed Issues:**
- SECRET_KEY moved to environment variables
- DEBUG mode controlled via .env
- ALLOWED_HOSTS configured
- CSRF protection enabled
- Input validation on contact form
- Error handling for email functionality
- Static files properly configured

## Contact Form Features

- Name, email, subject, and message validation
- Email notifications
- Success/error messages
- CSRF protection
- Input sanitization

## Troubleshooting

### Issue: "No module named 'django'"
**Solution:** Activate virtual environment and run `pip install -r requirements.txt`

### Issue: "SECRET_KEY is invalid"
**Solution:** Generate new SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Then update in `.env`

### Issue: Static files not loading
**Solution:** Collect static files (for production):
```bash
python manage.py collectstatic
```

## Next Steps

- [ ] Add a Blog section with Django models
- [ ] Implement project portfolio models
- [ ] Add admin interface for managing projects
- [ ] Deploy to production (Heroku, PythonAnywhere, etc.)
- [ ] Add SSL certificate
- [ ] Set up database backups

## License

This project is open source and available under the MIT License.
