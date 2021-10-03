last_id = 0


class DVD:
    def __init__(self, title, genre):
        global last_id
        self.title = title
        self.genre = genre
        last_id += 1
        self.id = last_id
