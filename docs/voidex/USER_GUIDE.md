# Voidex User Guide

Complete guide to using the Voidex desktop application for managing browser profiles with fingerprint protection.

![Voidex Profile Manager](../../assets/voidex-screenshot-1.png)
*Voidex main interface showing profile list*

![Voidex Profile Editor](../../assets/voidex-screenshot-2.png)
*Profile editor with all fingerprint configuration options*

## 📥 Installation

### Prerequisites

**Install Chromax first** - Voidex requires Chromax browser to function.

1. Download ChromaxSetup.exe from [Downloads](../../DOWNLOADS.md)
2. Run the installer
3. Chromax will be installed to: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`

### Installing Voidex

1. Download VoidexSetup.exe from [Downloads](../../DOWNLOADS.md)
2. Run the installer
3. Follow the installation wizard
4. Voidex will be installed to: `C:\Users\[username]\AppData\Local\Programs\Voidex\Voidex.exe`
5. Launch Voidex from Start Menu or Desktop shortcut

## 🚀 First Launch

When you first launch Voidex:

1. **Chromax Detection**:
   - Voidex will automatically detect Chromax at the default location
   - If not found, you'll see a prompt to set the path manually
   - Click "Browse" and navigate to: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`

2. **Welcome Screen**:
   - You'll see an empty profile list
   - Click "New Profile" or "Create Your First Profile" to get started

## 📝 Creating Your First Profile

### Step 1: Click "New Profile"

Click the "New Profile" button in the top toolbar or sidebar.

### Step 2: Basic Information

**Profile Name**: Give your profile a descriptive name (e.g., "Work Profile", "Shopping", "Testing")

### Step 3: Fingerprint Settings

#### User-Agent
- **Template**: Choose from pre-configured templates (Windows, macOS, Linux)
- **Custom**: Enter your own User-Agent string

#### Platform
Select the operating system to simulate:
- `Win32` - Windows
- `MacIntel` - macOS
- `Linux x86_64` - Linux

#### Screen Resolution
Choose from common resolutions:
- 1920x1080 (Full HD)
- 1366x768 (Laptop)
- 2560x1440 (2K)
- 3840x2160 (4K)
- Custom resolution

#### Timezone
Select your desired timezone (e.g., America/New_York, Europe/London)

#### Language
Set the browser language (e.g., en-US, en-GB, es-ES)

#### Canvas Protection
- **Off** - No canvas protection
- **Noise** - Add noise to canvas fingerprint (recommended)
- **Block** - Block canvas fingerprinting entirely

**Canvas Seed**: Enter a unique seed for noise generation (e.g., "profile-001")

#### WebGL Protection
- **Off** - No WebGL protection
- **Mask** - Mask WebGL vendor and renderer (recommended)
- **Block** - Block WebGL entirely

**WebGL Vendor**: e.g., "Intel Inc.", "Apple Inc.", "Mesa"
**WebGL Renderer**: e.g., "Intel(R) Iris(R) Xe Graphics", "Apple M1"

#### Hardware
- **CPU Cores**: Number of CPU cores to report (e.g., 4, 8, 16)
- **Device Memory**: RAM in GB (e.g., 4, 8, 16)

#### Geolocation
- **Mode**: prompt | allow | block
- **Latitude**: GPS latitude (e.g., 40.7128)
- **Longitude**: GPS longitude (e.g., -74.0060)
- **Accuracy**: Accuracy in meters (e.g., 10)

### Step 4: Proxy Configuration (Optional)

#### Proxy Mode
- **None** - No proxy
- **Custom** - Configure your own proxy

#### Proxy Type
- **Auto** - Automatic detection
- **HTTP** - HTTP proxy
- **SOCKS5** - SOCKS5 proxy (recommended for privacy)

#### Proxy Details
- **Host**: Proxy server IP or hostname
- **Port**: Proxy server port
- **Username**: Proxy authentication username (optional)
- **Password**: Proxy authentication password (optional)

**How Proxy Bridge Works:**
```
Your Profile → Proxy Bridge (localhost:8888) → Your Proxy → Internet
```

Voidex automatically creates a local proxy bridge that handles authentication for SOCKS5/HTTP proxies, since Chromium doesn't natively support authenticated SOCKS5 proxies.

### Step 5: Save Profile

Click "Save" to create your profile. It will appear in the sidebar.

## 🌐 Launching Browsers

### Launch a Browser

1. **Select a profile** from the sidebar
2. **Click "Launch Browser"** button
3. A new Chromax window will open with your fingerprint settings applied
4. The profile will show as "Active" in the sidebar

### Active Status

- **Active** (green) - Browser is currently running
- **Inactive** (gray) - Browser is closed

### Multiple Browsers

You can launch multiple profiles simultaneously. Each profile runs in its own isolated Chromax process.

## ✏️ Managing Profiles

### View Profile Details

Click on any profile in the sidebar to view:
- **Overview** - Basic information and status
- **Fingerprint** - Detailed fingerprint configuration
- **Proxy** - Proxy settings
- **Storage** - Cookie and storage information

### Edit Profile

1. Select a profile
2. Click "Edit" button
3. Modify any settings
4. Click "Save"

**Note**: Changes only apply to new browser sessions. Close and relaunch the browser to apply changes.

