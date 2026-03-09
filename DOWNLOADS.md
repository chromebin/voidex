# Downloads

Get started with Chromax and Voidex by downloading the installers below.

## 📦 Available Downloads

### Chromax Browser
**Custom Chromium with Native Fingerprint Protection**

- **Download**: [ChromaxSetup.exe](https://github.com/chromebin/voidex/releases/latest/download/ChromaxSetup.exe)
- **Version**: 1.0.0
- **Size**: ~150 MB
- **Install Location**: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`

### Voidex Launcher
**GUI Application for Managing Chromax Profiles**

- **Download**: [VoidexSetup.exe](https://github.com/chromebin/voidex/releases/latest/download/VoidexSetup.exe)
- **Version**: 1.0.0
- **Size**: ~200 MB
- **Install Location**: `C:\Users\[username]\AppData\Local\Programs\Voidex\Voidex.exe`

## 🤔 Which One Should I Download?

### Download Both (Recommended)
**Best for most users**
- ✅ GUI profile manager (Voidex)
- ✅ Custom browser with fingerprint protection (Chromax)
- ✅ Easy to use, no coding required
- ✅ Perfect for privacy-focused browsing

### Download Chromax Only
**For developers and automation**
- ✅ Use with Node.js/Python scripts
- ✅ Integrate with Puppeteer/Selenium
- ✅ Command-line control
- ✅ No GUI needed

### Download Voidex Only
**Not recommended** - Voidex requires Chromax to function. Always install Chromax first.

## 💻 System Requirements

### Windows
- **OS**: Windows 10 (64-bit) or later
- **RAM**: 4 GB minimum, 8 GB recommended
- **Disk Space**: 500 MB free space
- **Processor**: Intel Core i3 or equivalent

### macOS
- **OS**: macOS 10.15 (Catalina) or later
- **RAM**: 4 GB minimum, 8 GB recommended
- **Disk Space**: 500 MB free space
- **Processor**: Intel or Apple Silicon

### Linux
- **OS**: Ubuntu 20.04+ or equivalent
- **RAM**: 4 GB minimum, 8 GB recommended
- **Disk Space**: 500 MB free space
- **Processor**: x86_64 architecture

## 📥 Installation Instructions

### Installing Chromax

1. **Download** ChromaxSetup.exe from the link above
2. **Run** the installer
3. **Follow** the installation wizard
4. **Verify** installation:
   - Open Command Prompt or Terminal
   - Run: `"%LOCALAPPDATA%\Chromax\chrome.exe" --version`
   - You should see the Chromax version number

**Default Installation Path:**
```
Windows: C:\Users\[username]\AppData\Local\Chromax\chrome.exe
macOS: /Applications/Chromax.app/Contents/MacOS/Chromax
Linux: /opt/chromax/chrome
```

### Installing Voidex

1. **Install Chromax first** (see above)
2. **Download** VoidexSetup.exe from the link above
3. **Run** the installer
4. **Follow** the installation wizard
5. **Launch** Voidex from Start Menu or Desktop shortcut
6. **Verify** Chromax detection:
   - Voidex should automatically detect Chromax at the default location
   - If not, you can manually set the path in Settings

**Default Installation Path:**
```
Windows: C:\Users\[username]\AppData\Local\Programs\Voidex\Voidex.exe
macOS: /Applications/Voidex.app
Linux: /opt/voidex/voidex
```

## 🚀 First-Time Setup

### For Voidex Launcher Users

1. **Launch Voidex** from Start Menu
2. **Create your first profile**:
   - Click "New Profile"
   - Enter profile name
   - Configure fingerprint settings (or use defaults)
   - Click "Save"
3. **Launch browser**:
   - Select your profile
   - Click "Launch Browser"
   - Test at https://browserleaks.com/canvas

### For Script/Automation Users

1. **Install Chromax** (see above)
2. **Choose your example**:
   - [Node.js + Puppeteer](./examples/chromax-standalone/nodejs-puppeteer-example/)
   - [Python + Selenium](./examples/chromax-standalone/python-selenium-example/)
3. **Follow the example README** for setup instructions
4. **Run your script** and test fingerprint protection

## 🔄 Updating

### Chromax Updates
- Download the latest ChromaxSetup.exe
- Run the installer (it will update your existing installation)
- Your settings and profiles are preserved

### Voidex Updates
- Download the latest VoidexSetup.exe
- Run the installer (it will update your existing installation)
- Your profiles and settings are preserved

## 🆘 Troubleshooting

### Chromax Not Found
**Problem**: Voidex can't find Chromax installation

**Solution**:
1. Verify Chromax is installed: Check `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`
2. In Voidex, go to Settings and manually set the Chromax path
3. Restart Voidex

### Installation Failed
**Problem**: Installer shows error or fails to complete

**Solution**:
1. Run installer as Administrator
2. Disable antivirus temporarily
3. Check you have enough disk space
4. Try downloading again (file may be corrupted)

### Browser Won't Launch
**Problem**: Clicking "Launch Browser" does nothing

**Solution**:
1. Check Chromax path is correct in Settings
2. Close any existing Chromax processes in Task Manager
3. Check the profile's user data directory isn't corrupted
4. Try creating a new profile

### Fingerprint Not Working
**Problem**: Fingerprint protection doesn't seem to apply

**Solution**:
1. Make sure you're using Chromax, not regular Chrome
2. Test at https://browserleaks.com/canvas to verify
3. Check your fingerprint settings in the profile
4. Try a different canvas seed value

## 📞 Support

- **Documentation**: [docs/](./docs/)
- **Examples**: [examples/](./examples/)
- **Issues**: [GitHub Issues](https://github.com/chromebin/voidex/issues)
- **Discussions**: [GitHub Discussions](https://github.com/chromebin/voidex/discussions)

## 📄 License

Both Chromax and Voidex are released under the MIT License - free to use for any purpose.

---

**Ready to get started?** Download the installers above and follow the setup guide!
