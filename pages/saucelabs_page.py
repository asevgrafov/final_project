class SauceLabsPage:
    def __init__(self, app):
        self.app = app

    def get_title(self):
        return self.app.driver.title
