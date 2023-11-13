from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/eating-disorders')
def eating_disorders():
    return render_template('eating_disorders.html')

@app.route('/suicide-prevention')
def suicide_prevention():
    return render_template('suicide_prevention.html')

@app.route('/combination')
def combination():
    return render_template('combination.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
