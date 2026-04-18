from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/deploy', methods=['POST'])
def deploy():
    try:
        print("=== WEBHOOK HIT ===")
        print("Headers:", dict(request.headers))
        print("Data:", request.data)

        subprocess.Popen(
            ['/home/jiehoes/geonode-project/deploy.sh'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return 'OK', 200

    except Exception as e:
        print("ERROR:", str(e))
        return 'ERROR', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)