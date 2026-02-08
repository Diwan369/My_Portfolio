# 🚀 Quick Start Guide

## Your Portfolio is LIVE! ✅

### Access Your Website Now

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8000/ | **Website Home** |
| http://127.0.0.1:8000/admin/ | **Admin Panel** |

---

## 🔐 Admin Login Credentials

```
Username: diwan
Password: password123
```

---

## 📝 First Steps (Do This NOW!)

### 1️⃣ Add Your First Project
```
1. Go to http://127.0.0.1:8000/admin/
2. Login with credentials above
3. Click "Projects" section
4. Click "Add Project" button
5. Fill in details:
   - Title: e.g., "AI Chat Bot"
   - Description: What it does
   - Technologies: Python, Django, TensorFlow
   - Upload an image
   - Add GitHub URL
   - Add Live URL (optional)
6. Click "Save"
```

### 2️⃣ Upload Your Resume
```
1. In admin, click "Resumes"
2. Click "Add Resume"
3. Upload your PDF file
4. Check "Is active" checkbox
5. Click "Save"
6. Users can download via CV button in navbar!
```

### 3️⃣ Customize Skills (Optional)
- Skills already configured with 6 categories
- You can modify them in Admin > Skills
- Edit proficiency ratings (0-100)

---

## 🎨 Website Pages

All pages are **database-driven** and update automatically:

- **Home** `/` - Hero section, featured projects, CTA buttons
- **About** `/about/` - Your bio and achievements
- **Skills** `/skills/` - 6 skill categories with progress bars
- **Portfolio** `/portfolio/` - All your projects
- **Contact** `/contact/` - Email form → sends to batukdiwan7@gmail.com

---

## 🛠️ Terminal Commands Reference

```powershell
# Start server
..\portfolio\Scripts\Activate.ps1
python manage.py runserver

# Access Django shell for custom commands
python manage.py shell

# Create backup of database
copy db.sqlite3 db.sqlite3.backup

# Reset everything (delete all data)
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📂 Important Files

| File | Purpose |
|------|---------|
| `db.sqlite3` | Your entire website database (BACKUP THIS!) |
| `home/models.py` | Database structure (Project, Resume, Skill) |
| `home/templates/` | All HTML pages |
| `home/static/css/style.css` | All styling |
| `.env` | Secret keys (⚠️ don't share!) |

---

## 🌐 Going Live Soon?

When ready to deploy to production:

1. Change `DEBUG=False` in settings
2. Generate new `SECRET_KEY`
3. Configure email settings
4. Switch to PostgreSQL database
5. Use cloud storage for media (AWS S3, Cloudinary)
6. Get SSL certificate
7. Point your domain name

See `DEPLOYMENT_READY.md` for full details.

---

## ⚡ Pro Tips

✨ **CSS Customization**
- Edit colors in `home/static/css/style.css`
- Change theme with CSS variables at top of file

✨ **Add New Page**
- Create `.html` template in `home/templates/`
- Add view function in `home/views.py`
- Add URL route in `home/urls.py`
- Update navbar in `base.html`

✨ **Database Backup**
- Copy `db.sqlite3` regularly!
- This file contains all your projects

---

## 🆘 Troubleshooting

**Server not starting?**
- Make sure virtual environment is activated
- Check port 8000 isn't in use: `netstat -ano | findstr :8000`

**Admin login not working?**
- Clear browser cache
- Check credentials: username=`diwan`, password=`password123`

**Database corrupted?**
- Delete `db.sqlite3`
- Run `python manage.py migrate`
- Recreate superuser: `python manage.py createsuperuser`

**Pages not showing?**
- Check server is running
- Clear browser cache (Ctrl+Shift+Delete)
- Check Django error in terminal

---

## 📞 Contact Settings

Contact form sends emails to: **batukdiwan7@gmail.com**

To change:
- Edit `home/views.py` → `contact()` function → `DEFAULT_FROM_EMAIL`

---

## ✍️ Next: Content Management

### Add 3-5  Projects NOW!
This fills your portfolio and impresses visitors.

### Upload Your Resume PDF
Make it downloadable from CV button.

### Share with Friends!
Send them: http://127.0.0.1:8000
(on same network) or deploy to get real URL.

---

**Your portfolio is ready to shine! 🌟**

Questions? Check `SETUP_GUIDE.md` or `DEPLOYMENT_READY.md`

---
*Last updated: 2025*
*Status: ✅ Live and Running*
