from flask import Flask
app = Flask(__name__)

@app.route('/')
def sample():
    return "<h2 style='color:blue'>Welcome to Deloitte Cloud CICD Demo - This is Change#1</h2><a href="https://www.w3schools.com">Visit W3Schools</a>"

if __name__ == '__main__':
    app.run()
