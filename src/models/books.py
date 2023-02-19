class Book():
    favs = []

    def __init__(self, title, pages) -> None:
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return True
        
    def __str__(self) -> str:
        return f'{self.title}, {self.pages} long'
    
    def __eq__(self, other):
        if self.title and self.pages == other.pages:
            return True
        
    __hash__ = None

    def __repr__(self) -> str:
        return self.__str__()