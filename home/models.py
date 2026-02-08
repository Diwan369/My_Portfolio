from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    """Model for storing portfolio projects"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated tech stack")
    image = models.ImageField(upload_to='projects/%Y/%m/', null=True, blank=True)
    github_url = models.URLField(null=True, blank=True, help_text="Link to GitHub repository")
    live_url = models.URLField(null=True, blank=True, help_text="Link to live demo")
    featured = models.BooleanField(default=False, help_text="Display as featured project")
    order = models.IntegerField(default=0, help_text="Display order (lower appears first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Resume(models.Model):
    """Model for storing resume/CV"""
    title = models.CharField(max_length=200, default="Resume")
    file = models.FileField(upload_to='documents/resume/')
    is_active = models.BooleanField(default=True, help_text="Whether this resume is currently available for download")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

    def __str__(self):
        return f"{self.title} - {self.updated_at.strftime('%Y-%m-%d')}"


class Skill(models.Model):
    """Model for organizing skills"""
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('web', 'Web & Backend Development'),
        ('data', 'Data Science & Libraries'),
        ('tools', 'Tools & Development Environment'),
        ('design', 'Design & Graphics'),
        ('office', 'Office Productivity'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="Proficiency level 0-100")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class About(models.Model):
    """Model for About page content - profile image, about text, and education"""
    title = models.CharField(max_length=200, default="About Me")
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True, help_text="Profile picture for about page")
    about_content = models.TextField(help_text="About me section (supports HTML)")
    education_content = models.TextField(help_text="Education & achievements section (supports HTML)")
    is_active = models.BooleanField(default=True, help_text="Whether this about section is displayed on the website")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'

    def __str__(self):
        return self.title
