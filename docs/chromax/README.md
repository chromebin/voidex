# Chromax Browser

**Chromax** is a custom Chromium browser with **native fingerprint protection** built directly into the browser engine at the C++ source code level.

## 🎯 What is Chromax?

Chromax is a modified version of Chromium that provides undetectable browser fingerprint protection. Unlike browser extensions or JavaScript injection, Chromax's protection is built into the browser engine itself, making it impossible to detect.

## ✨ Key Features

- **Native Implementation** - Fingerprint protection built into Chromium's C++ source code
- **Undetectable** - No `navigator.webdriver`, functions show "[native code]"
- **Command-Line Control** - Configure via simple flags
- **Universal** - Works with Puppeteer, Selenium, Playwright, or standalone
- **Fast** - Native C++ performance, zero JavaScript overhead
- **Complete** - Protects Canvas, WebGL, Screen, User-Agent, Timezone, Geolocation, and more

## 🚀 Quick Start

### Installation

1. Download ChromaxSetup.exe from [Downloads](../../DOWNLOADS.md)
2. Run the installer
3. Chromax will be installed to: `C:\Users\[username]\AppData\Local\Chromax\chrome.exe`

### Basic Usage

**Launch with fingerprint protection:**

```bash
"%LOCALAPPDATA%\Chromax\chrome.exe" ^
  --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" ^
  --fingerprint-platform=Win32 ^
  --fingerprint-screen-resolution=1920x1080 ^
  --fingerprint-canvas-mode=noise ^
  --fingerprint-webgl-meta-mode=mask
```

## 🎭 Fingerprint Protection

Chromax protects against all major fingerprinting techniques:

- **Canvas Fingerprinting** - Noise injection at engine level
- **WebGL Fingerprinting** - Vendor/renderer masking + image hash protection
- **Screen Resolution** - Native screen API override
- **User-Agent** - Full UA and UA-CH (Client Hints) override
- **Timezone** - IANA timezone control
- **Geolocation** - Custom GPS coordinates
- **Hardware Spoofing** - CPU cores, device memory override
- **Platform** - navigator.platform control

## 🤖 Use Cases

### 1. Privacy Protection
Browse the web without being tracked by fingerprinting scripts.

### 2. Web Automation
Use with Puppeteer, Selenium, or Playwright to bypass anti-bot detection.

### 3. Testing & Development
Test websites with different browser fingerprints.

### 4. Research
Study fingerprinting techniques and anti-detection methods.

## 📚 Documentation

- **[Fingerprint Guide](./FINGERPRINT_GUIDE.md)** - Complete flag reference
- **[Quick Start](./QUICK_START.md)** - Get started in 5 minutes
- **[Why Native?](./WHY_NATIVE.md)** - Technical comparison with extensions

## 🔧 Integration Examples

- **[Node.js + Puppeteer](../../examples/chromax-standalone/nodejs-puppeteer-example/)** - Full automation example
- **[Python + Selenium](../../examples/chromax-standalone/python-selenium-example/)** - Full automation example
- **[Examples Overview](../../examples/README.md)** - All examples

## 🎯 Two Ways to Use Chromax

### Option 1: With Voidex Launcher (GUI)
Use the Voidex desktop application for easy profile management with a graphical interface.

**👉 [See Voidex User Guide](../voidex/USER_GUIDE.md)**

### Option 2: Standalone Scripts
Use Chromax directly in your Node.js or Python scripts for maximum flexibility.

**👉 [See Examples](../../examples/chromax-standalone/)**

## 🔒 Security & Privacy

- **No Telemetry** - All Google telemetry removed
- **No Sync** - Chrome Sync disabled
- **No Auto-Update** - Auto-update disabled
- **Privacy-First** - Built with privacy in mind
- **Proprietary** - Advanced native protection technology

## 📄 License

Proprietary License - Free for personal use. Commercial use requires a license.

---

**Ready to get started?** Download Chromax from the [Downloads page](../../DOWNLOADS.md)!
