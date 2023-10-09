from flask import Flask , render_template , send_from_directory , request, json
import json
import os 
app = Flask(__name__) 




data = [
    {
    "temp":34,
    "humidity":22,
    "rain":98
     },
    {
    "temp":45,
    "humidity":34,
    "rain":55
    },
    {
    "temp":32,
    "humidity":44,
    "rain":102
    }
]

@app.route("/") 
def hello_world():
    return(render_template("./index.html",data=data))

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name) 

if __name__ == "__main__":
    app.run(debug=True) 
