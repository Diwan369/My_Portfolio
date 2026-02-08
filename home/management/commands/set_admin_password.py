from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Set or update admin user password'

    def add_arguments(self, parser):
        parser.add_argument(
            '--password',
            type=str,
            default='Missionself@9192',
            help='Password for admin user (default: Missionself@9192)'
        )

    def handle(self, *args, **options):
        password = options['password']
        
        try:
            admin_user = User.objects.get(username='admin')
            admin_user.set_password(password)
            admin_user.save()
            self.stdout.write(
                self.style.SUCCESS('✅ Admin password updated successfully!')
            )
            self.stdout.write(f'   Username: admin')
            self.stdout.write(f'   Password: {password}')
        except User.DoesNotExist:
            # Create admin user if it doesn't exist
            User.objects.create_superuser('admin', 'admin@example.com', password)
            self.stdout.write(
                self.style.SUCCESS('✅ Admin user created successfully!')
            )
            self.stdout.write(f'   Username: admin')
            self.stdout.write(f'   Password: {password}')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error: {str(e)}')
            )
