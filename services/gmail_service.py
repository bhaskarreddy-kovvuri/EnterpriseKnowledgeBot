from googleapiclient.discovery import build
from auth.gmail_auth import GmailAuthenticator

class GmailClient:

    def __init__(self):

        creds = GmailAuthenticator().authenticate()

        self.client = build(
            "gmail",
            "v1",
            credentials=creds
        )

class GmailService:

    def __init__(self):
        self.client = GmailClient()
    
    def build_query(self, args):
        query = []
        subject = args.get("subject")

        if subject:
            query.append(
                f'subject:"{subject}"'
            )

        from_email = args.get("from_email")

        if from_email:
            query.append(
                f'from:{from_email}'
            )

        keywords = args.get("body_keywords")

        if keywords:
            for word in keywords:
                query.append(word)

        return " ".join(query)


    def search(self, args):
        gmail_query = self.build_query(args)

        response = self.client.client.users().messages().list(
            userId="me",
            q=gmail_query,
            maxResults=args.get("max_results", 10)
        ).execute()

        emails = []
        
        for item in response.get("messages", []):
            full_email = self.get_email(item["id"])
            emails.append(
                self.format_email(full_email)
            )
        return emails

    def format_email(self, message):

        headers = message["payload"]["headers"]
        subject = ""
        sender = ""
        recipient = ""
        date = ""

        for header in headers:

            if header["name"] == "Subject":
                subject = header["value"]
            elif header["name"] == "From":
                sender = header["value"]
            elif header["name"] == "To":
                recipient = header["value"]
            elif header["name"] == "Date":
                date = header["value"]
        return {
            "id": message["id"],
            "threadId": message["threadId"],
            "subject": subject,
            "from": sender,
            "to": recipient,
            "date": date,
            "snippet": message.get("snippet", "")
        }
    
    def get_email(self, message_id):
        return self.client.client.users().messages().get(
            userId="me",
            id=message_id,
            format="full"
        ).execute()