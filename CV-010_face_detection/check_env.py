import sys
import numpy
import cv2
import os

print('Python version:', sys.version)
print('NumPy version:', numpy.__version__)
print('OpenCV version:', cv2.__version__)

# Check static directory
static_dir = 'static'
if os.path.exists(static_dir):
    print(f'\n[INFO] Directory "{static_dir}" exists')
    files = os.listdir(static_dir)
    if files:
        print(f'Files in static/: {files}')
    else:
        print('No files in static/ directory')
else:
    print(f'\n[ERROR] Directory "{static_dir}" does not exist!')
    sys.exit(1)

# Test face detection
print('\n[INFO] Testing face detection...')
try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if not face_cascade.empty():
        print('[OK] Face cascade classifier loaded successfully')
    else:
        print('[ERROR] Failed to load face cascade classifier')
        sys.exit(1)
    
    # Test with a sample image if exists
    test_image = 'test.jpg'
    if os.path.exists(test_image):
        img = cv2.imread(test_image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        print(f'Found {len(faces)} faces in test image')
    else:
        print('No test.jpg image found - skipping detection test')
        
except Exception as e:
    print(f'[ERROR] Face detection test failed: {str(e)}')
    sys.exit(1)

print('\n[SUCCESS] All tests passed!')