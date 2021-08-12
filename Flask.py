from flask import Flask, redirect, url_for, render_template, request,send_file
import datetime    
from user1_test import do_plot

app = Flask(__name__)

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/predictions", methods=['GET', 'POST'])
def preds():
    if request.method == "POST":
	    user = request.form["nm"]
	    return redirect(url_for("user", usr=user))
    else:
	    return render_template("prediction.html")
    
    
    
@app.route("/<usr>")
def user(usr):
    b="need to get 1 day preds"
    c="a"
    d="need to get 30 day preds"
    if usr=="1":
        bytes_obj = do_plot()
    
        return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
    elif usr=="15":
        return c
    elif usr=="30":
        return d
    else:
        return ("none matches")

    


    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2')