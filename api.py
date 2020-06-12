import csv

from flask import Flask, jsonify
app = Flask(__name__)

def import_data(filename):
    return_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return_list.append(dict(row))
    return return_list

@app.route('/state/<search_term >')
def state(search_term):
    return_list = []
    for row in data:
        if row["State"] == search_term:
            return_list.append(row["County"])
    return jsonify(return_list)

@app.route('/county/<search_term>')
def county(search_term):
    return_list = []
    for row in data:
        if row["County"] == search_term:
            return_list.append(row["State"])
    return jsonify(return_list)

if __name__ == '__main__':
    data = import_data("county_demographics.csv")
    app.run(debug=True)

