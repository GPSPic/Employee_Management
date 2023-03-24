class Employee:
    def __init__(self, name, picture, job_description, contact_details, qol_accommodations, start_date):
        self.name = name
        self.picture = picture
        self.job_description = job_description
        self.contact_details = contact_details
        self.qol_accommodations = qol_accommodations
        self.start_date = start_date
        self.end_date = None
        self.manager = None
        self.active = True