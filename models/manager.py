class Manager:
    def __init__(self, name, picture, start_date, end_date):
        self.name = name
        self.picture = picture
        self.start_date = start_date
        self.end_date = end_date
        self.active = True
        self.team_members = []

    