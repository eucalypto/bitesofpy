class RecordScore():
    max_score: int = None

    """Class to track a game's maximum score"""
    def __call__(self, current_score, *args, **kwargs):
        if self.max_score is None:
            self.max_score = current_score
        if current_score > self.max_score:
            self.max_score = current_score
        return self.max_score
