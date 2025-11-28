import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Remote Vehicle Control Panel",
    page_icon="🚗",
    layout="centered"
)

# Title
st.title("🚗 Remote Vehicle Control Panel")
st.markdown("Control your vehicle remotely through this interface")

# Flask server URL configuration
# You can switch between local and deployed server
USE_DEPLOYED_SERVER = st.sidebar.checkbox("Use Deployed Server", value=False)

if USE_DEPLOYED_SERVER:
    FLASK_URL = "https://embedded-ai-chatbot.onrender.com"
else:
    FLASK_URL = "http://127.0.0.1:5001"

st.sidebar.info(f"**Connected to:** {FLASK_URL}")

# Speed control slider
st.subheader("Speed Control")
speed = st.slider("Select Speed (0-255)", min_value=0, max_value=255, value=128, step=1)
st.write(f"Current Speed: **{speed}**")

st.divider()

# Function to send command to Flask server
def send_command(direction, speed_value):
    """Send movement command to Flask server"""
    try:
        # Prepare the payload
        payload = {
            "direction": direction,
            "speed": speed_value
        }
        
        # Send POST request to Flask server
        response = requests.post(
            f"{FLASK_URL}/move",
            json=payload,
            timeout=5,
            headers={"Content-Type": "application/json"}
        )
        
        # Check if request was successful
        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ Command sent successfully: {direction.upper()} at speed {speed_value}")
            return True
        else:
            st.error(f"❌ Error: Server returned status code {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        st.error(f"❌ Connection Error: Cannot connect to Flask server at {FLASK_URL}")
        st.info("💡 Make sure the Flask server is running!")
        return False
    except requests.exceptions.Timeout:
        st.error("❌ Timeout Error: Server took too long to respond")
        return False
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
        return False

# Movement controls
st.subheader("Movement Controls")

# Create columns for button layout
col1, col2, col3 = st.columns([1, 1, 1])

# Forward button (centered)
with col2:
    if st.button("⬆️ Forward", use_container_width=True, type="primary"):
        send_command("forward", speed)

# Left and Right buttons
col_left, col_middle, col_right = st.columns([1, 1, 1])

with col_left:
    if st.button("⬅️ Left", use_container_width=True):
        send_command("left", speed)

with col_right:
    if st.button("➡️ Right", use_container_width=True):
        send_command("right", speed)

# Backward button (centered)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬇️ Backward", use_container_width=True):
        send_command("backward", speed)

st.divider()

# Stop button (full width, different color)
if st.button("🛑 STOP", use_container_width=True, type="secondary"):
    send_command("stop", 0)

st.divider()

# Test connection button
st.subheader("Server Status")
if st.button("🔍 Test Connection", use_container_width=True):
    try:
        # Try to ping the server (if /ping endpoint exists)
        response = requests.get(f"{FLASK_URL}/ping", timeout=5)
        if response.status_code == 200:
            st.success("✅ Flask server is online and responding!")
        else:
            st.warning(f"⚠️ Server responded with status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error(f"❌ Cannot connect to Flask server at {FLASK_URL}")
        st.info("""
        **Troubleshooting:**
        1. Make sure Flask server is running
        2. Check if Flask is running on port 5001
        3. If using deployed server, check the Render URL
        """)
    except Exception as e:
        st.error(f"❌ Error testing connection: {str(e)}")

# Sidebar with additional info
with st.sidebar:
    st.header("Instructions")
    st.markdown("""
    **How to use:**
    1. Adjust speed with the slider
    2. Click direction buttons to move
    3. Click STOP to halt the vehicle
    
    **Controls:**
    - ⬆️ Forward: Move ahead
    - ⬇️ Backward: Move back
    - ⬅️ Left: Turn left
    - ➡️ Right: Turn right
    - 🛑 Stop: Emergency stop
    """)
    
    st.divider()
    
    st.header("Server Configuration")
    st.markdown(f"""
    **Flask Server URL:**  
    `{FLASK_URL}`
    
    Toggle "Use Deployed Server" above to switch between local and cloud server.
    """)
    
    st.divider()
    
    st.caption("🚗 Embedded AI - Week 3 Task 2")
