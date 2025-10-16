# 🌐 Creating Public URL for FAD

## Quick Setup (5 Minutes)

### Step 1: Install ngrok

1. **Download ngrok:**
   - Go to: https://ngrok.com/download
   - Click "Download for Windows"
   - Extract the `ngrok.exe` file

2. **Move ngrok.exe:**
   - Option A: Move to your project folder: `c:\Users\surya\OneDrive\Documents\new peoject\`
   - Option B: Move to `C:\Windows\System32\` (available everywhere)

### Step 2: Create Free Account

1. **Sign up:**
   - Go to: https://dashboard.ngrok.com/signup
   - Sign up with email or Google
   - It's completely FREE!

2. **Get your auth token:**
   - After signup, you'll see your auth token
   - Copy it (looks like: `2abc123def456ghi789jkl`)

### Step 3: Configure ngrok

Open Command Prompt and run:
```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE
```

Replace `YOUR_AUTH_TOKEN_HERE` with your actual token.

### Step 4: Create Public URL

**Option A: Use the automated script**
```bash
# Just double-click this file:
create_public_url.bat
```

**Option B: Manual method**
```bash
# Terminal 1: Start FAD
python app_v2.py

# Terminal 2: Start ngrok
ngrok http 5000
```

### Step 5: Share Your URL

ngrok will show something like:
```
Forwarding    https://abc123def.ngrok.io -> http://localhost:5000
```

**Share this URL:** `https://abc123def.ngrok.io`

Anyone can now access your FAD application from anywhere in the world!

---

## 🎯 Example URLs You'll Get

### Free ngrok (Random URL)
- `https://1a2b3c4d.ngrok.io`
- `https://xyz789.ngrok.io`
- Changes every time you restart

### Paid ngrok (Custom Domain)
- `https://fad.ngrok.io`
- `https://fraud-detection.ngrok.io`
- Same URL every time

---

## 📱 How Users Will Access

### Method 1: Direct URL
1. You share: `https://abc123.ngrok.io`
2. User opens in any browser
3. Clicks "Grant Permissions"
4. Uses FAD immediately

### Method 2: Install as App
1. User visits your URL
2. Browser shows "Install FAD"
3. User clicks Install
4. FAD appears as app icon
5. User searches "FAD" to open it

---

## 🔧 Troubleshooting

### Issue: "ngrok: command not found"

**Solution:**
1. Make sure ngrok.exe is in your project folder OR
2. Add ngrok to system PATH OR
3. Run from the folder where ngrok.exe is located

### Issue: "Failed to start tunnel"

**Solution:**
1. Check if you configured auth token:
   ```bash
   ngrok config add-authtoken YOUR_TOKEN
   ```
2. Make sure FAD server is running first
3. Check if port 5000 is available

### Issue: "ERR_NGROK_108"

**Solution:**
- Your auth token is invalid
- Get new token from: https://dashboard.ngrok.com/get-started/your-authtoken
- Configure again:
  ```bash
  ngrok config add-authtoken NEW_TOKEN
  ```

### Issue: URL changes every time

**Solution:**
- Free ngrok gives random URLs
- For permanent URL, upgrade to paid plan ($8/month)
- Or deploy to cloud (Render.com - free)

---

## 🚀 Alternative: Deploy to Cloud (Free & Permanent)

### Option 1: Render.com (Recommended)

1. **Create account:**
   - Go to: https://render.com
   - Sign up with GitHub

2. **Push code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "FAD application"
   git push
   ```

3. **Deploy on Render:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app_v2.py`
   - Click "Create Web Service"

4. **Get your URL:**
   - Render gives you: `https://fad-yourname.onrender.com`
   - This URL is permanent and free!

### Option 2: Heroku (Free Tier)

1. **Install Heroku CLI:**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Create Procfile:**
   ```
   web: python app_v2.py
   ```

3. **Deploy:**
   ```bash
   heroku login
   heroku create fad-fraud-detection
   git push heroku main
   ```

4. **Get your URL:**
   - `https://fad-fraud-detection.herokuapp.com`

---

## 💡 Recommendations

### For Testing/Demo (Use ngrok)
- ✅ Quick setup (5 minutes)
- ✅ No code changes needed
- ✅ Works immediately
- ⚠️ URL changes each restart
- ⚠️ Requires ngrok running

**Best for:** Quick demos, testing, temporary access

### For Production (Use Cloud)
- ✅ Permanent URL
- ✅ Always online
- ✅ No local server needed
- ✅ Free tier available
- ⚠️ Takes 10-15 minutes setup

**Best for:** Long-term use, multiple users, 24/7 access

---

## 📊 Comparison

| Feature | ngrok (Free) | ngrok (Paid) | Render.com | Heroku |
|---------|-------------|--------------|------------|--------|
| Setup Time | 5 min | 5 min | 15 min | 15 min |
| Cost | Free | $8/mo | Free | Free |
| URL Type | Random | Custom | Custom | Custom |
| Permanent | ❌ | ✅ | ✅ | ✅ |
| Always On | ❌ | ❌ | ✅ | ✅ |
| Local Server | Required | Required | Not needed | Not needed |

---

## ✅ Quick Start Checklist

### For ngrok:
- [ ] Download ngrok
- [ ] Sign up for account
- [ ] Get auth token
- [ ] Configure: `ngrok config add-authtoken TOKEN`
- [ ] Run: `create_public_url.bat`
- [ ] Share the URL!

### For Cloud (Render):
- [ ] Create Render account
- [ ] Push code to GitHub
- [ ] Create Web Service on Render
- [ ] Connect GitHub repo
- [ ] Deploy
- [ ] Share permanent URL!

---

## 🎉 You're Ready!

### To create public URL now:

**Easiest way:**
```bash
# Just double-click:
create_public_url.bat
```

**Manual way:**
```bash
# Terminal 1
python app_v2.py

# Terminal 2
ngrok http 5000
```

Then share the `https://` URL shown by ngrok!

---

## 📞 Need Help?

### ngrok Documentation
- https://ngrok.com/docs

### Render Documentation
- https://render.com/docs

### FAD Support
- Check README_V2.md
- Check TROUBLESHOOTING.md
- Review console logs

---

**Your FAD application will be accessible worldwide! 🌍**
