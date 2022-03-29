from http.client import OK
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/mobile-control/<action>', methods=['GET'])
def handleAction(action):
    # TODO: Here we have an action comming from mobile using UART here to map it to the embedded board
    return 'OK'


# # More Secure way to pass action data
# @app.route('/mobile-control/action', methods=['POST'])
# def handleAction():
#     if request.method == 'POST':
#         data = request.json
#         print(data['Action'])
#         print(data['Reporter'])

#         # TODO: Here we have an action comming from mobile using UART here to map it to the embedded board

#     return 'OK'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
