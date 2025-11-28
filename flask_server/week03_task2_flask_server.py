from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Vehicle Control Server is running!",
        "endpoints": {
            "/": "Server status",
            "/ping": "Health check",
            "/move": "POST - Send movement commands"
        }
    })

# Ping endpoint for health checks
@app.route('/ping', methods=['GET'])
def ping():
    """Health check endpoint"""
    return jsonify({
        "status": "alive",
        "message": "Flask server is running",
        "timestamp": datetime.datetime.now().isoformat()
    }), 200

# Move endpoint for vehicle control
@app.route('/move', methods=['POST'])
def move():
    """
    Endpoint to receive movement commands
    Expected JSON: {"direction": "forward/backward/left/right/stop", "speed": 0-255}
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate that data exists
        if not data:
            return jsonify({
                "status": "error",
                "message": "No JSON data received"
            }), 400
        
        # Extract direction and speed
        direction = data.get('direction', 'unknown')
        speed = data.get('speed', 0)
        
        # Print command to console (simulating vehicle control)
        print(f"[VEHICLE COMMAND RECEIVED] Direction: {direction}, Speed: {speed}")
        
        # In future weeks, this is where you would send the command to Arduino
        # Example: send_to_arduino(direction, speed)
        
        # Return success response
        return jsonify({
            "status": "ok",
            "message": "Command received",
            "direction": direction,
            "speed": speed,
            "timestamp": datetime.datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    print("=" * 50)
    print("🚗 Vehicle Control Flask Server Starting...")
    print("=" * 50)
    print("Server will run on: http://127.0.0.1:5001")
    print("Available endpoints:")
    print("  - GET  /         : Server status")
    print("  - GET  /ping     : Health check")
    print("  - POST /move     : Send movement commands")
    print("=" * 50)
    
    # Run the Flask app
    app.run(
        host='0.0.0.0',  # Listen on all network interfaces
        port=5001,
        debug=True
    )
