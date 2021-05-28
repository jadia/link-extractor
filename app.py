from flask import Flask, render_template, request, url_for
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField, validators
from extract import GetFileLinks
from datetime import datetime as dt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'
APP_NAME = 'Link Extractor'

class InputForm(Form):
    input_url = StringField('Directory URL')
    extension = StringField('Extension of files')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        print("Post request")
        url = request.form['input_url']
        ext = request.form['extension']
        file_links = GetFileLinks(url, ext)
        return render_template('result.html', 
                                extension=request.form['extension'], 
                                result=file_links.get_file_links())
    else:
        print("Get request.")
        return render_template('index.html', form=form)


@app.context_processor
def inject_now():
    return {'now': dt.utcnow()}


@app.context_processor
def inject_app_name():
    return {'app_name': APP_NAME}


@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html") 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
