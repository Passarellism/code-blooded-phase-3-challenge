from classes.Review import Review


class Movie:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if isinstance(title, str) and 0 < len(title):
            self._title = title

    title = property(get_title, set_title)

    def reviews(self):
        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        return [review.viewer for review in self.reviews()]

    def average_rating(self):
        avg_rating = [review.rating for review in self.reviews()]
        return sum(avg_rating) / len(avg_rating)


    # @classmethod
    # def highest_rated(cls):
    #     return max(movie in cls.average_rating() if )
            
