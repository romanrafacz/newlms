from flask import Blueprint, render_template, request
from app.contact.forms import ContactForm

contact_blueprint = Blueprint(
        'contact', __name__,
        template_folder = "templates")

@contact_blueprint.route('/contactus', methods=['POST', 'GET'])
def contactus():
    contactForm = ContactForm()
    return render_template('contactus.html', form=contactForm)

