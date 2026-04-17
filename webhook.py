from flask import Flask, request, abort
import subprocess
import hmac
import hashlib

app = Flask(__name__)

SECRET = b"mysecret123"

@app.route('/deploy', methods=['POST'])
def deploy():
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        abort(403)

    sha_name, signature = signature.split('=')

    mac = hmac.new(SECRET, msg=request.data, digestmod=hashlib.sha256)

    if not hmac.compare_digest(mac.hexdigest(), signature):
        abort(403)

    subprocess.Popen(['/home/jiehoes/geonode-project/deploy.sh'])
    return 'OK'