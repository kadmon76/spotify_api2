
from flask import Flask, request, Response 
import json



app = Flask(__name__)
@app.route('/', methods=['POST','GET']) #<--decoration using flask to conecct to through url
def index(): 
    if request.method == 'POST': #<-- if webhook is resiving msg store message
        pass
        return Response('ok', status = 200)
    else:
        pass
    return b'<h1>sddd</h1>'


def main():
   pass 


if __name__ == "__main__":
    app.run(debug = True)


