from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

SECRET = "mysecret123"

@app.route('/deploy', methods=['POST'])
def deploy():
    if request.headers.get("X-Secret") != SECRET:
        abort(403)

    subprocess.Popen(['/home/jiehoes/geonode-project/deploy.sh'])
    return 'OK'
