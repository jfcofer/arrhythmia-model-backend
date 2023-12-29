# run.py

import sys

print(sys.path)

from dotenv import load_dotenv

print("Importing app module...")
from app import create_app, socketio

print("Import successful.")

# Load environment variables from .env file
load_dotenv()


app = create_app()

if __name__ == "__main__":
    socketio.run(app)
