from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.utils.safestring import mark_safe
import logging
import os

from .models import Project, Resume, Skill, About

logger = logging.getLogger(__name__)


def home(request):
    """Home page with featured projects"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    resume = Resume.objects.filter(is_active=True).first()
    
    context = {
        'featured_projects': featured_projects,
        'resume': resume,
    }
    return render(request, 'index.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact form handler with email notification"""
    success = False
    error = None
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Validation
        if not name or not email or not message:
            error = 'Please fill in all required fields.'
        elif '@' not in email:
            error = 'Please enter a valid email address.'
        elif len(message) < 10:
            error = 'Message must be at least 10 characters long.'
        else:
            try:
                # Send email to portfolio owner
                email_subject = f'Email from portfolio: {subject}' if subject else 'Email from portfolio: No subject provided'
                email_message = f'''
New Message from Portfolio Contact Form

From: {name}
Email: {email}
Subject: {subject or "No subject provided"}

Message:
{message}
                '''
                
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@diwanghimire.com',
                    recipient_list=['batukdiwan7@gmail.com'],
                    fail_silently=False,
                )
                success = True
                
                # Log successful submission
                logger.info(f'Contact form submitted by {name} ({email})')
                
            except Exception as e:
                logger.error(f'Email error: {str(e)}')
                error = 'Failed to send message. Please try again later.'

    return render(request, 'contact.html', {'success': success, 'error': error})


def about(request):
    """About page with profile image and about content from database"""
    about_data = About.objects.filter(is_active=True).first()
    resume = Resume.objects.filter(is_active=True).first()
    
    context = {
        'about': about_data,
        'resume': resume,
    }
    return render(request, 'about.html', context)


def portfolio(request):
    """Portfolio page with all projects"""
    all_projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    
    context = {
        'projects': all_projects,
        'featured_projects': featured_projects,
    }
    return render(request, 'portfolio.html', context)


def skills(request):
    """Skills page with organized skill categories"""
    skills = Skill.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'skills': skills,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'skills.html', context)


def download_resume(request):
    """Download resume from database"""
    try:
        resume = Resume.objects.filter(is_active=True).first()
        
        if not resume or not resume.file:
            return HttpResponseNotFound('Resume not found')
        
        # Get file path
        file_path = resume.file.path
        
        if not os.path.exists(file_path):
            return HttpResponseNotFound('Resume file not found')
        
        # Log download
        logger.info(f'Resume downloaded by {request.META.get("REMOTE_ADDR")}')
        
        # Return file as download
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="Diwan_Ghimire_Resume.pdf"'
        return response
        
    except Exception as e:
        logger.error(f'Resume download error: {str(e)}')
        return HttpResponseNotFound('Error downloading resume')
