from flask import Blueprint, render_template, request, send_from_directory
import os

seo_bp = Blueprint('seo', __name__)

@seo_bp.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../static'), 'robots.txt')

@seo_bp.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../static'), 'sitemap.xml')

@seo_bp.route('/seo-dashboard-static')
def seo_dashboard_static():
    # Legacy placeholder view kept on a separate route.
    results = []
    return render_template('seo_dashboard.html', results=results)
