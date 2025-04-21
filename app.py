import sys
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
from datetime import datetime
import time

sys.path.insert(1, 'C://Users//HP//Desktop//mini project//Domain specific mini Project//HybridCipherMechanics')
import HybridCipherMechanics.encoDeco as hcm


def setTime():
    today = time.localtime()
    yr = today.tm_year
    month = today.tm_mon
    mday = today.tm_mday
    hr = today.tm_hour
    mint = today.tm_min
    sec = today.tm_sec
    wday = today.tm_wday
    yday = today.tm_yday
    t = [yr, month, mday, hr, mint, sec, wday, yday]
    return t

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Connect to MongoDB (Assuming MongoDB is running locally)
client = MongoClient('mongodb://localhost:27017/')
db = client['HCM_chatApp']
messages_collection = db['messages']
m_collection = db['m']
users_collection = db['users']

userInHCM = 'HCM_user'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')  # Corrected typo
    global userInHCM
    userInHCM = username
    users_collection.insert_one({
        "username": username,
        "password": password
    })
    return jsonify({'status': 'success', 'message': 'Logged in'}), 200

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('chat_message')
def handle_chat_message(data):
    username = data.get('username')
    message = data.get('message')

    if username and message:
        mes = {
            'username': username,
            'message': hcm.encryption(message),
            "time": setTime(),
            'timestamp': datetime.now()
        }

        messages_collection.insert_one(mes)
        m_collection.insert_one({
            'username': username,
            'message': message,
            'dMessage' : hcm.decryption(),
            "time": setTime(),
            'timestamp': datetime.now()
        })
        # Broadcast the message to all clients
        emit('chat_message', {'username': username, 'message': message}, broadcast=True)

@app.route('/messages', methods=['GET'])
def get_messages():
    """Retrieves chat history from MongoDB and returns it as JSON."""
    messages = m_collection.find().sort('timestamp', 1)
    chat_history = []
    for msg in messages:
        chat_history.append({
            'username': msg['username'],
            'message': msg['message'],
            'time': msg['time'],
            'timestamp': msg['timestamp']
        })
    return jsonify(chat_history)

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')  # Corrected typo
    users_collection.insert_one({
        "username": username,
        "password": password
    })
    return jsonify({'status': 'success', 'message': 'Signed up'}), 200

@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.get_json()
    if data and 'user' in data:
        received_data = data['data']
        print(f"Received data: {received_data}")
        return jsonify({'status': 'success', 'message': 'Data received'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'No data received'}), 400

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)