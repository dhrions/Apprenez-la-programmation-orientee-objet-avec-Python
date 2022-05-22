class Thread:
    def __init__(self, title,time_posted,posts):
        self.title = title
        self.time_posted = time_posted
        self.posts = posts

    def display(self):
        pass
    def add_posts(self):
        pass

class File:
    def __init__(self):
        self.name = name
        self.size = size

    def display(self):
        pass

class Image(File):

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        pass
    def post(self, thread, content):
        pass
    def make_thread(self,title,content):
        pass

class Moderator(User):
    def edit(self,post,content):
        pass
    def delete(self, thread, post):
        pass

class Post:
    def __init__(self, user, time_posted, content):
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        pass

class FilePost(Post):
    def __init__(self, file):
        self.file = file
