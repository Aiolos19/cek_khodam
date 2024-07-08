from flask import Flask, render_template, request, redirect, url_for
import random
from khodam_list import khodam_list

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        khodam = random.choice(khodam_list)
        return render_template('index.html', khodam=khodam, name=name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# for public
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
