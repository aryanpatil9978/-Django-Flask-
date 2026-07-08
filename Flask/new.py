#IMPORTING
from flask import Flask, render_template,request
import os

# INTERACTION
web = Flask(__name__)
picfolder = os.path.join("static")
web.config['UPLOAD_FOLDER'] = picfolder

# MAPPING
@web.route('/') #map in a proper manner

#ex: ('/') : www.youtube.com
#('/home') : www.youtube.com/home

# INPUTS

def home():
    pic = os.path.join(web.config['UPLOAD_FOLDER'],'Author.png')
    return render_template('home.html',pic=pic)
    return render_template('register.html')

@web.route('/register')
def register_page():
    return render_template('register.html')

@web.route('/confirmation', methods=['GET','POST'])
def confitmation_page():
    if request.method == 'POST':
        register_data = request.form
        return render_template('confirmation.html',data = register_data)
    return "Data not found"

# MAIN
if __name__ == "__main__": # is used to check whether a file is being run directly, instead of being imported into another file
    web.run(debug=True) #dont need to reload the page to see changed
