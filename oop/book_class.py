class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        print(f'{self.title} by {self.author} published in {self.year}')
    
    def __del__(self):
        print('Deleting {self.title}')