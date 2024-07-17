
College Bus Auto-Ticketing App

A system to manage bus ticketing for college students using face recognition technology. The project includes three main modules: capturing student data, detecting faces, developed using OpenCV, Python, and SQL.
This project automates bus ticket management for college students using face recognition, providing a secure, efficient, and user-friendly system for capturing, detecting, and managing student data and payments

Advantages of E-Tickets

- Convenience: No need for physical tickets; use face recognition.
- Security: Reduces ticket fraud and misuse.
- Efficiency: Speeds up the boarding process.
- Cost-Effective: Saves on printing and distributing tickets.
- Eco-Friendly: Reduces paper waste.


# System Requirements

- Python 3.x
- OpenCV
- Postgres Sql


Technologies Used

- OpenCV: For face detection and recognition.
- Python: Backend logic and scripts.
- SQL: For storing and managing students and payment data.

# Modules

- adding_faces.py: Captures student faces and collects data.
- test.py: Detects and recognizes student faces.and takes ticket and return their balance amount in the wallet

how to run this program?




download and install python
https://www.python.org/downloads/

download and install PostgreSQL
https://www.postgresql.org/download/



install OpenCV
pip install opencv-python


for connecting PostgreSQL database install 'psycopg2'

pip install psycopg2-binary


As this project uses PostgreSQL database you need to set up the Data base in the code 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ticket',
        'USER': 'foss project',
        'PASSWORD': 'foss123',
        'HOST': '192.168.1.10',  
        'PORT': '5432',
    }
}



