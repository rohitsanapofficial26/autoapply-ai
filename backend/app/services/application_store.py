applications = []

def save_application(job_url: str, status: str):
    applications.append({
        "job_url": job_url,
        "status": status
    })

def get_applications():
    return applications
