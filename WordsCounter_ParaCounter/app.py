# Words Counter and Paragraphs Counter Flask App using Python

from flask import Flask,request,render_template
from datetime import date

#### Defining Flask App
app = Flask(__name__)


#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

def replace_multiple_newlines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

################## ROUTING FUNCTIONS #########################

#### Our main page
@app.route('/')
def home():
    return render_template('index.html',datetoday2=datetoday2) 

#### This function will run when we add a new user
@app.route('/count', methods=['GET', 'POST'])
def count():
    text = request.form['text']
    
    words = len(text.split())
    paras = replace_multiple_newlines(text)

    clean_text = text.replace('\r', '').replace('\n', '')
    chars = len(clean_text)

    # Pass original text to the template
    return render_template(
        'index.html',
        words=words,
        paras=paras,
        chars=chars,
        text=text,  # Send the entered text back
        datetoday2=datetoday2
    )



#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)
