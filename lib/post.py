class Post():
    def __init__(self, id, title, content, comments = None):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        if self.comments == []:
            return f"Post ID: {self.id}\nPost Title: {self.title}\nContents: {self.content}"
        else:
            return f"Post ID: {self.id}\nPost Title: {self.title}\nContents: {self.content}\nComments: {self.comments}"
    