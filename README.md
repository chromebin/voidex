<div align="center">

# Chromax & Voidex                 <img align="right" src="https://visitor-badge.laobi.icu/badge?page_id=chromebin.voidex" />

### Native Browser Fingerprint Protection

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](#-license)
[![Node.js](https://img.shields.io/badge/node-%3E%3D14.0.0-brightgreen.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.7-blue.svg)](https://www.python.org/)
[![Support](https://img.shields.io/badge/Support-Sponsors-brightgreen.svg)](#-support-the-project)

[Downloads](./DOWNLOADS.md) • [Examples](./examples/) • [Documentation](./docs/)

---

**Native fingerprint protection built into Chromium's source code.**  
Undetectable. Fast. Private. Universal.

🎭 **Undetectable** • ⚡ **Fast** • 🔒 **Private** • 🌍 **Universal**

</div>

---

## 🎯 What is This Project?

This project provides **two products** for browser fingerprint protection:

### 1. Chromax Browser
**Custom Chromium with Native Fingerprint Protection**

Chromax is a modified Chromium browser with fingerprint protection built directly into the browser engine (C++ source code). Unlike extensions or JavaScript injection, Chromax's protection is truly undetectable.

- ✅ **Native Implementation** - Built into Chromium's C++ source
- ✅ **Command-Line Control** - Configure via simple flags
- ✅ **No Detection** - No `navigator.webdriver`, functions show "[native code]"
- ✅ **Universal** - Works with Puppeteer, Selenium, Playwright, or standalone

**Use Chromax when:**
- You want to write automation scripts (Node.js/Python)
- You need command-line control
- You're integrating with Puppeteer/Selenium
- You want maximum flexibility

**📥 [Download ChromaxSetup.exe](./DOWNLOADS.md)**

### 2. Voidex Launcher
**GUI Application for Managing Chromax Profiles**

Voidex is an Electron-based desktop application that makes it easy to manage multiple browser profiles with different fingerprints. No coding required.

![Voidex Profile Manager](./assets/voidex-screenshot-1.png)
*Voidex profile manager - Create and manage multiple browser profiles*

![Voidex Profile Editor](./assets/voidex-screenshot-2.png)
*Profile editor - Configure fingerprint settings with an intuitive GUI*

- ✅ **Easy Profile Management** - Create, edit, delete profiles
- ✅ **Visual Configuration** - GUI for all fingerprint settings
- ✅ **Proxy Support** - Built-in proxy bridge for SOCKS5/HTTP
- ✅ **No Coding** - Point and click interface

**Use Voidex when:**
- You want a GUI (no coding)
- You need to manage multiple profiles
- You want easy proxy configuration
- You prefer a GoLogin-like experience

**📥 [Download VoidexSetup.exe](./DOWNLOADS.md)**

**⚠️ Note:** Voidex requires Chromax to be installed first.

---

## 🤔 Which One Do I Need?

| Use Case | Download |
|----------|----------|
| **GUI profile manager, no coding** | Both (Chromax + Voidex) |
| **Automation scripts (Node.js/Python)** | Chromax only |
| **Privacy browsing with easy setup** | Both (Chromax + Voidex) |
| **Advanced automation with Puppeteer/Selenium** | Chromax only |

**👉 [See Downloads Page](./DOWNLOADS.md)** for installation instructions.

---

## 🚀 Quick Start

### Using Voidex Launcher (GUI)

1. **Download and install** both Chromax and Voidex from [Downloads](./DOWNLOADS.md)
2. **Launch Voidex** from Start Menu
3. **Create a profile**:
   - Click "New Profile"
   - Configure fingerprint settings
   - Click "Save"
4. **Launch browser** with your profile
5. **Test** at https://browserleaks.com/canvas

**👉 [See Voidex User Guide](./docs/voidex/USER_GUIDE.md)**

### Using Chromax with Scripts

**Node.js + Puppeteer:**

```javascript
const puppeteer = require('puppeteer-core');

const browser = await puppeteer.launch({
  executablePath: 'C:\\Users\\[username]\\AppData\\Local\\Chromax\\chrome.exe',
  args: [
    '--fingerprint-platform=Win32',
    '--fingerprint-screen-resolution=1920x1080',
    '--fingerprint-webgl-meta-mode=mask',
    '--fingerprint-canvas-mode=noise'
  ]
});

const page = await browser.newPage();
await page.goto('https://browserleaks.com/canvas');
```

**Python + Selenium:**

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r'C:\Users\[username]\AppData\Local\Chromax\chrome.exe'
options.add_argument('--fingerprint-platform=Win32')
options.add_argument('--fingerprint-screen-resolution=1920x1080')
options.add_argument('--fingerprint-webgl-meta-mode=mask')
options.add_argument('--fingerprint-canvas-mode=noise')

driver = webdriver.Chrome(options=options)
driver.get('https://browserleaks.com/canvas')
```

**👉 [See Complete Examples](./examples/chromax-standalone/)**

---

## 🎭 Fingerprint Protection Features

Chromax protects against all major fingerprinting techniques:

| Protection | Status | Method |
|------------|--------|--------|
| Canvas Fingerprinting | ✅ Protected | Noise injection at engine level |
| WebGL Fingerprinting | ✅ Protected | Vendor/renderer masking + image hash |
| Screen Resolution | ✅ Protected | Native screen API override |
| User-Agent | ✅ Protected | UA + UA-CH override |
| Timezone | ✅ Protected | IANA timezone override |
| Geolocation | ✅ Protected | GPS coordinate override |
| Hardware Info | ✅ Protected | CPU/memory spoofing |
| Platform | ✅ Protected | navigator.platform override |

**All protection is native** - implemented in C++, not JavaScript.

---

## 📚 Available Fingerprint Flags

Control fingerprints via command-line flags:

```bash
# User Agent & Platform
--user-agent=<string>
--fingerprint-platform=<string>
--fingerprint-ua-ch-json=<json>

# Screen & Hardware
--fingerprint-screen-resolution=<WxH>
--fingerprint-cpu-cores=<number>
--fingerprint-device-memory=<number>

# Locale & Timezone
--fingerprint-timezone=<iana>
--fingerprint-accept-language=<string>

# WebGL Protection
--fingerprint-webgl-meta-mode=<mask|real|off>
--fingerprint-webgl-vendor=<string>
--fingerprint-webgl-renderer=<string>
--fingerprint-webgl-image-mode=<off|noise|block>
--fingerprint-webgl-image-seed=<string>

# Canvas Protection
--fingerprint-canvas-mode=<off|noise|block>
--fingerprint-canvas-seed=<string>

# Geolocation
--fingerprint-geolocation-mode=<prompt|allow|block>
--fingerprint-geolocation-lat=<number>
--fingerprint-geolocation-lon=<number>
--fingerprint-geolocation-accuracy=<number>

# ClientRects, AudioContext, Media Devices, Fonts, WebGPU, Speech Voices, Device Name
--fingerprint-client-rects-mode=<off|noise|block>
--fingerprint-audio-context-mode=<off|noise|block>
--fingerprint-audio-context-seed=<string>
--fingerprint-mask-media-devices=<off|mask>
--fingerprint-fonts-config=<json>
--fingerprint-webgpu-mode=<off|mask>
--fingerprint-webgpu-vendor=<string>
--fingerprint-webgpu-architecture=<string>
--fingerprint-speech-voices=<off|mask>
--fingerprint-speech-voices-config=<json>
--fingerprint-device-name=<string>
```

**👉 [See Complete Flag Reference](./docs/chromax/FINGERPRINT_GUIDE.md)**

---

## 🏗️ How It Works

Unlike browser extensions or JavaScript injection, Chromax uses a **custom Chromium build** with native fingerprint protection:

1. **Chromium Source Patches** - Browser engine patched at C++ level
2. **Command-Line Flags** - New flags added for fingerprint control
3. **Native API Override** - Browser APIs overridden at engine level
4. **No Detection** - No `navigator.webdriver` or extension artifacts
5. **Consistent** - Fingerprints persist across navigation and reloads

**Why Native Matters:**

| Feature | Browser Extensions | JS Injection | Chromax (Native) |
|---------|-------------------|--------------|------------------|
| Detectable | ❌ Yes | ❌ Yes | ✅ No |
| navigator.webdriver | ❌ Present | ❌ Present | ✅ Removed |
| Function .toString() | ❌ Modified | ❌ Modified | ✅ Native |
| Performance | ⚠️ Slower | ⚠️ Slower | ✅ Fast |
| Works in iframes | ⚠️ Limited | ⚠️ Limited | ✅ Perfect |

**👉 [Learn More About Native Protection](./docs/chromax/WHY_NATIVE.md)**

---

## 📚 Documentation

### For Chromax Browser
- **[Chromax Overview](./docs/chromax/README.md)** - What is Chromax?
- **[Fingerprint Guide](./docs/chromax/FINGERPRINT_GUIDE.md)** - Complete flag reference
- **[Quick Start](./docs/chromax/QUICK_START.md)** - Get started in 5 minutes
- **[Why Native?](./docs/chromax/WHY_NATIVE.md)** - Technical comparison

### For Voidex Launcher
- **[Voidex Overview](./docs/voidex/README.md)** - What is Voidex?
- **[User Guide](./docs/voidex/USER_GUIDE.md)** - How to use the GUI app

### Examples & Integration
- **[Examples Overview](./examples/README.md)** - All examples
- **[Node.js + Puppeteer](./examples/chromax-standalone/nodejs-puppeteer-example/)** - Puppeteer automation
- **[Python + Selenium](./examples/chromax-standalone/python-selenium-example/)** - Selenium automation
- **[Proxy Bridge](./examples/chromax-standalone/nodejs-proxy-bridge/)** - Proxy authentication helper

---

## 🧪 Testing Your Fingerprint

Test your custom fingerprint at:

- **Canvas**: https://browserleaks.com/canvas
- **WebGL**: https://browserleaks.com/webgl
- **General**: https://whoer.net
- **Comprehensive**: https://pixelscan.net
- **IP/Location**: https://iphey.com

---

## 🤖 Automation Integration

Chromax works seamlessly with popular automation tools:

- **Puppeteer** (Node.js)
- **Selenium** (Python, Java, C#, etc.)
- **Playwright** (Node.js, Python, Java, C#)
- **Any tool that supports custom Chrome binary**

See [examples/](./examples/) for integration code.

---

## 🔒 Security & Privacy

- **No Telemetry** - All Google telemetry removed
- **No Sync** - Chrome Sync disabled
- **No Auto-Update** - Auto-update disabled
- **Privacy-First** - Built with privacy in mind
- **Proprietary** - Advanced native protection technology

---

## 🤝 Feedback & Support

We value your feedback! Please feel free to:

- Report bugs or issues
- Suggest new features
- Request improvements
- Share your use cases

---

## 💖 Support the Project

Chromax and Voidex are actively developed and maintained. If you find this project valuable, please consider supporting its continued development.

### Why Support Matters

This project requires significant time and resources to:
- Maintain compatibility with the latest Chromium versions
- Develop new fingerprint protection features
- Provide support and documentation
- Test across different platforms and use cases

Currently, development is done part-time due to personal financial constraints. Your support would enable full-time dedicated development and faster feature releases.

### How to Support

**🏢 Business/Enterprise Support**
If you're using Chromax/Voidex in a commercial environment and would like:
- Priority support and faster response times
- Custom feature development
- Consulting and integration services
- Enterprise licensing options
- Service Level Agreement (SLA)

Please contact: [ihor.z.1987@gmail.com](mailto:ihor.z.1987@gmail.com)

**💼 Investment Opportunities**
Looking for investors to help scale development and bring this project to full-time focus. If you're interested in supporting the long-term growth of Chromax/Voidex, please reach out to discuss partnership opportunities.

**⭐ Other Ways to Help**
- Star the repository on GitHub
- Share the project with others who might benefit
- Provide feedback and feature suggestions
- Report bugs and issues

### Sponsorship Tiers

| Tier | Monthly | Benefits |
|------|---------|----------|
| 🥉 **Supporter** | $10 | Priority email support, Name in supporters list |
| 🥈 **Contributor** | $50 | Above + Priority issue responses, Feature voting |
| 🥇 **Sponsor** | $200 | Above + Monthly video call, Priority feature requests |
| 💎 **Enterprise** | $1,000+ | Above + Custom development, SLA support, Direct line |

Your support directly impacts the development speed and quality of Chromax and Voidex. Thank you for considering! 🙏

---

## 📄 License

Proprietary License - Free for personal use. Commercial use requires a license.

For licensing inquiries, please contact: [ihor.z.1987@gmail.com](mailto:ihor.z.1987@gmail.com)

---

<div align="center">

**Chromax & Voidex** - Undetectable by Design 🎭

Made with ❤️ for privacy and automation

[⭐ Star on GitHub](https://github.com/chromebin/voidex) • [🐛 Report Issue](https://github.com/chromebin/voidex/issues) • [💬 Discussions](https://github.com/chromebin/voidex/discussions)

</div>

---

**⚠️ Disclaimer**: This tool is for educational and privacy purposes only. Use responsibly and in accordance with applicable laws and terms of service.
