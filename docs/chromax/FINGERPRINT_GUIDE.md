# Chromax - Native Fingerprint Protection Guide

**Chromax** is a custom Chromium browser with **native fingerprint protection** built directly into the browser engine. No extensions, no JavaScript injection - just pure, native fingerprint control via command-line flags.

## 🎯 Features

- **Native Implementation**: All fingerprint protection is built into Chromium's source code
- **Command-Line Control**: Configure fingerprints via simple command-line flags
- **Consistent & Reliable**: Fingerprints remain consistent across page reloads and navigation
- **No Detection**: Cannot be detected by anti-bot systems (no `navigator.webdriver`, no extension artifacts)
- **Full Coverage**: Protects Canvas, WebGL, Screen, User-Agent, Timezone, Geolocation, and more
- **Automation-Friendly**: Works seamlessly with Puppeteer, Selenium, Playwright

## 🚀 Quick Start

### Node.js Example

```javascript
const { spawn } = require('child_process');

const chromium = spawn('C:\\Users\\[username]\\AppData\\Local\\Chromax\\chrome.exe', [
  '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
  '--fingerprint-platform=Win32',
  '--fingerprint-screen-resolution=1920x1080',
  '--fingerprint-timezone=America/New_York',
  '--fingerprint-webgl-meta-mode=mask',
  '--fingerprint-webgl-vendor=Intel Inc.',
  '--fingerprint-webgl-renderer=Intel(R) Iris(R) Xe Graphics',
  '--fingerprint-canvas-mode=noise',
  '--fingerprint-canvas-seed=my-unique-seed',
  'https://browserleaks.com/canvas'
]);
```

### Python Example

```python
import subprocess

subprocess.Popen([
    r'C:\Users\[username]\AppData\Local\Chromax\chrome.exe',
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    '--fingerprint-platform=Win32',
    '--fingerprint-screen-resolution=1920x1080',
    '--fingerprint-timezone=America/New_York',
    '--fingerprint-webgl-meta-mode=mask',
    '--fingerprint-webgl-vendor=Intel Inc.',
    '--fingerprint-canvas-mode=noise',
    'https://browserleaks.com/canvas'
])
```

## 📚 Available Fingerprint Flags

### User Agent & Platform
```bash
--user-agent=<string>                    # Custom User-Agent string
--fingerprint-platform=<string>          # navigator.platform (Win32, MacIntel, etc.)
--fingerprint-ua-ch-json=<json>          # User-Agent Client Hints (UA-CH)
```

### Screen & Display
```bash
--fingerprint-screen-resolution=<WxH>    # Screen resolution (e.g., 1920x1080)
```

### Hardware
```bash
--fingerprint-cpu-cores=<number>         # navigator.hardwareConcurrency
--fingerprint-device-memory=<number>     # navigator.deviceMemory (GB)
```

### Locale & Timezone
```bash
--fingerprint-timezone=<iana>            # IANA timezone (e.g., America/New_York)
--fingerprint-accept-language=<string>   # Accept-Language header
```

### WebGL Protection
```bash
--fingerprint-webgl-meta-mode=<mode>     # Mode: mask | real | off
--fingerprint-webgl-vendor=<string>      # UNMASKED_VENDOR_WEBGL
--fingerprint-webgl-renderer=<string>    # UNMASKED_RENDERER_WEBGL
```

### WebGL Image Protection
```bash
--fingerprint-webgl-image-mode=<mode>    # Mode: off | noise | block
--fingerprint-webgl-image-seed=<string>  # Seed for noise generation
```

### Canvas Protection
```bash
--fingerprint-canvas-mode=<mode>         # Mode: off | noise | block
--fingerprint-canvas-seed=<string>       # Seed for noise generation
```

### Geolocation
```bash
--fingerprint-geolocation-mode=<mode>    # Mode: prompt | allow | block
--fingerprint-geolocation-lat=<number>   # Latitude
--fingerprint-geolocation-lon=<number>   # Longitude
--fingerprint-geolocation-accuracy=<n>   # Accuracy in meters
```

### ClientRects, AudioContext, Media Devices, Fonts, WebGPU, Speech Voices, Device Name

```bash
# ClientRects - getClientRects() / getBoundingClientRect() fingerprint protection
--fingerprint-client-rects-mode=<mode>   # Mode: off | noise | block

# AudioContext - AudioContext fingerprint protection
--fingerprint-audio-context-mode=<mode>   # Mode: off | noise | block
--fingerprint-audio-context-seed=<string> # Seed for noise (when mode=noise)

# Mask Media Devices - navigator.mediaDevices.enumerateDevices() masking
--fingerprint-mask-media-devices=<mode>   # Mode: off | mask

# Fonts Configuration - Font list override
--fingerprint-fonts-config=<json>         # JSON array of font names to report

# WebGPU - WebGPU adapter/vendor fingerprint masking
--fingerprint-webgpu-mode=<mode>          # Mode: off | mask
--fingerprint-webgpu-vendor=<string>      # Vendor string (when mode=mask)
--fingerprint-webgpu-architecture=<string> # Architecture string (when mode=mask)

# Speech Voices - speechSynthesis.getVoices() override
--fingerprint-speech-voices=<mode>        # Mode: off | mask
--fingerprint-speech-voices-config=<json> # JSON array of voice configs (when mode=mask)

# Device Name - navigator.deviceName / device info override
--fingerprint-device-name=<string>       # Custom device name string
```

