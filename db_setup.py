# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def init_db(app):
#     db.init_app(app)
#     # Create all tables (if they don't exist)
#     with app.app_context():
#         db.create_all()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(100))
#     last_name = db.Column(db.String(100))
#     email = db.Column(db.String(120), unique=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(200))  # Hashed password
#     linkedin = db.Column(db.String(255))


import psycopg2

# Database connection settings
DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

def create_users_table():
    """Create the users table if it doesn't exist."""
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        username VARCHAR(50) UNIQUE NOT NULL,
        password TEXT NOT NULL,
        linkedin TEXT
    );
    """)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_users_table()
    print("Users table created successfully.")