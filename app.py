from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>DevOps Lab App</title></head>
    <body style="font-family:Arial; text-align:center; margin-top:80px; background:#1a1a2e; color:#eee;">
        <h1 style="color:#00d4ff;">🚀 DevOps Lab - Flask App</h1>
        <p style="font-size:18px;">Running successfully inside <b>Docker + Kubernetes</b></p>
        <p style="color:#aaa;">Containerized with Docker | Orchestrated with Kubernetes (Minikube)</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
