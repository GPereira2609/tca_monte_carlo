import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

CONFIG_PATH = os.path.join(BASE_DIR, "config/config.yaml")


with open(CONFIG_PATH, "r") as f:
    _config = yaml.safe_load(f)

# GENERAL
UPDATE_DB = _config["GENERAL"].get("update_database", True)

# DATABASE
URL = _config["DATABASE"].get("url", "HT-Annoy")
USER = _config["DATABASE"].get("user")
PASSWORD = _config["DATABASE"].get("password")
DRIVER = _config["DATABASE"].get("driver")
DB_NAME = _config["DATABASE"].get("dbname")
HOST = _config["DATABASE"].get("host")
PORT = _config["DATABASE"].get("port")


