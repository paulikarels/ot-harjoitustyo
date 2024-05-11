from build import build
from datapack import *

def pytest_configure():
    build()
    create_users()
    create_courses()
    create_exercises()
    get_database_connection().commit()

