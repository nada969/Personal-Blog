from datetime import date
from abc import ABC , abstractmethod


class User:
    def __init__(self,name:str,type_user:str):
        if type_user not in ["admin","user"]:
            raise ValueError("type_user must be 'admin' or 'user'")
        self.name = name
        self.type = type_user


class Admin(User):
    
    def delete(self,post):
        # Admin can delete post
        pass

class Post:
    def __init__(self,user:User,title:str,date:date,doc:str):
        self.user = user
        self.title = title
        self.date = date
        self.doc = doc
        self.comments:list = []           ### composition
        self.interactions:list = []       ### composition

    def edit(self):
        pass


# Abstraction  
class Interaction(ABC):
    def __init__(self,type_interact:str,user:User, post:Post):
        self.type = type_interact
        self.user = user
        self.post = post

    @abstractmethod
    def perform(self):
        pass

def Comment(Interaction):
    def perform(self):
        print(f"{self.user.name} commented on {self.post.title}")

def Like(Interaction):
    def perform(self):
        print(f"{self.user.name} liked {self.post.title}")

def Share(Interaction):
    def perform(self):
        print(f"{self.user.name} shared {self.post.title}")




def main():
    user1 = User("Nadod", "admin")
    user2 = User("yasser","user")
    post1 = Post(user1,"post1","12-1","ljwfpejvekyfoejfcme")
    post2= Post(user2,"post2",15-1,"kiwhdowahdn")

    print(post1.date)

if __name__ == "__main__":
    main()

   