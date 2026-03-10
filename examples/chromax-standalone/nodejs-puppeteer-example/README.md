# Chromax + Puppeteer Example

Complete example of using Puppeteer with Chromax browser for automated testing and scraping with native fingerprint protection.

## 📋 Prerequisites

1. **Install Chromax** - Download ChromaxSetup.exe from [Downloads](../../../DOWNLOADS.md)
2. **Install Node.js** - Version 14.0.0 or higher

## 🚀 Installation

```bash
cd examples/chromax-standalone/nodejs-puppeteer-example
npm install
```

## 🎯 Usage

### Basic Usage

```bash
node index.js
```

The script will:
1. Launch Chromax with fingerprint protection
2. Test fingerprint settings
3. Open https://browserleaks.com/canvas
4. Keep browser open for manual testing

### Custom Chromax Path

If Chromax is not installed at the default location, set the environment variable:

```bash
# Windows (Command Prompt)
set CHROMIUM_PATH=C:\custom\path\to\chrome.exe
node index.js

# Windows (PowerShell)
$env:CHROMIUM_PATH="C:\custom\path\to\chrome.exe"
node index.js

# Linux/Mac
export CHROMIUM_PATH=/custom/path/to/chrome
node index.js
```

## ⚙️ Configuration

Edit `index.js` to customize fingerprint settings:

```javascript
const config = {
  chromiumPath: '...',  // Auto-detected
  
  fingerprint: {
    userAgent: 'Mozilla/5.0...',
    platform: 'Win32',
    screenResolution: '1920x1080',
    timezone: 'America/New_York',
    
    webgl: {
      mode: 'mask',
      vendor: 'Intel Inc.',
      renderer: 'Intel(R) Iris(R) Xe Graphics'
    },
    
    canvas: {
      mode: 'noise',
      seed: 'my-canvas-seed-456'
    }
  }
};
```

## 🔗 Proxy Support

### Without Authentication

```javascript
proxy: {
  enabled: true,
  server: 'http://proxy.example.com:8080'
}
```

### With Authentication

Use the [proxy bridge](../nodejs-proxy-bridge/) for authenticated proxies:

1. **Start proxy bridge** (in separate terminal):
```bash
cd ../nodejs-proxy-bridge
node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080 --port 9999
```

2. **Configure script** to use bridge:
```javascript
proxy: {
  enabled: true,
  server: 'http://127.0.0.1:9999'
}
```

## 📝 What This Example Does

1. **Launches Chromax** with fingerprint protection
2. **Tests fingerprint** by checking:
   - Navigator properties (userAgent, platform, etc.)
   - WebGL vendor/renderer
   - Canvas fingerprint
   - Native code verification
3. **Opens test site** at browserleaks.com/canvas
4. **Stays open** for manual testing

## 🧪 Testing Your Fingerprint

After the browser launches, test at:
- https://browserleaks.com/canvas
- https://browserleaks.com/webgl
- https://whoer.net
- https://pixelscan.net

## 💡 Pro Tips

1. **Use unique seeds** for canvas/webgl for different profiles
2. **Match User-Agent** with platform and WebGL vendor
3. **Test thoroughly** before production use
4. **Use puppeteer-core** (not puppeteer) to avoid downloading regular Chrome

## 🔧 Advanced Usage

### Headless Mode

```javascript
headless: true
```

### Multiple Pages

```javascript
const page1 = await browser.newPage();
const page2 = await browser.newPage();

await page1.goto('https://example.com');
await page2.goto('https://another-site.com');
```

### Screenshots

```javascript
await page.screenshot({ path: 'screenshot.png' });
```

### Scraping

```javascript
const title = await page.title();
const content = await page.$eval('h1', el => el.textContent);
```

## 📞 Support

- **Chromax Documentation**: [docs/chromax/](../../../docs/chromax/)
- **Puppeteer Docs**: https://pptr.dev/
- **Issues**: Open an issue on GitHub

## 📄 License

Proprietary License - Free for personal use
