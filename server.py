from flask import Flask
from flask import Flask, render_template,session, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hate-speech-detector.html')


@app.route('/design1')
def design1():
    return render_template('design_1.html')


@app.route('/', methods=['POST'])
def process():
    text = request.form['text']

    print(text)
    return render_template('hate-speech-detector.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88)