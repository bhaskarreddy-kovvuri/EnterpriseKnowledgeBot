from services.gmail_service import GmailService

class GmailTool:

    def __init__(self):
        self.gmail = GmailService()

    def execute(self, query):
        return self.gmail.search(query)