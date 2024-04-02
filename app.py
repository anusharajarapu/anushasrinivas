from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

'''@app.route('/',methods=['GET','POST'])
def demo():
    if request.method == 'POST':
        Name = request.form['name']
        branch = request.form['branch']
        marks = request.form['marks']
        print(Name,branch,marks)
    return render_template('index.html')

@app.route('/chet/<int:a>/<int:b>')
def chetu(a,b):
    return f'multiple{a},{b} is: {a*b}'
app.run()
@app.route('/nana/<string:a>/<string:b>',methods=['GET','POST'])
def nana(a,b):
    print(request.args)
    return f'{a},{b}'''

@app.route('/ush/')
def chet():
        return redirect(url_for('demo'))
@app.route('/redirected-page')
def demo():
        return render_template('index.html')
    
app.run(use_reloader=True,debug=True)
    