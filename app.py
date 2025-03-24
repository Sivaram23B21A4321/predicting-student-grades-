from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders index.html located in templates folder

if __name__ == '__main__':
    app.run(debug=True)
