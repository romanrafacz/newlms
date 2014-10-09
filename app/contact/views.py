from flask import Blueprint, render_template, request, url_for, redirect, flash
from app import mail
from flask_mail import Message
from app.contact.forms import ContactForm
from app.models import Contact

contact_blueprint = Blueprint(
        'contact', __name__,
        template_folder = "templates")


@contact_blueprint.route('/contactus', methods=['POST', 'GET'])
def contactus():
    """
    Process and send email confirmation
    """

    contactForm = ContactForm()

    if request.method == 'POST':
        form_firstname=request.form['firstname']
        form_lastname=request.form['lastname']
        form_email=request.form['email']
        form_comments=request.form['comments']
        flash('email sent')

        msg = Message('Hello', recipients=form_email)
        mail.send(msg)

        return redirect('contactus')

    return render_template('contactus.html', form=contactForm)

