"""Settings module"""

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(".env"))

# pylint: disable=too-few-public-methods


class Settings:
    """
    Class for managing application settings.

    This class reads environment variables from a .env file and provides
    access to various configuration settings used by the application.

    Attributes:
        ENVIRONMENT (str): The current environment (e.g., "dev", "prod").
        APP_PASSWORD (str): The application password.
        SECRET_KEY (str): The secret key used for token generation.
        ALGORITHM (str): The algorithm used for token generation.
        ACCESS_TOKEN_EXPIRE_MINUTES (int): The expiration time for access tokens in minutes.
        NEO4J_URI (str): The URI for connecting to Neo4j database.
        NEO4J_USERNAME (str): The username for Neo4j authentication.
        NEO4J_PASSWORD (str): The password for Neo4j authentication.
        SYSADMIN_USERNAME (str): The username for the sysadmin account.
        SYSADMIN_PASSWORD (str): The password for the sysadmin account.
        SYSADMIN_EMAIL (str): The email address for the sysadmin account.

    Example:
        settings = Settings()
        print(settings.SECRET_KEY)
        print(settings.NEO4J_URI)
    """

    ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
    APP_PASSWORD = os.environ.get("APP_PASSWORD")
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
    ALGORITHM = os.environ.get("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get(
        "ACCESS_TOKEN_EXPIRE_MINUTES", 10_080))  # one week
    NEO4J_URI = os.environ.get("NEO4J_URI")
    NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")


settings = Settings()
