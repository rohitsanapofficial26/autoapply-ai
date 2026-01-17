def generate_email_application(
    recruiter_email: str,
    subject: str,
    cover_letter: str
):
    return {
        "to": recruiter_email,
        "subject": subject,
        "body": cover_letter
    }
