from flask import Flask
app = Flask(__name__)

@app.route('/give/<name>/<lastname>')
def hello_name(name,lastname):
   return "hello"+" "+name+" "+lastname

if __name__ == '__main__':
   app.run(debug = True)