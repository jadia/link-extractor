from flask import Flask, render_template, request, url_for, send_file
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField, validators
from extract import GetFileLinks
from datetime import datetime as dt
import shortuuid
import os


URL_TXT_DIR = 'files'
if not os.path.exists(URL_TXT_DIR): os.makedirs(URL_TXT_DIR)

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
        file_links_obj = GetFileLinks(url, ext)
        url_list = file_links_obj.get_file_links()

        unique_id = shortuuid.uuid(name=url)
        url_list_file_name = url.split("://")[1].split("/")[0] + '-' + unique_id + '.txt'
        url_list_file_path = os.path.join(URL_TXT_DIR ,url_list_file_name)
        with open(url_list_file_path, 'w') as f:
            f.writelines("%s\n" % url for url in url_list)

        return render_template('result.html', 
                                extension=ext, 
                                result=url_list,
                                file_name=url_list_file_name)
    else:
        print("Get request.")
        return render_template('index.html', form=form)

@app.route('/download/<file_name>', methods=['GET'])
def download_url_file(file_name):
    # unique_id = shortuuid.uuid(name=url)
    # url_list_file = url.split("://")[1].split("/")[0] + '-' + unique_id + '.txt'
    url_list_file = os.path.join(URL_TXT_DIR ,file_name)
    return send_file(url_list_file, as_attachment=True, attachment_filename='urls_list.txt')

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
    app.run(host='0.0.0.0', port=4000)
