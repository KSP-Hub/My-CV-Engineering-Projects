import os
print("Current working directory:", os.getcwd())
print("Files in configs directory:")
try:
    for file in os.listdir("D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/configs"):
        print(f"  {file}")
except Exception as e:
    print(f"Error listing directory: {e}")

print("\nTesting cascade file:")
try:
    with open("D:/Apps/GitHub/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection/configs/haarcascade_frontalface_default.xml", 'r') as f:
        content = f.read(200)
        print(f"First 200 chars: {content}")
except Exception as e:
    print(f"Error reading cascade file: {e}")