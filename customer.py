# Observer Pattern for notifying customers
class Customer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")
