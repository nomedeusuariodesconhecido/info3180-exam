"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import app, models, db
from app.models import Emails
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session, jsonify



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('ContactsForm.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    

@app.route('/displayEmails', methods=["GET", "POST"])
def displayEmails():
    #query_result = []
    error = "Sorry... No such person!"
    if request.method =='POST':
        srch_name = request.form["personName"]
        query_result = db.session.query(Emails).filter(Emails.name==srch_name).first()
    else:
        return render_template("404.html")
    
    if query_result > 0:
        name = query_result.name
        email = query_result.email
        return render_template('ContactsForm.html', usr_name=name, usr_email=email)
    else:
        return render_template('ContactsForm.html', error=error)



# @app.route('/displayEmails/<name>', methods=["GET", "POST"])
# def displayEmails(name):
#     if request.method =='GET':
#         #name = request.form['personName']
#         query_result = Emails.query.filter_by(Emails.name==name).first_or_404()
#         query_result = db.session.query(Emails).filter(Emails.name==name).first_or_404()
#         return query_result
#     else:
#         print "Can't handle that request"
            
#     for result in query_result:
#         usr_id = result.id
#         usr_name = result.name
#         usr_email = result.email  
        
        
    
# @app.route('/renderForm/')
# def renderForm():
#     return render_template("ContactsForm.html")
    


###
# The functions below should be applicable to all Flask apps.
###
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")


# res =query_result.decode('utf-8')