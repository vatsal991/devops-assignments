import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")  
mongo = PyMongo(app)
collection = mongo.db.my_collection

# Making changes for task 3
@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        data = {
            "field1": request.form.get("field1"),
            "field2": request.form.get("field2")
        }
        if not data["field1"] or not data["field2"]:
            error = "All fields are required."
        else:
            try:
                collection.insert_one(data)
                return redirect(url_for("success"))
            except Exception as e:
                error = str(e)
    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html", message="Data submitted successfully")

if __name__ == "__main__":
    app.run(debug=True)
