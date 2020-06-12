from flask import Flask
app = Flask(__name__)

@app.route('/<rwanda>/<mozambique>')
def hello_world(rwanda, mozambique):
    return 'Hello, {} and {}'.format(rwanda, mozambique)

if __name__ == '__main__':
    app.run(debug=True)