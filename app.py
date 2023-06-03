from flask import Flask, render_template, request
from translatorE2F import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate/english_to_french', methods=['POST'])
def translate_english_to_french():
    if request.method == 'POST':
        text = request.form['text']
        translated_text = english_to_french(text)
        return render_template('result.html', text=text, translated_text=translated_text)
    else:
        return 'Method Not Allowed', 405

@app.route('/translate/french_to_english', methods=['POST'])
def translate_french_to_english():
    if request.method == 'POST':
        text = request.form['text']
        translated_text = french_to_english(text)
        return render_template('result.html', text=text, translated_text=translated_text)
    else:
        return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run()
