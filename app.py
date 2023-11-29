from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog.sql")

    def run(self):
        post = PostRepository(self._connection)
        result = post.find_with_comments(4)
        print(result)

if __name__ == '__main__':
    app = Application()
    app.run()