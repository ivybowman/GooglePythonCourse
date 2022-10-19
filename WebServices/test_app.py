from flask import Flask, request
# From https://stackoverflow.com/a/35614301
app = Flask(__name__)


@app.route('/feedback', methods=['GET', 'POST'])
def add_message():
    content = request.json
    print(content)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)