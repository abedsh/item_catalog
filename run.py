from app import app

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()





#from flask import Flask
#app = Flask(__name__)
#@app.route("/")
#def hello():
#    return "Hello, I love Digital Ocean!"
#if __name__ == "__main__":
#    app.run()
