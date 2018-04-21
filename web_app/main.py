from flask import Flask, request, render_template
from ctrlmodel import searchNodes

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    node = None
    if request.method == 'POST':
        text = request.form['text']
        node = searchNodes(str(text))

    return render_template('index.html', node=node)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
