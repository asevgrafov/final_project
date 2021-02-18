from faker import Faker

fake = Faker("ru_RU")


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        return UserData(username=fake.email(), password=fake.password())


class PersonalInfo:
    def __init__(self, firstname, lastname, postal_code):
        self.firstname = firstname
        self.lastname = lastname
        self.postal_code = postal_code

    @staticmethod
    def random():
        return PersonalInfo(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            postal_code=fake.postcode(),
        )
