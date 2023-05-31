from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/',methods=['POST'])
def api_listener():
    # Handle the incoming request here
    # You can access the request data using request.data or request.json

    # Example: Print the received JSON payload
    try:
        data = request.json
        print("Data is ",data)
        print(data.keys())
    except Exception as e:
        print("Exception occurd: ", e)

    response = Response("Message Recieved", status=200)
    return response

if __name__ == '__main__':
    # Args for setting host and port for worker instance host="localhost", port=8000
    app.run(debug= True,use_reloader=True)
