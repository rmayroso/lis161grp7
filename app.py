from flask import Flask, render_template
from data import memberdictionary

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/vmo')
def vmo():
    return render_template('vmo.html')

@app.route('/logo')
def logo():
    return render_template('logo.html')

@app.route('/members/<mem_type>')
def members(mem_type):
    mem_list = memberdictionary[mem_type]
    return render_template('list.html',mem_list=mem_list, mem_type=mem_type)

@app.route('/members/<mem_type>/<int:mem_index>')
def profile(mem_type, mem_index):
    mem_profile = memberdictionary[mem_type][mem_index]
    return render_template('profile.html', mem_profile=mem_profile)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)