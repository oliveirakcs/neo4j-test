import os
from neo4j import GraphDatabase
from config import settings

NEO4J_URI = os.environ.get("NEO4J_URI")


"""Provides a database module for interacting with a Neo4j database.

This module contains the `Database` class, which provides methods for
interacting with a Neo4j database. The `Database` class allows you to perform
various operations such as retrieving entity records, retrieving entities by
UUID or parameter, creating new entities, updating entities, and creating
relationships between entities.
"""


DEFAULT_QUERY_SKIP = 0
DEFAULT_QUERY_LIMIT = 100


class Database:
    """
    Provides methods for interacting with a Neo4j database.

    Args:
        uri (str): The URI of the Neo4j database.
        username (str): The username for authentication.
        password (str): The password for authentication.

    Attributes:
        driver (neo4j.GraphDatabase.driver): The Neo4j driver for database
        connection.

    """

    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))


database = Database(
    uri=settings.NEO4J_URI,
    username=settings.NEO4J_USERNAME,
    password=settings.NEO4J_PASSWORD,
)
