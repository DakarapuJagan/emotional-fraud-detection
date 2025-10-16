# 🔧 Fixing Common Errors in FAD

## Quick Error Fixes

### Error 1: Module Not Found

**Error Message:**
```
ModuleNotFoundError: No module named 'flask'
```

**Fix:**
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install flask flask-cors opencv-python pillow textblob scikit-learn pandas python-dotenv werkzeug numpy deepface tensorflow tf-keras
```

---

### Error 2: Port Already in Use

**Error Message:**
```
OSError: [WinError 10048] Only one usage of each socket address
```

**Fix Option 1 - Change Port:**
Edit `app_v2.py`, change last line:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed from 5000 to 5001
```

**Fix Option 2 - Kill Process:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill it (replace PID with actual number)
taskkill /PID [PID] /F
```

---

### Error 3: Camera Permission Error

**Error Message:**
```
NotAllowedError: Permission denied
```

**Fix:**
1. Close other apps using camera (Zoom, Teams, Skype)
2. Check browser permissions:
   - Chrome: Settings → Privacy → Camera
   - Allow for localhost
3. Try different browser
4. Restart browser

---

### Error 4: DeepFace Model Download

**Error Message:**
```
Exception: weight file could not be loaded
```

**Fix:**
This is normal on first run! DeepFace downloads AI models (~100-500MB).
- Wait 5-10 minutes
- Ensure internet connection
- Models download to: `C:\Users\surya\.deepface\weights`

---

### Error 5: TensorFlow/Keras Error

**Error Message:**
```
ValueError: You have tensorflow 2.18.0 and this requires tf-keras
```

**Fix:**
```bash
pip install tf-keras
```

---

### Error 6: Pandas Conflict

**Error Message:**
```
AttributeError: module 'pandas' has no attribute 'DataFrame'
```

**Fix:**
There's a conflicting `pandas.py` file. Rename it:
```bash
ren "C:\Users\surya\AppData\Local\Programs\Python\Python312\pandas.py" "pandas_old.py.bak"
```

---

### Error 7: Template Not Found

**Error Message:**
```
jinja2.exceptions.TemplateNotFound: index_v2.html
```

**Fix:**
Make sure file exists:
```
new peoject/
└── templates/
    └── index_v2.html
```

If missing, the file should be in the templates folder.

---

### Error 8: Static Files Not Loading

**Error Message:**
```
404 Not Found - /static/app_v2.js
```

**Fix:**
Check file structure:
```
new peoject/
└── static/
    ├── app_v2.js
    ├── styles.css
    └── manifest.json
```

---

### Error 9: CORS Error

**Error Message:**
```
Access to fetch blocked by CORS policy
```

**Fix:**
Already fixed in app_v2.py with:
```python
CORS(app, resources={r"/*": {"origins": "*"}})
```

If still issues, clear browser cache.

---

### Error 10: ngrok Not Found

**Error Message:**
```
'ngrok' is not recognized as an internal or external command
```

**Fix:**
1. Download ngrok from: https://ngrok.com/download
2. Extract ngrok.exe
3. Move to project folder OR
4. Add to system PATH

---

## 🔍 Diagnostic Script

Run this to check your setup:

```bash
python check_setup.py
```

This will check:
- Python version
- All dependencies
- File structure
- Port availability
- Camera access

---

## 🚀 Clean Start

If you have multiple errors, try a clean start:

### Step 1: Stop Everything
```bash
# Press Ctrl+C in all terminals
# Or close all command prompts
```

### Step 2: Clean Install
```bash
# Uninstall all packages
pip uninstall -y flask flask-cors opencv-python deepface tensorflow textblob scikit-learn pandas

# Reinstall fresh
pip install -r requirements.txt
```

### Step 3: Restart
```bash
python app_v2.py
```

---

## 📋 Checklist Before Running

- [ ] Python 3.8+ installed
- [ ] All dependencies installed
- [ ] No other app using port 5000
- [ ] Camera not in use by other apps
- [ ] Internet connection (for first run)
- [ ] All files in correct folders

---

## 🆘 Still Having Issues?

### Check Console Logs
Look for specific error messages in the terminal.

### Check Browser Console
1. Press F12
2. Go to Console tab
3. Look for errors (red text)

### Check File Paths
Make sure all files exist:
```bash
dir templates
dir static
```

### Check Python Version
```bash
python --version
```
Should be 3.8 or higher.

### Check Dependencies
```bash
pip list
```
Should show flask, deepface, tensorflow, etc.

---

## 💡 Common Solutions

### Solution 1: Restart Everything
```bash
# Close all terminals
# Close browser
# Restart computer
# Try again
```

### Solution 2: Use Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate
venv\Scripts\activate

# Install
pip install -r requirements.txt

# Run
python app_v2.py
```

### Solution 3: Try v1.0
If v2.0 has issues, try the original:
```bash
python app.py
```

---

## ✅ Verification Steps

After fixing errors:

1. **Test Server:**
   ```bash
   python app_v2.py
   ```
   Should show: "Running on http://127.0.0.1:5000"

2. **Test Browser:**
   Open: http://localhost:5000
   Should show FAD interface

3. **Test Permissions:**
   Click "Grant Permissions"
   Should ask for camera/microphone

4. **Test Camera:**
   Click "Start Camera"
   Should show video feed

5. **Test Analysis:**
   Click "Analyze"
   Should show emotion results

---

## 🎯 Quick Fix Commands

```bash
# Fix dependencies
pip install -r requirements.txt

# Fix port conflict
netstat -ano | findstr :5000
taskkill /PID [PID] /F

# Fix pandas conflict
ren "C:\Users\surya\AppData\Local\Programs\Python\Python312\pandas.py" "pandas_old.py.bak"

# Fix tf-keras
pip install tf-keras

# Clean restart
python app_v2.py
```

---

**Most errors are fixed by:**
1. Installing dependencies: `pip install -r requirements.txt`
2. Closing conflicting apps
3. Restarting the server

**Your FAD should work after these fixes! 🛡️**
