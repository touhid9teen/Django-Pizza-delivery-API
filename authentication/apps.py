from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

'''
git rm -r --cached venv/
git rm -r --cached .env
git rm -r --cached db.sqlite3
git rm -r --cached static/
git rm -r --cached media/

'''