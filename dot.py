from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def demo():
    if request.method == 'POST':
        #print(request.form)
        SEext = int(request.form['se'])
        CNext = int(request.form['cn'])
        IOText = int(request.form['iot'])
        SEint = int(request.form['intse'])
        CNint = int(request.form['intcn'])
        IOTint = int(request.form['intiot'])

        SE = SEext+SEint
        CN = CNext+CNint
        IOT = IOText+IOTint
        #print(SE,CN,IOT)
        if SE<35 or CN<35 or IOT<35:
            return 'Sorry U r  Fial better Lucky Next Time!!!'
        marks = SE+CN+IOT
        if marks<=210:
            result = 'FAIL'
        elif 211<=marks<=300:
            result ='Just pass'
        else:
            result = 'Results Not Relesed'
        return render_template('dot.html',result = result)
    return render_template('dot.html')

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
