from flask import Blueprint, render_template
from backend.caps_subjects import CAPS_GRADE8_SUBJECTS, CAPS_GRADE9_SUBJECTS, CAPS_GRADE10_SUBJECTS

premium_bp = Blueprint('premium', __name__)

@premium_bp.route('/premium-extra-class')
def premium_extra_class():
    # Show all CAPS subjects for Grades 8, 9, and 10
    return render_template('premium_extra_class.html', 
        subjects_8=CAPS_GRADE8_SUBJECTS, 
        subjects_9=CAPS_GRADE9_SUBJECTS, 
        subjects_10=CAPS_GRADE10_SUBJECTS)
