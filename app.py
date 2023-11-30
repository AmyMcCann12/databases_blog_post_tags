from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog_posts_tags.sql")

    def run(self):
        post_repository = PostRepository(self._connection)
        post_repository.delete(2)
        posts = post_repository.all()
        for post in posts:
            print(post)


if __name__ == '__main__':
    app = Application()
    app.run()