## 🔧 Complete Examples

See the [`examples/chromax-standalone/`](../../examples/chromax-standalone/) directory for complete, working examples:

- **[nodejs-puppeteer-example](../../examples/chromax-standalone/nodejs-puppeteer-example/)** - Puppeteer automation
- **[python-selenium-example](../../examples/chromax-standalone/python-selenium-example/)** - Selenium automation
- **[README.md](../../examples/README.md)** - Detailed documentation

## 🎭 Fingerprint Profiles

### Windows 10 Desktop
```bash
chrome.exe \
  --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36" \
  --fingerprint-platform="Win32" \
  --fingerprint-screen-resolution="1920x1080" \
  --fingerprint-timezone="America/New_York" \
  --fingerprint-cpu-cores=8 \
  --fingerprint-device-memory=8 \
  --fingerprint-webgl-meta-mode=mask \
  --fingerprint-webgl-vendor="Intel Inc." \
  --fingerprint-webgl-renderer="Intel(R) Iris(R) Xe Graphics" \
  --fingerprint-canvas-mode=noise \
  --fingerprint-canvas-seed="win10-profile-001"
```

### macOS Desktop
```bash
chrome \
  --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36" \
  --fingerprint-platform="MacIntel" \
  --fingerprint-screen-resolution="2560x1440" \
  --fingerprint-timezone="America/Los_Angeles" \
  --fingerprint-cpu-cores=8 \
  --fingerprint-device-memory=16 \
  --fingerprint-webgl-meta-mode=mask \
  --fingerprint-webgl-vendor="Apple Inc." \
  --fingerprint-webgl-renderer="Apple M1" \
  --fingerprint-canvas-mode=noise \
  --fingerprint-canvas-seed="mac-profile-001"
```

### Linux Desktop
```bash
chrome \
  --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36" \
  --fingerprint-platform="Linux x86_64" \
  --fingerprint-screen-resolution="1920x1080" \
  --fingerprint-timezone="Europe/London" \
  --fingerprint-cpu-cores=4 \
  --fingerprint-device-memory=8 \
  --fingerprint-webgl-meta-mode=mask \
  --fingerprint-webgl-vendor="Mesa" \
  --fingerprint-webgl-renderer="Mesa DRI Intel(R) UHD Graphics" \
  --fingerprint-canvas-mode=noise \
  --fingerprint-canvas-seed="linux-profile-001"
```

## 🧪 Testing Your Fingerprint

Test your custom fingerprint at these sites:

- **Canvas**: https://browserleaks.com/canvas
- **WebGL**: https://browserleaks.com/webgl
- **General**: https://whoer.net
- **Comprehensive**: https://pixelscan.net
- **IP/Location**: https://iphey.com

## 🤖 Automation Integration

### Puppeteer (Node.js)

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
await page.goto('https://example.com');
```

### Selenium (Python)

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
driver.get('https://example.com')
```

### Playwright (Node.js)

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch({
  executablePath: 'C:\\Users\\[username]\\AppData\\Local\\Chromax\\chrome.exe',
  args: [
    '--fingerprint-platform=Win32',
    '--fingerprint-screen-resolution=1920x1080',
    '--fingerprint-webgl-meta-mode=mask',
    '--fingerprint-canvas-mode=noise'
  ]
});
```

## 🏗️ How It Works

Unlike browser extensions or JavaScript injection, Chromax modifies the browser engine itself:

1. **Native Patches** - Chromium source code is patched to add fingerprint control
2. **Command-Line Flags** - New flags are added to configure fingerprints
3. **Engine-Level Override** - Browser APIs are overridden at the C++ level
4. **No JavaScript** - No `navigator.webdriver`, no extension artifacts
5. **Undetectable** - Appears as a normal Chrome browser

### Modified Components

- **Blink Rendering Engine**: Canvas, WebGL, Screen APIs
- **Content Layer**: Navigator properties, hardware info
- **Network Stack**: User-Agent, Accept-Language headers
- **Geolocation Service**: GPS coordinates override
- **Timezone Handler**: IANA timezone override

## 🔒 Security & Privacy

- **No Telemetry**: All Google telemetry removed
- **No Sync**: Chrome Sync disabled
- **No Updates**: Auto-update disabled
- **Privacy-First**: Built with privacy in mind

## ⚠️ Important Notes

1. **Consistency**: Use the same seed for canvas/webgl across sessions for consistent fingerprints
2. **Realism**: Match User-Agent with platform, screen resolution, and WebGL vendor
3. **Testing**: Always test your fingerprint before production use
4. **Installation**: Make sure Chromax is installed via [ChromaxSetup.exe](../../DOWNLOADS.md)

## 📄 License

Proprietary License - Free for personal use. Commercial use requires a license.

## 🤝 Feedback

We value your feedback! Please feel free to report bugs or suggest new features.

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Documentation**: See [examples/](../../examples/)
- **Downloads**: See [DOWNLOADS.md](../../DOWNLOADS.md)

## 🌟 Credits

Built with ❤️ by the Chromax Team

---

**Disclaimer**: This tool is for educational and privacy purposes only. Use responsibly and in accordance with applicable laws and terms of service.
