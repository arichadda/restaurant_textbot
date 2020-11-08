class Restaurant:
    def __init__(self, name, rating, user_ratings_count, open_):
        self.name = name
        self.rating = rating
        self.user_ratings_count = user_ratings_count
        self.open_ = open_
    
    def __str__(self):
        return self.name + " with a rating of " + str(self.rating) + " out of 5 and " + str(self.user_ratings_count) + " ratings"