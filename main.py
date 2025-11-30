from flask import Flask, render_template
import pandas as pd

app = Flask(__name__) # Create a Flask instance named Website


@app.route("/") #Decorator connects app.route to home function
def home():

    filepath = "data/stations.txt"
    stations = pd.read_csv(filepath, skiprows=17)
    stations = stations[["STAID", "STANAME                                 "]]
    # Render_template looks for a templates folder and finds the file we are requesting
    #.to_html() changes the stations variable from a data frame to html code
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>") # <> Means user can enter a value
def about(station, date):
    # .zfill(6) Takes the station ID and ensures it is 6 digits, the value provided will be on the right and added values will be 0
    # ie, station = 10, .zfill(6) outputs 000010
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    print(filename)

    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"]) # Read Data for user requested station, skips unneeded info and parses dates

    # Grabs the cell at specified date for the TG column. .squeeze() allows us to return only the  value from that cell and ignore the index
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    return {"station": station, # Taken from URL
            "date": date, # Taken from URL
            "temperature": temperature # Taken from CSV
            }

if __name__ == "__main__":
    app.run(debug=True, port=5001)


