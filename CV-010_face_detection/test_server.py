import os
import sys
import subprocess
import time
import requests
import socket

def check_port(port):
    """Check if port is available"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) != 0

def test_server():
    """Test server startup and basic functionality"""
    print("[TEST] Starting server test...")
    
    # Check port 5000
    if not check_port(5000):
        print("[ERROR] Port 5000 is already in use. Please stop the process first.")
        return False
    
    # Start server in background
    print("[TEST] Starting server...")
    process = subprocess.Popen([
        'python', 'app.py'
    ], cwd='.', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Wait for server to start
    time.sleep(3)
    
    try:
        # Test if server is responsive
        print("[TEST] Testing server connection...")
        response = requests.get('http://localhost:5000', timeout=5)
        if response.status_code == 200:
            print("[SUCCESS] Server is running and accessible")
        else:
            print(f"[ERROR] Server returned status code: {response.status_code}")
            process.terminate()
            return False
        
        # Test upload endpoint
        print("[TEST] Testing upload endpoint...")
        if os.path.exists('input.jpg'):
            with open('input.jpg', 'rb') as f:
                files = {'file': f}
                upload_response = requests.post('http://localhost:5000/upload', files=files, timeout=10)
                
            if upload_response.status_code == 200:
                result = upload_response.json()
                print(f"[SUCCESS] Face detection test passed. Found {result.get('count', 0)} faces.")
            else:
                print(f"[ERROR] Upload failed with status code: {upload_response.status_code}")
                print(f"Response: {upload_response.text}")
                process.terminate()
                return False
        else:
            print("[WARNING] input.jpg not found. Skipping upload test.")
            
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server. Is it running?")
        process.terminate()
        return False
    except requests.exceptions.Timeout:
        print("[ERROR] Server timeout. The server might be stuck.")
        process.terminate()
        return False
    except Exception as e:
        print(f"[ERROR] Test failed: {str(e)}")
        process.terminate()
        return False
    
    # Clean up
    process.terminate()
    print("[TEST] Test completed successfully!")
    return True

if __name__ == '__main__':
    test_server()