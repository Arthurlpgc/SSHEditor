from flask import Flask, request
from connector import Connection
import sys, random, json

dic = {}
app = Flask(__name__)
@app.route('/connect/', methods=['POST'])
def get_conn():
    rnd = str(random.randint(0, 1000000))
    params = request.json
    dic[rnd] = Connection(hostname=params['hostname'], username=params['username'], password=params['password'])
    return rnd


@app.route('/getpath/', methods=['POST'])
def get_path():
    params = request.json
    files = dic[params['key']].get_file_structure(path=params['path'])
    return json.dumps(files)
if __name__ == '__main__':
    app.run(host='0.0.0.0')