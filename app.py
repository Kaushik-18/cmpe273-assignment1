from flask import Flask
from flask import abort
import requests
import base64
import sys

app = Flask(__name__)

GIT_BASE_URL = "https://api.github.com/"


def parse_input_url(url_args):
    vals = url_args.split("github.com/")
    try:
        global GIT_BASE_URL
        GIT_BASE_URL = GIT_BASE_URL + "repos/" + vals[1]
    except IndexError:
        print "Invalid URL"


@app.route('/')
def hello():
    return "First App"


@app.route('/v1/<path:path>')
def get_config(path):
    urls = GIT_BASE_URL + "/contents/" + path
    outputs = requests.get(urls)
    status_code = outputs.status_code
    if status_code == 200:
        enc_file_value = outputs.json()['content']
        return base64.b64decode(enc_file_value)
    else:
        abort(404)


# calling api , parsing url from command line


if __name__ == '__main__':
    if sys.argv > 1:
        parse_input_url(sys.argv[1])

    app.run(debug=True, host='0.0.0.0')
