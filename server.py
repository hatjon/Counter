from flask import Flask, session, render_template, redirect

app = Flask(__name__)
app.secret_key= 'secret'


@app.route('/')
def index():
    if 'counter1' in session:
        session['counter1']+=1
        return render_template('index.html')
    
    if 'counter1' not in session:
        session['counter1']=0
        return render_template('index.html')

@app.route('/clear')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)