### Delete Profile

1. Select a profile
2. Click "Delete" button
3. Confirm deletion

**Warning**: This will delete the profile and all its browser data (cookies, history, etc.)

## 🔧 Advanced Features

### Custom User Data Directory

Each profile stores its browser data in:
```
C:\Users\[username]\AppData\Roaming\Voidex\profiles\[profile-id]\chrome-data
```

This includes:
- Cookies
- Local Storage
- Cache
- History
- Extensions (if installed)

### Proxy Bridge Ports

Proxy bridges are assigned ports automatically:
- First profile: 8888
- Second profile: 8889
- Third profile: 8890
- And so on...

You can see the assigned port in the profile's proxy settings.

### Environment Variables

You can override the Chromax path using an environment variable:

```cmd
set CHROMIUM_PATH=C:\custom\path\to\chrome.exe
```

Then restart Voidex.

## 🧪 Testing Your Fingerprint

After launching a browser with your profile:

1. Visit fingerprint testing sites:
   - https://browserleaks.com/canvas
   - https://browserleaks.com/webgl
   - https://whoer.net
   - https://pixelscan.net

2. Verify your settings:
   - Canvas fingerprint matches your seed
   - WebGL vendor/renderer matches your config
   - Screen resolution matches your config
   - User-Agent matches your config
   - Timezone matches your config

## 🆘 Troubleshooting

### Chromax Not Found

**Problem**: Voidex shows "Chromax not found" error

**Solution**:
1. Verify Chromax is installed: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`
2. In Voidex, go to Settings
3. Manually set the Chromax path
4. Restart Voidex

### Browser Won't Launch

**Problem**: Clicking "Launch Browser" does nothing

**Solution**:
1. Check Chromax path is correct in Settings
2. Close any existing Chromax processes:
   - Open Task Manager
   - End all "chrome.exe" processes
3. Try launching again
4. Check Windows Event Viewer for errors

### Fingerprint Not Applied

**Problem**: Fingerprint settings don't seem to work

**Solution**:
1. Make sure you're using Chromax, not regular Chrome
2. Test at https://browserleaks.com/canvas
3. Check your profile's fingerprint settings
4. Try a different canvas seed value
5. Close and relaunch the browser

### Proxy Not Working

**Problem**: Browser can't connect through proxy

**Solution**:
1. Verify proxy credentials are correct
2. Test proxy connection outside Voidex
3. Check proxy type (HTTP vs SOCKS5)
4. Look at Voidex console for proxy bridge errors
5. Try a different proxy bridge port

### Profile Data Corrupted

**Problem**: Profile won't load or browser crashes

**Solution**:
1. Close the browser
2. Delete the profile's user data:
   - Navigate to: `%APPDATA%\Voidex\profiles\[profile-id]\chrome-data`
   - Delete the folder
3. Relaunch the browser (fresh data will be created)

### Multiple Instances

**Problem**: Can't launch multiple profiles

**Solution**:
- Each profile should launch independently
- Make sure previous browser windows are fully closed
- Check Task Manager for lingering chrome.exe processes

## 💡 Pro Tips

### 1. Consistent Seeds
Use the same canvas/webgl seed for a profile across sessions to maintain consistent fingerprints.

### 2. Realistic Configurations
Match your User-Agent with platform, screen resolution, and WebGL vendor for realistic fingerprints.

### 3. Test Before Production
Always test your fingerprint at browserleaks.com before using for important tasks.

### 4. Profile Organization
Use descriptive profile names like:
- "Work - Windows 10"
- "Shopping - macOS"
- "Testing - Linux"

### 5. Proxy Rotation
For mobile proxies with IP rotation, use the "Change IP URL" feature to rotate IPs without restarting.

### 6. Backup Profiles
Voidex stores profiles in: `%APPDATA%\Voidex\config.json`
- Back up this file to save your profiles
- Restore by copying the file back

## 🔧 Settings

### Chromax Path
Set the path to your Chromax installation:
- Default: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`
- Custom: Browse to select a different location

### Startup Options
- Launch Voidex on system startup
- Minimize to system tray
- Remember window size and position

### Advanced
- Default proxy bridge starting port (default: 8888)
- Browser launch timeout
- Debug logging

## 📊 Profile Details Tabs

### Overview Tab
- Profile name and ID
- Active status
- Last launched time
- Browser version

### Fingerprint Tab
- All fingerprint settings
- User-Agent details
- Canvas/WebGL configuration
- Hardware settings

### Proxy Tab
- Proxy configuration
- Bridge status and port
- Connection test results

### Storage Tab
- User data directory path
- Disk space used
- Cookie count
- Clear data options

## 🔗 Integration with Scripts

While Voidex provides a GUI, you can also use Chromax directly in scripts:

**👉 [See Script Examples](../../examples/chromax-standalone/)**

## 📞 Support

- **User Guide**: You're reading it!
- **Chromax Documentation**: [docs/chromax/](../chromax/)
- **Examples**: [examples/](../../examples/)
- **Issues**: Open an issue on GitHub

## 📄 License

Proprietary License - Free for personal use. Commercial use requires a license.

---

**Need help?** Check the [Troubleshooting](#-troubleshooting) section above or open an issue on GitHub!
