# 🚀 Deployment & GitHub Guide

## Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `myportfolio`
3. **DO NOT** initialize with README (you already have one)
4. Click "Create repository"

## Step 2: Push to GitHub
After creating the repository, you'll see instructions. Run these commands in PowerShell:

```powershell
cd "c:\Users\Diwan\Desktop\Diwan\Programming\Python\Internship\My portfolio\myportfolio"
git branch -M main
git remote add origin https://github.com/Diwan369/myportfolio.git
git push -u origin main
```

## Step 3: Deploy to Render

### 3a. Set Up Render
1. Go to https://render.com
2. Sign up with GitHub account
3. Click "New +" → "Web Service"
4. Connect your GitHub repository `myportfolio`
5. Fill in these settings:

| Setting | Value |
|---------|-------|
| Name | myportfolio |
| Environment | Python 3 |
| Build Command | `bash build.sh` |
| Start Command | `gunicorn myportfolio.wsgi` |
| Branch | main |

### 3b. Add Environment Variables in Render Dashboard
In Render → myportfolio → Environment:

```
SECRET_KEY=<generate from https://djecrety.ir/>
DEBUG=False
ALLOWED_HOSTS=yourdomain.onrender.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.onrender.com
EMAIL_HOST_USER=batukdiwan7@gmail.com
EMAIL_HOST_PASSWORD=<your gmail app password>
```

### 3c. Create Superuser on Render
After deployment, run in Render Shell:
```
python manage.py createsuperuser
```

## Your Live Site
Once deployed:
- **Website:** `https://myportfolio-xxxx.onrender.com/`
- **Admin Panel:** `https://myportfolio-xxxx.onrender.com/admin/`

---

## 📝 Important Notes
- ✅ `.gitignore` excludes `.env`, `db.sqlite3`, and sensitive files
- ✅ Settings are configured to use environment variables
- ✅ WhiteNoise handles static files
- ✅ All security headers are enabled for production
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --no-input