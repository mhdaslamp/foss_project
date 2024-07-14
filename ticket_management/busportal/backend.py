# busportal/backends.py

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
import psycopg2
from django.conf import settings

class AdmNoAuthBackend(BaseBackend):
    def authenticate(self, request, adm_no=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            conn = psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT']
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM busapp_student WHERE adm_no=%s", (adm_no,))
            user = cursor.fetchone()

            if user:
                django_user, created = UserModel.objects.get_or_create(adm_no=adm_no)
                return django_user if django_user.check_password(password) else None
            else:
                print(f"No user found with adm_no: {adm_no}")

            conn.close()
        except Exception as e:
            print(f"Error connecting to database: {e}")

        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
