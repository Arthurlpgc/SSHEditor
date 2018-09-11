from flask import Flask
from connector import Connection
x = Connection()

app = Flask(__name__)
@app.route('/', methods=['GET'])
def get_test():
    return ''' 
<html>
    <head></head>
    <body>
    %s
    </body>
</html>
''' % x.get_file_structure('/test_dir')
if __name__ == '__main__':
    app.run(host='0.0.0.0')