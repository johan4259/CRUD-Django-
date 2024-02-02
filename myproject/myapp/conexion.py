from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import connection
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/postgres")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_database_session():
    try:
        return Session()
    except Exception as e:
        print(f"Error creating database session: {e}")
        return None

def list_clients():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, first_name, last_name, email FROM myapp_client")
        rows = cursor.fetchall()
    clients = [
        {"id": row[0], "first_name": row[1], "last_name": row[2], "email": row[3]}
        for row in rows
    ]
    return clients
        
def create_client(first_name, last_name, email):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO myapp_client (first_name, last_name, email) VALUES (%s, %s, %s)",
            [first_name, last_name, email]
        )

class ClientListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        clients = list_clients()
        return Response({"clients": clients})
