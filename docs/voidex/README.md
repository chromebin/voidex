# Voidex Launcher

**Voidex** is a desktop application that provides an easy-to-use GUI for managing browser profiles with Chromax's native fingerprint protection.

![Voidex Profile Manager](../../assets/voidex-screenshot-1.png)
*Voidex profile manager interface*

![Voidex Profile Editor](../../assets/voidex-screenshot-2.png)
*Profile editor with fingerprint configuration*

## 🎯 What is Voidex?

Voidex is an Electron-based desktop application that makes it easy to create and manage multiple browser profiles with different fingerprints. No coding required - just point and click.

## ✨ Key Features

- **Profile Management** - Create, edit, delete, and organize browser profiles
- **Visual Configuration** - GUI for all fingerprint settings
- **Proxy Support** - Built-in proxy bridge for SOCKS5/HTTP with authentication
- **Browser Integration** - Launch isolated Chromax instances with custom fingerprints
- **Data Persistence** - Profiles saved locally
- **Modern UI** - Clean, responsive interface

## 🚀 Quick Start

### Installation

1. **Install Chromax first** - Download ChromaxSetup.exe from [Downloads](../../DOWNLOADS.md)
2. **Download Voidex** - Download VoidexSetup.exe from [Downloads](../../DOWNLOADS.md)
3. **Run installer** - Follow the installation wizard
4. **Launch Voidex** - Open from Start Menu or Desktop shortcut

Voidex will be installed to: `C:\Users\[username]\AppData\Local\Programs\Voidex\Voidex.exe`

### First Launch

1. Voidex will automatically detect Chromax at: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`
2. If not found, you'll be prompted to set the path manually
3. Click "New Profile" to create your first profile

## 🎭 Features

### Profile Management
- Create unlimited profiles with different fingerprints
- Edit existing profiles
- Delete profiles you no longer need
- Organize profiles by use case

### Fingerprint Configuration
Configure all fingerprint parameters via GUI:
- User-Agent and Platform
- Screen Resolution
- Timezone and Language
- Canvas Protection (noise/block)
- WebGL Protection (mask/block)
- Geolocation Override
- Hardware Spoofing (CPU cores, memory)

### Proxy Support
Built-in proxy bridge system:
- **HTTP Proxies** - With or without authentication
- **SOCKS5 Proxies** - With or without authentication
- **Automatic Bridge** - Handles authentication automatically
- **Per-Profile Proxies** - Different proxy for each profile

### Browser Isolation
Each profile launches a separate Chromax process with:
- Isolated user data directory
- Custom fingerprint settings
- Independent cookies and storage
- No cross-profile contamination

## 📚 Documentation

- **[User Guide](./USER_GUIDE.md)** - Complete guide to using Voidex
- **[Chromax Documentation](../chromax/)** - Learn about the underlying browser

## 🎯 Use Cases

### 1. Privacy-Focused Browsing
Create profiles with different fingerprints for different websites.

### 2. Multi-Account Management
Manage multiple accounts on the same website without conflicts.

### 3. Testing & QA
Test websites with different browser fingerprints and configurations.

### 4. Easy Profile Switching
Quickly switch between different browser configurations.

## 🔧 Technical Details

### Architecture
- **Main Process** - Handles profile management, browser launching, proxy bridges
- **Renderer Process** - Manages the UI and user interactions
- **Preload Script** - Secure bridge between main and renderer processes

### Data Storage
- Uses `electron-store` for persistent profile storage
- Profiles stored locally in user's data directory
- Each profile gets a unique UUID
- Profile data: `%APPDATA%\Voidex\config.json`

### Proxy Bridge System
- Per-profile proxy bridge servers
- Automatic port assignment (starting from 8888)
- Handles SOCKS5/HTTP authentication
- Clean shutdown on browser close

## 🔒 Security & Privacy

- **Local Storage** - All data stored locally on your machine
- **No Telemetry** - No usage tracking or analytics
- **No Cloud Sync** - Your profiles stay on your device
- **Secure** - Advanced native protection technology

## 🤝 vs. Commercial Tools

Voidex provides similar functionality to commercial tools like GoLogin or Multilogin:

| Feature | GoLogin/Multilogin | Voidex |
|---------|-------------------|---------|
| Profile Management | ✅ | ✅ |
| Native Fingerprinting | ✅ | ✅ |
| Proxy Support | ✅ | ✅ |
| GUI Interface | ✅ | ✅ |
| Cost | $49-299/month | Free (Personal) |
| Native C++ Protection | ✅ | ✅ |

## 📄 License

Proprietary License - Free for personal use. Commercial use requires a license.

---

**Ready to get started?** Download Voidex from the [Downloads page](../../DOWNLOADS.md) and check out the [User Guide](./USER_GUIDE.md)!
