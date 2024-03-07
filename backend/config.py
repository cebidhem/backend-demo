"""This config hold database connection details."""
import os

POSTGRES = {
    'user': os.environ.get('DB_USER', 'postgres'),
    'pw': os.environ.get('DB_PASS', 'mytestdb123'),
    'db': os.environ.get('DB_NAME', 'py-demo'),
    'host': os.environ.get('DB_ADDRESS', '127.0.0.1'),
    'port': os.environ.get('DB_PORT', '5432'),
}