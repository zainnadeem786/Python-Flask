from flask import Flask, redirect , url_for , render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World  This Is First Flask Program'

#app.run(host,port,debug,option)
#app.run(port=8000)

@app.route('/home')
def index():
    return "Home Page"

@app.route('/display/<name>')
def display(name):
    return f"Name is :{name}"

# Redirect 
@app.route('/google')
def web():
    # return redirect('https://www.google.com')
    return url_for('home')

#Form Get
@app.route('/form')
def form():
    return render_template('forms .html')
@app.route('/submit',methods=['POST'])
def submit():
    return " Form is Submit"

app.run(port=8000, debug=True)