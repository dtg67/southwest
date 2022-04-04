class Passenger:
    def __init__(self):
        self.confirmation_number = ""
        self.first_name = ""
        self.last_name = ""
        self.phone_number = None
        self.full_name = self.first_name + " " + self.last_name
        self.email = None

    def __iter__(self):
        yield "Name", self.full_name
        yield "First Name", self.first_name
        yield "Last Name", self.last_name
        yield "Confirmation Number", self.confirmation_number
        yield "Phone Number", self.phone_number
        yield "Email", self.email

    def set_confirmation_number(self, conf_numb):
        self.confirmation_number = conf_numb

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_email(self, email):
        self.email = email

    def get_full_name(self):
        return self.full_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number

    def get_confirmation_number(self):
        return self.confirmation_number

    def get_email(self):
        return self.email

