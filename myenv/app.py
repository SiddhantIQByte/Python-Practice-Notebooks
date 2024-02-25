##Flask App URL Routiing
from flask import Flask,render_template,request,redirect,url_for  ##Create a simple flask App 

app=Flask(__name__,template_folder='tem_plate') 

@app.route("/",methods=["GET"]) #-> Url in ()
def welcome():
        return "<h2>Welcome to the project!!</h2>"

@app.route("/index",methods=["GET"])
def index():
        return "<h3>Welcome to the index page!!</h3>"
#* Variable Rule
@app.route("/success/<int:score>",methods=["GET"])
def success(score):
        return "<h3>The person has passed and the score is :</h3> "+ str(score)

@app.route("/fail/<int:score>",methods=["GET"])
def failed(score):
        return "<h3>The person has failed and the score is :</h3> "+ str(score)

@app.route("/form",methods=["GET" , "POST"])
def form():
        if request.method=="GET":
                return render_template('form.html')
        else:
                maths=float(request.form['maths'])
                science=float(request.form['science'])
                history=float(request.form['history'])
                average_marks = (maths+science+history)/3
        res=""
        if average_marks>=50:
            result="success"
        else:
            result="fail"
                

        return redirect(url_for(result,score=int(average_marks)))


        # return render_template('result.html',results=average_marks)

if __name__=="__main__":  #entry point 
        app.run(debug=True)      # if I don't give true , I ve to stop the server whenever there is a code chance , app.run takes url and port