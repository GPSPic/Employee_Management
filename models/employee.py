class Employee:
    def __init__(self, name, picture, job_description, contact_details, start_date, manager=None, id=None):
        self.name = name
        self.picture = picture
        self.job_description = job_description
        self.contact_details = contact_details
        self.start_date = start_date
        self.manager = manager
        self.id = id
        self.qol_accommodations = None
        self.end_date = None
        self.active = True
    

    def add_end_date(self, date):
        self.end_date = date

    def toggle_active(self):
        if self.end_date:
            self.active = False

    def update_manager(self, manager):
        self.manager = manager

    def remove_manager(self):
        self.manager = None