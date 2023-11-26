from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/',)
def welcome():
    return "welcome to my ere"

@app.route('/pa/<int:score>/')
def qa(score):
    return "dsf"

@app.route('/pa/<int:score>/')
def pa(score):
    return "dsfdsf"


@app.route('/members/<int:marks>/')
def welcome1(marks):
    result=""
    if marks<50:
        result='fa'
    else:
        result='pa'

    return redirect(url_for(result,score=marks))




if __name__=='__main__':
    app.run(debug=True)