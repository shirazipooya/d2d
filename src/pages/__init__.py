import os
from dotenv import load_dotenv

load_dotenv(".env")

HOME_PAGE_URL = os.getenv("HOME_PAGE_URL")
DOWNLOAD_PAGE_URL = os.getenv("DOWNLOAD_PAGE_URL")
