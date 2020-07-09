class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0
    def receive_upvotes(self):
        self.upvotes += 1
    
    
    def is_popular(self):
        return self.upvotes > 100

class Animal:
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        if weight > 0:
            self.weight = weight
        else:
            raise Exception
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'


class tiger(Animal):
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes
    def say_great(self):
        return 'It\s GREEEEAAATTT!!!'