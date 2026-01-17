def decide_apply_method(job_url: str):
    if "mailto:" in job_url:
        return "email"
    if "greenhouse.io" in job_url or "lever.co" in job_url:
        return "manual"
    return "manual"
