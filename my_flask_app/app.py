from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username == username.capitalize() and password.isalnum():
            return redirect("/success")
        else:
            return redirect("/")
    
    return render_template("login.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
