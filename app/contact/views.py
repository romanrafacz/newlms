from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.contact.forms import ContactForm
from app.models import Contact
from app import db

contact_blueprint = Blueprint(
        'contact', __name__,
        template_folder = "templates")


@contact_blueprint.route('/contactus', methods=['POST', 'GET'])
def contactus():
    contactForm = ContactForm()

    if request.method == 'POST':
        form_firstname=request.form['firstname']
        form_lastname=request.form['lastname']
        form_email=request.form['email']
        form_comments=request.form['comments']
        db.session.add(Contact(firstname=form_firstname, lastname=form_lastname, email=form_email, comments=form_comments)) 
        db.session.commit()
        flash('email sent')
        return redirect('contactus')

    return render_template('contactus.html', form=contactForm)

