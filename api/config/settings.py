import os
from dotenv import load_dotenv

# Automatically finds the .env file in the root or parent directories
load_dotenv()

class Settings:
    def __init__(self):
        # Use .get() to provide defaults if the variable is missing
        self.HOST_URL = os.getenv("HOST_URL", "0.0.0.0")
        self.HOST_PORT = int(os.getenv("HOST_PORT", 8000))
        self.DATABASE_URL = os.getenv("DATABASE_URL")

        # Basic check to ensure required values exist
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL is not set in the environment!")

# Create a single instance to use throughout your app
conf = Settings()
