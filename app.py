from flask import Flask, request

app = Flask(__name__)

@app.get('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    if not name or not message:
        return "Error"
    return f"Hello {name}! {message}!"

if __name__=='__main__':
    app.run(host='0.0.0.0')