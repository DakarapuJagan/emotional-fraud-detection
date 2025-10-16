"""
Automated ngrok setup script for FAD
This script helps you download and configure ngrok
"""

import os
import sys
import subprocess
import webbrowser
import time

def print_header():
    print("=" * 60)
    print("\n  🌐 FAD - Public URL Setup\n")
    print("=" * 60)
    print()

def check_ngrok_installed():
    """Check if ngrok is installed"""
    try:
        result = subprocess.run(['ngrok', 'version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print("✅ ngrok is already installed!")
            print(f"   Version: {result.stdout.strip()}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    print("❌ ngrok is not installed")
    return False

def guide_ngrok_installation():
    """Guide user through ngrok installation"""
    print("\n📥 Let's install ngrok!\n")
    print("Step 1: Download ngrok")
    print("   Opening download page in your browser...")
    
    webbrowser.open('https://ngrok.com/download')
    time.sleep(2)
    
    print("\n   Please:")
    print("   1. Download ngrok for Windows")
    print("   2. Extract the ngrok.exe file")
    print("   3. Move it to this folder:")
    print(f"      {os.getcwd()}")
    print("\n   Or move it to: C:\\Windows\\System32\\")
    
    input("\nPress Enter after you've downloaded and extracted ngrok...")

def guide_ngrok_signup():
    """Guide user through ngrok signup"""
    print("\n📝 Step 2: Create ngrok account (FREE)\n")
    print("   Opening signup page in your browser...")
    
    webbrowser.open('https://dashboard.ngrok.com/signup')
    time.sleep(2)
    
    print("\n   Please:")
    print("   1. Sign up with email or Google")
    print("   2. Copy your auth token from the dashboard")
    
    input("\nPress Enter after you've signed up...")

def configure_ngrok():
    """Configure ngrok with auth token"""
    print("\n🔑 Step 3: Configure ngrok\n")
    print("   You should see your auth token on the ngrok dashboard")
    print("   It looks like: 2abc123def456ghi789jkl")
    print()
    
    auth_token = input("   Paste your auth token here: ").strip()
    
    if not auth_token:
        print("\n❌ No token provided!")
        return False
    
    try:
        result = subprocess.run(['ngrok', 'config', 'add-authtoken', auth_token],
                              capture_output=True,
                              text=True,
                              timeout=10)
        
        if result.returncode == 0:
            print("\n✅ ngrok configured successfully!")
            return True
        else:
            print(f"\n❌ Configuration failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"\n❌ Error configuring ngrok: {e}")
        return False

def start_fad_server():
    """Start FAD server"""
    print("\n🚀 Step 4: Starting FAD server...\n")
    
    try:
        # Check if app.py exists
        if os.path.exists('app.py'):
            app_file = 'app.py'
        else:
            print("❌ Could not find app.py")
            return None
        
        print(f"   Starting {app_file}...")
        
        # Start server in background
        if sys.platform == 'win32':
            process = subprocess.Popen(['python', app_file],
                                     creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            process = subprocess.Popen(['python', app_file])
        
        print("✅ FAD server started!")
        print("   Waiting for server to initialize...")
        time.sleep(5)
        
        return process
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return None

def start_ngrok_tunnel():
    """Start ngrok tunnel"""
    print("\n🌐 Step 5: Creating public URL...\n")
    
    try:
        print("   Starting ngrok tunnel...")
        print("   This will show your public URL\n")
        print("=" * 60)
        print("\n   Press Ctrl+C to stop the tunnel\n")
        print("=" * 60)
        print()
        
        # Start ngrok
        subprocess.run(['ngrok', 'http', '5000'])
        
    except KeyboardInterrupt:
        print("\n\n✅ Tunnel stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting ngrok: {e}")

def main():
    """Main setup function"""
    print_header()
    
    # Check if ngrok is installed
    if not check_ngrok_installed():
        guide_ngrok_installation()
        
        # Check again after installation
        if not check_ngrok_installed():
            print("\n❌ ngrok still not found!")
            print("   Please make sure ngrok.exe is in your PATH")
            print("   or in the current directory")
            input("\nPress Enter to exit...")
            return
    
    # Check if already configured
    try:
        result = subprocess.run(['ngrok', 'config', 'check'],
                              capture_output=True,
                              text=True,
                              timeout=5)
        
        if 'authtoken' not in result.stdout.lower():
            guide_ngrok_signup()
            if not configure_ngrok():
                print("\n❌ Setup failed!")
                input("\nPress Enter to exit...")
                return
    except:
        guide_ngrok_signup()
        if not configure_ngrok():
            print("\n❌ Setup failed!")
            input("\nPress Enter to exit...")
            return
    
    # Start FAD server
    server_process = start_fad_server()
    if not server_process:
        print("\n❌ Could not start FAD server!")
        input("\nPress Enter to exit...")
        return
    
    # Start ngrok tunnel
    try:
        start_ngrok_tunnel()
    finally:
        # Cleanup
        if server_process:
            print("\n🛑 Stopping FAD server...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except:
                server_process.kill()
    
    print("\n✅ Setup complete!")
    print("\nTo run again, just execute:")
    print("   python setup_ngrok.py")
    print("\nOr use the batch file:")
    print("   create_public_url.bat")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✅ Setup cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    
    input("\nPress Enter to exit...")
