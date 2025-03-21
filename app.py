import sys

sys.path.insert(1, 'C://Users//HP//Desktop//mini project//Domain specific mini Project//HybridCipherMechanics')
import HybridCipherMechanics.encoDeco as hcm

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
from pymongo import MongoClient
from datetime import datetime
import time
import platform

system_name = platform.system()
print(system_name)

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
db = client['chat-app']
messages_collection = db['messages']
m_collection = db['m']





@app.route('/')
def index():
    return render_template('index.html')

# Handle incoming chat messages
@socketio.on('message')
def handle_message(msg):
    # Save message to MongoDB
    message = {
        'username': system_name,  # In a real app, you would fetch the username
        'message': hcm.encryption(msg),
        "time" : setTime(),
        'timestamp': datetime.now()
    }

    messages_collection.insert_one(message)
    m_collection.insert_one({
        'username': platform.system(),  #In a real app, you would fetch the username
        'message': msg,
        "time" : setTime(),
        'timestamp': datetime.now()
    })

    # Broadcast the message to all clients
    send(msg, broadcast=True)

# Fetch chat history
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = m_collection.find().sort('timestamp', 1)
    chat_history = []
    for msg in messages :
        chat_history.append({
            'username': msg['username'],
            'message': msg['message'],
            'time': msg['time'],
            'timestamp': msg['timestamp']
        })
    return jsonify(chat_history)

if __name__ == '__main__' :
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
