import schedule
import time
import httpx
import os
from .mailer import send_application_email

EXTRARANK_SERVER = os.environ.get('EXTRARANK_SERVER', 'http://127.0.0.1:8000')
SITE_HOSTNAME = os.environ.get('SITE_HOSTNAME', 'vele-secondary.co.za')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@example.com')

QUERIES = [
    'high school support',
    'online school South Africa',
    'Vele Secondary School',
    'student timetable',
]

def run_seo_geo_check():
    results = []
    for q in QUERIES:
        payload = {"queries": [q], "site_hostname": SITE_HOSTNAME}
        try:
            with httpx.Client(timeout=30) as client:
                r = client.post(f"{EXTRARANK_SERVER}/geo/check", json=payload)
                r.raise_for_status()
                data = r.json()
                results.append(f"Query: {q}\nResult: {data}\n")
        except Exception as e:
            results.append(f"Query: {q}\nError: {e}\n")
    # Email results
    body = "SEO/Geo Check Results:\n\n" + "\n".join(results)
    send_application_email(ADMIN_EMAIL, "SEO/Geo Weekly Report", body)

schedule.every().monday.at("08:00").do(run_seo_geo_check)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
