from flask import Flask, render_template ,redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/greeting")
def greet():
    return "Wish you good luck today!!"

@app.route("/products")
def prod():
    return "Apple, Mangoes,...!!"

@app.route("/user")
def user():
    return "<ul><li>User1</li><li>User2</li><li>User3</li></ul>"

@app.route("/users")
def users():
    return render_template("hello.html")

@app.route("/users/<userid>")
def user_name(userid):
    return render_template("hello.html", name = userid)

@app.route("/result/<int:phy>/<int:chem>/<int:maths>")
def result(phy,chem,maths):
    dict={'phy':phy,'che':chem,'maths':maths}
    return render_template("table.html",result=dict)

@app.route("/stat")
def stat():
    return render_template("s1.html")

@app.route("/sucess/<name>")
def sucess(name):
    return "Success ! Your name is"+name
{
message : "Success ! Your name is",
name:name
}

@app.route("/login", methods=["GET"])
def loginpage():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port= 5500,debug=True)