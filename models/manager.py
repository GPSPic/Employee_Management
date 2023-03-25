class Manager:
    def __init__(self, name, picture, start_date, id=None):
        self.name = name
        self.picture = picture
        self.start_date = start_date
        self.id = id
        self.end_date = None
        self.active = True
        self.team_members = []

    def add_end_date(self, date):
        self.end_date = date

    def toggle_active(self):
        if self.end_date:
            self.active = False

    def add_team_member(self, employee):
        if employee not in self.team_members:
            self.team_members.append(employee)

    def remove_team_member(self, employee):
        if employee in self.team_members:
            self.team_members.remove(employee)
    
    def remove_all_team_members(self):
        self.team_members = []