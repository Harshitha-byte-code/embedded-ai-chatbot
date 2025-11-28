# Task 2: Flask Server + Streamlit Vehicle Control Panel Reflection

## Architecture Description
Understanding the Client-Server Architecture:
In our vehicle control system, we implemented a classic client-server architecture with clear separation of concerns:

The Client (Streamlit Control Panel):
The Streamlit application acts as the client and serves as the user interface. It provides an intuitive web-based control panel with interactive elements including a speed slider (0-255) and directional buttons (Forward, Backward, Left, Right, and Stop). When a user interacts with any control element, the client prepares a JSON payload containing the direction and speed parameters, then sends an HTTP POST request to the Flask server's /move endpoint. The client also displays real-time feedback to users about command success or failure, making the interface responsive and informative.

The Server (Flask API):
The Flask application serves as the backend server, listening for incoming HTTP requests on port 5001. It exposes RESTful API endpoints, primarily the /move endpoint which accepts POST requests with JSON payloads. When the server receives a command, it validates the data, processes it, and currently prints the command to the console terminal. The server returns appropriate HTTP status codes and JSON responses to inform the client whether the command was successfully received and processed.
Where the Arduino Vehicle Fits In:

In the complete embedded system architecture, the Arduino Uno WiFi will be integrated as the hardware control layer. The architecture will work as follows:

User Interaction Layer: User clicks "Forward" button on Streamlit web interface
Client Processing: Streamlit sends POST request: {"direction": "forward", "speed": 150} to Flask server
Server Processing: Flask receives and validates the command
Hardware Communication: Flask forwards the command to Arduino via WiFi or serial connection
Physical Control: Arduino interprets the command and controls motor drivers (likely using PWM for speed control)
Vehicle Movement: The physical vehicle moves forward at the specified speed

The Flask server essentially acts as a bridge or gateway between the web-based control interface and the embedded hardware. This separation allows us to:

Control the vehicle from any device with a web browser
Easily add features like authentication, logging, or multiple user support
Update the user interface without modifying Arduino code
Scale to control multiple vehicles from one interface

One Bug and How I Fixed It
The Bug:
When attempting to run the Streamlit control panel, I encountered a frustrating error: Error: Invalid value: File does not exist: week03_task2_streamlit_control.py. This error appeared multiple times despite the file clearly existing in my GitHub repository.
Root Cause Analysis:
After careful debugging, I realized the issue was related to my current working directory. I was executing the streamlit run command while positioned in the flask_server directory, but the Streamlit control panel file was actually located in a separate streamlit_app directory. The error message was accurate - the file didn't exist relative to my current directory, even though it existed in the project.
The Solution:
I fixed this by properly navigating the directory structure:

First, I used cd .. to move back to the parent directory (embedded-ai-chatbot)
Then, I navigated to the correct location: cd streamlit_app
Finally, I ran the command: streamlit run week03_task2_streamlit_control.py

This time, the application launched successfully!
What I Learned:
This debugging experience taught me several important lessons:

Directory awareness: Always verify your current working directory before running commands. The terminal prompt shows this, but I needed to pay more attention.
Project structure understanding: Taking time to understand the folder hierarchy of a project prevents navigation errors.
Reading error messages carefully: The error message was actually very clear - "File does not exist" meant it couldn't find the file in the current directory, not that the file was missing from the project.
Using absolute vs relative paths: I could have also used the full path: streamlit run ~/embedded-ai-chatbot/streamlit_app/week03_task2_streamlit_control.py from any directory.

Additional Technical Learning:
Beyond this directory issue, I also learned about Flask-CORS (Cross-Origin Resource Sharing), which was essential for allowing the Streamlit frontend (running on one port) to communicate with the Flask backend (running on a different port). Without CORS enabled, browsers would block the requests due to security policies. Adding CORS(app) to the Flask application resolved this cross-origin issue.

Overall Learning Experience
Technical Skills Gained

Building interactive web applications with Streamlit
Creating RESTful APIs with Flask
Integrating third-party APIs (OpenAI)
Understanding client-server communication patterns
Working with HTTP requests and JSON data
Managing environment variables and API keys securely
Implementing error handling for network requests
Understanding CORS and cross-origin security

Challenges Overcome

Directory navigation and project structure organization
API key management and environment configuration
Debugging network communication issues
Balancing user experience with technical constraints

Future Improvements
For future iterations of this project, I would:

Add user authentication and session management
Implement rate limiting to prevent API abuse
Add comprehensive logging for debugging and monitoring
Deploy both services to cloud platforms (Render, Heroku, or AWS)
Implement WebSocket connections for real-time bidirectional communication
Add unit tests and integration tests for both applications
Create a mobile-responsive design for the control panel
Implement emergency stop functionality that works even if the main interface fails

Connection to Embedded AI
This project demonstrates the practical application of AI and embedded systems working together. The chatbot shows how AI can provide intelligent, conversational interfaces, while the vehicle control system demonstrates how web technologies can interface with embedded hardware. Together, these skills form the foundation for creating sophisticated embedded AI systems that can interact naturally with users while controlling physical hardware - the future of robotics and IoT.

Submitted by: [Your Name]
Submission Date: [Date]
Course: Embedded AI - Week 3
Due Date: January 1, 2025
