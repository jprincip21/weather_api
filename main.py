from flask import Flask, render_template

app = Flask(__name__) # Create a Flask instance named Website


@app.route("/") #Decorator connects app.route to home function
def home():
    return render_template("home.html") # Render_template looks for a templates folder and finds the file we are requesting

@app.route("/api/v1/<station>/<date>") # <> Means user can enter a value
def about(station, date):
    temperature = 23

    return {"station": station, # Taken from URL
            "date": date, # Taken from URL
            "temperature": temperature # Taken from CSV
            }

if __name__ == "__main__":
    app.run(debug=True)


