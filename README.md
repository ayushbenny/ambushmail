# Ambush Mail Service

The AmbushService class represents a mail service that utilizes the Ambush platform for sending emails. It provides a convenient way to authenticate and send emails using the Microsoft Graph API.

# Initialization
To use the AmbushService, you need to provide the following parameters during initialization:

    > client_id (str): The client ID for authentication.
    > client_secret (str): The client secret for authentication.
    > tenant_id (str): The ID of the tenant.
    > user_id (str): The ID of the user.
    > to_mail (str): The email address of the recipient(s) (comma-separated for multiple recipients).
    > cc_mail (str): The email address of the recipient(s) to be CC'd (comma-separated for multiple recipients).
    > subject (str): The subject of the email.
    > body (str): The body/content of the email.
    > token (str): The authentication token.

# Sending an Email
You can send an email using the send_mail method of the AmbushService class. It accepts the following optional parameters:

    > attachment_files (list): List of attachment files to be included.
    > attachment_file_names (list): List of names for the attachment files.
    > bcc_mail (str): The email address of the recipient(s) to be BCC'd (comma-separated for multiple recipients).
The send_mail method returns a dictionary containing the response indicating the status of the email send operation.

Please note that you need to have a valid authentication token (token) in order to send emails using the Ambush mail service.

# Example Usage:
    ambush = AmbushService(
        client_id="your_client_id",
        client_secret="your_client_secret",
        tenant_id="your_tenant_id",
        user_id="your_user_id",
        to_mail="recipient@example.com",
        cc_mail="cc_recipient@example.com",
        subject="Hello from Ambush",
        body="This is the email content.",
        token="your_authentication_token"
        ).send_mail()

This is a basic example demonstrating how to use the AmbushService class to send an email with an attachment and BCC recipient.

Note: Make sure to replace the placeholder values with your own credentials and recipient information.

For more information on the Ambush mail service, refer to the official documentation or contact the Ambush support team.