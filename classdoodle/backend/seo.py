from flask import Blueprint, send_from_directory
import os

seo_bp = Blueprint('seo', __name__)

@seo_bp.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../static'), 'robots.txt')

@seo_bp.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../static'), 'sitemap.xml')
