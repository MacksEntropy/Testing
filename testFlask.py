from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_listener():
    # Handle the incoming request here
    # You can access the request data using request.data or request.json

    # Example: Print the received JSON payload
    data = request.json
    print(data)

    # Return a response if needed
    return 'Received the request successfully', 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
