from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
from flask_cors import CORS
from backend.db_helper import *
from main import *
from audio import *
import threading
from capture import *
import os
import sys

app = Flask(__name__)
CORS(app)

# Define a global variable to store the email
global_email = None

"""
Code for the database backend server.
"""

# Receiving the sign_up data credentials 
@app.route('/signup_data', methods=['POST'])
def signup_data():
    data = request.get_json()
    name = data.get('name')
    gender = data.get('gender')
    dob = data.get('dob')
    mobile = data.get('mobile')
    email = data.get('email')
    password = data.get('password')

    if insert_signup(name, gender, dob, mobile, email, password) == 1:
        response_data = {'message': 'Data inserted successfully!'}
    else:
        response_data = {'message': 'Error in inserting the data!'}
    return jsonify(response_data)

# Receiving the login_data credentials
@app.route('/login_data', methods=['POST'])
def login_data():
    global global_email
    data = request.get_json()
    print(data)
    
    # Save the email to the global variable
    global_email = data['email']
    
    response_data = search_login_credentials(global_email, data['password'])
    if response_data:
        return jsonify(response_data)   
    return jsonify({'message': 'Data not found!'})

# Router to render the index HTML template
@app.route('/')
def index_page():
    return render_template('index.html')

# Router to render the Main Quiz HTML template
@app.route('/quiz_html')
def quix_page():
    return render_template('quiz.html')

# Router to stream video frames
@app.route('/video_feed')
def video_feed():
    return Response(proctoringAlgo(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/process_audio_and_text', methods=['POST'])
def process_audio():
    record_audio()
    return jsonify({'status': 'success', 'message': 'Audio and text processing started.'})

# Router to stop the camera and flask server
@app.route('/stop_camera')
def stop_camera():
    global running
    running = False
    main_app()    
    stop_recording()
    
    print('Server stopping.....')
    
    # Redirect to a specific route
    return redirect(url_for('mic_off'))

@app.route('/mic_off')
def hello():
    # Convert the recorded audio to text
    convert_audio_to_text()
    return redirect(url_for('login_data'))
    
@app.route('/fullscreen_check', methods=['POST'])
def fullscreen_check():
    data = request.get_json()
    is_fullscreen = data.get('fullscreen')
    
    # Process fullscreen state if necessary
    if is_fullscreen is False:
        # Handle case when fullscreen mode is exited
        pass

    return jsonify({'status': 'success'})

@app.route('/window_switch', methods=['POST'])
def window_switch():
    data = request.get_json()
    user_response = data.get('response')
    question_number = data.get('question_number')
    
    # Save the response or handle it as needed
    print(user_response, question_number)
    
    return jsonify({'status': 'success'})

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    score = data.get('score')
    total_questions = data.get('total_questions')
    
    # Process and save the score in the database or perform any other logic
    save_score(global_email, score, total_questions)
    
    return jsonify({'status': 'success', 'message': 'Score submitted successfully!'})

# Main function
if __name__ == "__main__":
    print("Starting the Python Flask Server.....")
    app.run(port=5000, debug=True)


@app.route('/stop_camera')
def stop_camera():
    global running
    running = False
    main_app()    
    stop_recording()
    
    print('Server stopping.....')
    
    # Redirect to a specific route
    return redirect(url_for('hello'))

@app.route('/hello')
def hello():
    # Convert the recorded audio to text
    convert_audio_to_text()
    os._exit(0) 
    return