from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/endpoint/<search_term>') # This is the route, url or endpoint
def hello(search_term): # This is your function name and input.
    print("value is: {}".format(search_term))
    print("type is: {}".format(type(search_term)))
    if float(13.8) == float(search_term):
        print("Comparison operator worked")
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)


