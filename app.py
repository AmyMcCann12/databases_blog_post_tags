from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog_posts_tags.sql")
