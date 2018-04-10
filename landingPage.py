from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/ninjas')
def projects():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def about():
    return render_template('dojos.html')
if __name__=="__main__":
    app.run(debug=True)