# Chromax + Selenium Example

Complete example of using Selenium with Chromax browser for automated testing and scraping with native fingerprint protection.

## 📋 Prerequisites

1. **Install Chromax** - Download ChromaxSetup.exe from [Downloads](../../../DOWNLOADS.md)
2. **Install Python** - Version 3.7 or higher

## 🚀 Installation

```bash
cd examples/chromax-standalone/python-selenium-example
pip install -r requirements.txt
```

## 🎯 Usage

### Basic Usage

```bash
python main.py
```

The script will:
1. Launch Chromax with fingerprint protection
2. Test fingerprint settings
3. Open https://browserleaks.com/canvas
4. Wait for you to press Enter before closing

### Custom Chromax Path

If Chromax is not installed at the default location, set the environment variable:

```bash
# Windows (Command Prompt)
set CHROMIUM_PATH=C:\custom\path\to\chrome.exe
python main.py

# Windows (PowerShell)
$env:CHROMIUM_PATH="C:\custom\path\to\chrome.exe"
python main.py

# Linux/Mac
export CHROMIUM_PATH=/custom/path/to/chrome
python main.py
```

## ⚙️ Configuration

Edit `main.py` to customize fingerprint settings:

```python
CONFIG = {
    'chromium_path': '...',  # Auto-detected
    
    'fingerprint': {
        'user_agent': 'Mozilla/5.0...',
        'platform': 'Win32',
        'screen_resolution': '1920x1080',
        'timezone': 'America/New_York',
        
        'webgl': {
            'mode': 'mask',
            'vendor': 'Intel Inc.',
            'renderer': 'Intel(R) Iris(R) Xe Graphics'
        },
        
        'canvas': {
            'mode': 'noise',
            'seed': 'my-canvas-seed-456'
        }
    }
}
```

## 🔗 Proxy Support

### Without Authentication

```python
'proxy': {
    'enabled': True,
    'server': 'http://proxy.example.com:8080'
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
```python
'proxy': {
    'enabled': True,
    'server': 'http://127.0.0.1:9999'
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
4. **Waits** for you to press Enter before closing

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
4. **Install selenium** via pip, not system package manager

## 🔧 Advanced Usage

### Headless Mode

```python
'headless': True
```

### Screenshots

```python
driver.save_screenshot('screenshot.png')
```

### Element Interaction

```python
element = driver.find_element(By.ID, 'button')
element.click()

input_field = driver.find_element(By.NAME, 'username')
input_field.send_keys('myusername')
```

### Wait for Elements

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'myElement')))
```

## 📞 Support

- **Chromax Documentation**: [docs/chromax/](../../../docs/chromax/)
- **Selenium Docs**: https://selenium-python.readthedocs.io/
- **Issues**: Open an issue on GitHub

## 📄 License

Proprietary License - Free for personal use
