### integrating HTML with flask web framework
# HTTP VERBS GET and POST




from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('webview2.html')

@app.route("/success")
def success():
    return render_template('output.html',result='PASS')


@app.route("/fail")
def fail():
    return render_template('output.html',result='FAIL')
    

### resultchecker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        Science=float(request.form['Science'])
        Maths=float(request.form['Maths'])
        C=float(request.form['C'])
        total_score=(Science+Maths+C)/3
    res=""
    if total_score>=50:
        res="success"
    else:
        res='fail'
    return redirect(url_for(res,score=total_score))

if __name__=='__main__':
    app.run(debug=True)