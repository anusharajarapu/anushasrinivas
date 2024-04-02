from flask import Flask,request,render_template,redirect,url_for
app = Flask(__name__)

@app.route('/')
def demo():
    return render_template('register.html')

@app.route('/register',methods['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        pwd = request.form['password']
        phone = request.form['phone']
        place = request.form['place']
        data = {'name':name,mail,pwd,phone,'place':}
        if data['mail'] and data['pwd']:
            print(data['mail'], data['pwd'])
        return redirect(url_for('login',mail=data['mail'],pwd=data))
        else:
            return render_template('register.html')
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login(mail,pwd):
    if request.method == 'POST':
        user = request.form['A@n@u']
        pwd = request.form['pwd']
        if mail == user:
            return [user,pwd]
        else:
             return render_template('register.html')
    return render_template('register.html')

    app.run(use_reloader=True,debug=True)
