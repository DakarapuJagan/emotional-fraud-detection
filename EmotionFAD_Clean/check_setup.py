"""Quick diagnostic script for FAD"""
import sys
import os

print("="*60)
print("FAD - System Check")
print("="*60)

# Check Python version
print(f"\nPython Version: {sys.version}")
if sys.version_info < (3, 8):
    print("ERROR: Python 3.8+ required")
else:
    print("OK: Python version is good")

# Check dependencies
print("\nChecking dependencies...")
required = ['flask', 'cv2', 'deepface', 'textblob', 'PIL', 'numpy']
for module in required:
    try:
        __import__(module)
        print(f"  OK: {module}")
    except ImportError:
        print(f"  MISSING: {module}")

# Check files
print("\nChecking files...")
files = [
    'app.py',
    'templates/index.html',
    'static/app.js',
    'requirements.txt'
]
for file in files:
    if os.path.exists(file):
        print(f"  OK: {file}")
    else:
        print(f"  MISSING: {file}")

print("\n" + "="*60)
print("If any items show MISSING, install with:")
print("  pip install -r requirements.txt")
print("="*60)
