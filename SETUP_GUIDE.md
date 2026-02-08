# Portfolio Setup & Admin Guide

## 📋 Overview
Your portfolio is now fully database-integrated with the following features:
- ✅ Project Management (Add/Edit/Delete projects)
- ✅ Resume Upload & Download
- ✅ Skill Management
- ✅ Contact Form with Email Notifications
- ✅ Admin Panel for Managing Everything

---

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 4. Start Development Server
```bash
python manage.py runserver
```

Your site will be at: `http://127.0.0.1:8000/`
Admin panel at: `http://127.0.0.1:8000/admin/`

---

## 🎯 How to Use the Admin Panel

### Access Admin
1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials

### Add/Edit Projects
1. Click "Projects" in the admin panel
2. Click "Add Project" button
3. Fill in the form:
   - **Title**: Project name (e.g., "AI Prediction Model")
   - **Description**: Detailed project description
   - **Technologies**: Comma-separated (e.g., "Python, NumPy, Pandas, Machine Learning")
   - **Image**: Upload project screenshot/image
   - **GitHub URL**: Link to your GitHub repo
   - **Live URL**: Link to live demo (if available)
   - **Featured**: Check to highlight on home page
   - **Order**: Number for display order (lower = appears first)
4. Click "Save"

**Example:**
```
Title: AI Student Performance Analyzer
Description: Built an ML model to predict student performance...
Technologies: Python, Scikit-learn, Pandas, Flask
Featured: ✓ (checked)
Order: 1
```

### Upload Resume
1. Click "Resumes" in admin panel
2. Click "Add Resume"
3. Upload your PDF file
4. Toggle "Is Active" to make it downloadable
5. Save

**Note:** Only the active resume will be available for download

### Manage Skills
1. Click "Skills" in admin panel
2. Add/Edit individual skills
3. Select category (Programming Language, Tools, etc.)
4. Set proficiency level (0-100)
5. Set display order

**Categories:**
- Programming Languages (Python, C, C++, HTML, CSS)
- Web & Backend Development (Django, SQL, OOP)
- Data Science & Libraries (NumPy, Pandas, Tkinter)
- Tools & Development Environment (VS Code, GitHub)
- Design & Graphics (Photoshop)
- Office Productivity (Excel, Word, PowerPoint)

---

## 🔗 URL Endpoints

### Public Pages
- Home: `/` 
- About: `/about/`
- Skills: `/skills/`
- Portfolio: `/portfolio/`
- Contact: `/contact/`
- Download Resume: `/download-resume/`

### Admin
- Admin Panel: `/admin/`
- Projects: `/admin/home/project/`
- Resumes: `/admin/home/resume/`
- Skills: `/admin/home/skill/`

---

## 📱 Features by Page

### Home (`/`)
- Displays featured projects (marked as Featured in admin)
- Download CV button in navbar
- Hero section with your info
- Social links (Facebook, Twitter, LinkedIn)

### Portfolio (`/portfolio/`)
- Displays ALL projects from database
- Shows project image, title, tech stack
- Links to GitHub & Live demo
- Empty state if no projects added

### Skills (`/skills/`)
- Organized by category
- Shows proficiency bars
- Dynamically pulls from Skills model

### About (`/about/`)
- Static content (hardcoded in template)
- Link to your Ambition Guru blog
- References resume if available

### Contact (`/contact/`)
- Contact form sends email to: `batukdiwan7@gmail.com`
- Requires: Name, Email, Message
- Optional: Subject field

---

## 📧 Email Configuration

### Console Output (Default - for development)
Emails print to console. Good for testing.

### Gmail Configuration (Production)
1. Update `.env` file:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

**Get App Password:**
1. Enable 2FA on Gmail
2. Go to: https://myaccount.google.com/apppasswords
3. Use the 16-character password

---

## 🗂️ Project Structure
```
myportfolio/
├── home/
│   ├── models.py          # Database models (Project, Resume, Skill)
│   ├── views.py           # View logic & resume download
│   ├── admin.py           # Admin panel configuration
│   ├── urls.py            # URL routes
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, images
├── media/                 # User uploads (projects, resumes)
├── logs/                  # Application logs
├── manage.py              
├── requirements.txt       # Python dependencies
├── db.sqlite3            # Database
└── myportfolio/
    ├── settings.py       # Django settings (configured for media)
    └── urls.py           # Main URL configuration
```

---

## 🎨 Customization

### Change Colors
Edit `home/static/css/style.css`:
```css
:root {
    --primary-color: #00d4ff;      /* Cyan */
    --secondary-color: #1a1a2e;    /* Dark */
    --dark-bg: #0f0f1e;            /* Darker background */
    --text-light: #e0e0e0;         /* Light text */
    --text-gray: #a0a0a0;          /* Gray text */
}
```

### Modify About/About Page Content
Edit `home/templates/about.html` - HTML content is hardcoded

### Update Social Links
Edit `home/templates/base.html` footer section and `index.html` social icons

---

## 📝 Database Models

### Project Model
- Title (unique)
- Slug (auto-generated from title)
- Description (rich text)
- Technologies (comma-separated)
- Image (optional)
- GitHub URL (optional)
- Live URL (optional)
- Featured (boolean - shows on home)
- Order (display order)
- Created/Updated timestamps

### Resume Model
- Title (default: "Resume")
- File (PDF/DOC upload)
- Is Active (boolean - enables download)
- Uploaded/Updated timestamps

### Skill Model
- Name
- Category (choice field)
- Proficiency (0-100)
- Order (display order)

---

## 🔒 Security Notes

- Keep SECRET_KEY safe (in .env)
- Never commit .env to Git
- Change DEBUG=False for production
- Use environment variables for sensitive data
- Create strong superuser password

---

## 🐛 Troubleshooting

### Resume Download Not Working
- Check file exists in `media/documents/resume/`
- Verify "Is Active" is checked in admin
- Check file permissions

### Images Not Showing
- Ensure file is in `media/projects/`
- Check file path in database
- Run server with `python manage.py runserver`

### Emails Not Sending
- Check EMAIL_BACKEND setting
- Verify email credentials in .env
- Check Gmail app password is correct
- Review logs in `logs/portfolio.log`

### Admin Panel Not Loading
- Run migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Check DEBUG=True in settings

---

## 📞 Contact & Support

For questions about your portfolio:
- Email: batukdiwan7@gmail.com
- LinkedIn: https://t.co/gwtUQFD2aV
- Website: http://127.0.0.1:8000/ (local dev)

---

**Last Updated:** February 6, 2026
**Django Version:** 6.0.2
**Python Version:** 3.8+
