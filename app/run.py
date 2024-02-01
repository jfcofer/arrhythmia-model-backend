# run.py

from dotenv import load_dotenv
from app import create_app, socketio

# Load environment variables from .env file
load_dotenv()

app = create_app()

if __name__ == "__main__":
    socketio.run(app)
