from flask import Blueprint, render_template, request
import os

seo_dashboard = Blueprint('seo_dashboard', __name__)

EXTRARANK_SERVER = os.environ.get('EXTRARANK_SERVER', 'http://127.0.0.1:8000')
SITE_HOSTNAME = os.environ.get('SITE_HOSTNAME', 'rewriteacademy.co.za')

@seo_dashboard.route('/seo-dashboard', methods=['GET', 'POST'])
def seo_dashboard_view():
    results = []
    error = None
    if request.method == 'POST':
        queries = request.form.get('queries', '').splitlines()
        queries = [q.strip() for q in queries if q.strip()]
        try:
            import httpx  # Optional dependency; lazy import avoids startup failure.
            with httpx.Client(timeout=30) as client:
                for q in queries:
                    payload = {"queries": [q], "site_hostname": SITE_HOSTNAME}
                    r = client.post(f"{EXTRARANK_SERVER}/geo/check", json=payload)
                    r.raise_for_status()
                    data = r.json()
                    results.append({"query": q, "status": "ok", "result": data})
        except Exception as e:
            error = str(e)
    return render_template('seo_dashboard.html', results=results, error=error)
