from faker import Faker

fake = Faker("ru_RU")


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        return UserData(username=fake.email(), password=fake.password())
