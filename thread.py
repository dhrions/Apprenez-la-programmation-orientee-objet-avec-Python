from abc import ABC


class Thread:
    def __init__(self, title, time_posted, posts):
        self.title = title
        self.time_posted = time_posted
        self.posts = posts

    def display(self):
        pass

    def add_posts(self):
        pass


class File(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f"Fichier '{self.name}'.")


class ImageFile(File):
    def display(self):
        print(f"Le nom de l'image est {self.name}.")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content):
        pass

    def make_thread(self, title, content):
        pass


class Moderator(User):
    def edit(self, post, content):
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
    def __init__(self, file, user, time_posted, content):
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        super().display()
        self.file.display()
