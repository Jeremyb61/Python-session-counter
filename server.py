from flask import Flask, render_template, request, redirect, session
app= Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter']+=1
    return render_template('index.html', add=session['counter'])

@app.route('/add2', methods=['POST'])
def add():
    session['counter'] = session['counter'] + 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    del session['counter']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

