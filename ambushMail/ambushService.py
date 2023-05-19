import base64
import msal
import requests

class AmbushService:
    """
    Class representing the Ambush mail service.

    Args:
        client_id (str): The client ID for authentication.
        client_secret (str): The client secret for authentication.
        tenant_id (str): The ID of the tenant.
        user_id (str): The ID of the user.
        to_mail (str): The email address of the recipient(s) (comma-separated for multiple recipients).
        cc_mail (str): The email address of the recipient(s) to be CC'd (comma-separated for multiple recipients).
        subject (str): The subject of the email.
        body (str): The body/content of the email.
        token (str): The authentication token.

    Attributes:
        client_id (str): The client ID for authentication.
        client_secret (str): The client secret for authentication.
        tenant_id (str): The ID of the tenant.
        user_id (str): The ID of the user.
        to_mail (str): The email address of the recipient(s) (comma-separated for multiple recipients).
        cc_mail (str): The email address of the recipient(s) to be CC'd (comma-separated for multiple recipients).
        subject (str): The subject of the email.
        body (str): The body/content of the email.
        token (str): The authentication token.
        authority (str): The authority URL for authentication.
        app (msal.ConfidentialClientApplication): The MSAL application instance for authentication.
        scopes (list): The list of scopes for authentication.

    """
    def __init__(self, client_id, client_secret, tenant_id, user_id, to_mail, cc_mail,
                 subject, body, token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.to_mail = to_mail
        self.cc_mail = cc_mail
        self.subject = subject
        self.body = body
        self.token = token
        self.authority = f"https://login.microsoftonline.com/{self.tenant_id}"
        self.app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority
        )
        self.scopes = ["https://graph.microsoft.com/.default"]

    def send_mail(self, attachment_files=None, attachment_file_names=None, bcc_mail=None):
        """
        Send an email using the Ambush mail service.

        Args:
            attachment_files (list, optional): List of attachment files to be included.
            attachment_file_names (list, optional): List of names for the attachment files.
            bcc_mail (str, optional): The email address of the recipient(s) to be BCC'd (comma-separated for multiple recipients).

        Returns:
            dict: Response indicating the status of the email send operation.
        """
        if self.token:
            endpoint = f"https://graph.microsoft.com/v1.0/users/{self.user_id}/sendMail"

            to_recipients = list(map(lambda email: {"EmailAddress": {"Address": email}}, self.to_mail.split(",")))
            cc_recipients = list(map(lambda email: {"EmailAddress": {"Address": email}}, self.cc_mail.split(","))) if self.cc_mail else []
            bcc_recipients = list(map(lambda email: {"EmailAddress": {"Address": email}}, bcc_mail.split(","))) if bcc_mail else []
            attachments = []
            if attachment_file_names and attachment_files:
                attachments = [
                    {
                        "@odata.type": "#microsoft.graph.fileAttachment",
                        "Name": name,
                        "ContentBytes": base64.b64encode(file).decode("utf-8")
                    }
                    for name, file in zip(attachment_file_names, attachment_files)
                ]

            mail_msg = {
                "Message": {
                    "Subject": self.subject,
                    "Body": {"ContentType": "html", "Content": self.body},
                    "ToRecipients": to_recipients,
                    "ccRecipients": cc_recipients,
                    "bccRecipients": bcc_recipients,
                    "Attachments": attachments
                },
                "SaveToSentItems": "true"
            }

            mail_send = requests.post(
                endpoint,
                headers={"Authorization": "Bearer " + self.token},
                json=mail_msg
            )
            return mail_send
