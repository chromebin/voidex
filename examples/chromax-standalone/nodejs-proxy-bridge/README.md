# Chromax Proxy Bridge

A local HTTP proxy bridge that enables Chromax to connect to authenticated SOCKS5/HTTP proxies.

## 🎯 Why This Exists

Chromium's `--proxy-server` flag has limitations:
- ❌ Doesn't support SOCKS5 proxy authentication
- ❌ Doesn't support HTTP proxy authentication in all cases

This proxy bridge solves these issues by:
- ✅ Creating a local HTTP proxy (no auth needed)
- ✅ Forwarding to your upstream proxy (with auth)
- ✅ Handling SOCKS5 and HTTP proxies
- ✅ Automatic port assignment

## 📋 Prerequisites

- **Node.js** - Version 14.0.0 or higher

## 🚀 Installation

```bash
cd examples/chromax-standalone/nodejs-proxy-bridge
npm install
```

## 🎯 Usage

### Basic Usage

```bash
node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080 --port 9999
```

The bridge will start and show:
```
✅ Proxy bridge is running!

📋 Configuration:
   Local proxy:    http://127.0.0.1:9999
   Upstream proxy: socks5://user:****@host:1080

💡 Use this in your Chromax launch command:
   --proxy-server=http://127.0.0.1:9999
```

### Auto-Assign Port

```bash
node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080
```

The bridge will automatically find an available port starting from 8888.

### Verbose Logging

```bash
node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080 --verbose
```

## 📝 Examples

### SOCKS5 Proxy with Authentication

```bash
node proxy-bridge-cli.js --upstream socks5://myuser:mypass@proxy.example.com:1080 --port 9999
```

### HTTP Proxy with Authentication

```bash
node proxy-bridge-cli.js --upstream http://myuser:mypass@proxy.example.com:8080 --port 9999
```

### SOCKS5 Proxy without Authentication

```bash
node proxy-bridge-cli.js --upstream socks5://proxy.example.com:1080 --port 9999
```

## 🔗 Using with Scripts

### Node.js (Puppeteer)

**Terminal 1** - Start proxy bridge:
```bash
node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080 --port 9999
```

**Terminal 2** - Run your script:
```javascript
const puppeteer = require('puppeteer-core');

const browser = await puppeteer.launch({
  executablePath: 'C:\\Users\\[username]\\AppData\\Local\\Chromax\\chrome.exe',
  args: [
    '--proxy-server=http://127.0.0.1:9999',
    '--fingerprint-canvas-mode=noise',
    // ... other flags
  ]
});
```

### Python (Selenium)

**Terminal 1** - Start proxy bridge:
```bash
node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080 --port 9999
```

**Terminal 2** - Run your script:
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r'C:\Users\[username]\AppData\Local\Chromax\chrome.exe'
options.add_argument('--proxy-server=http://127.0.0.1:9999')
options.add_argument('--fingerprint-canvas-mode=noise')

driver = webdriver.Chrome(options=options)
driver.get('https://example.com')
```

## 🔧 Programmatic Usage

You can also use the proxy bridge module in your Node.js code:

```javascript
const { createProxyBridge } = require('./proxy-bridge');

async function main() {
  // Create bridge
  const bridge = await createProxyBridge(
    'socks5://user:pass@host:1080',
    9999,  // port (or null for auto-assign)
    true   // verbose
  );
  
  console.log(`Bridge running on: ${bridge.url}`);
  
  // ... use bridge.port with Chromax ...
  
  // Close when done
  await bridge.close();
}
```

## 🛠️ API Reference

### `createProxyBridge(upstreamProxyUrl, port, verbose)`

Creates and starts a proxy bridge.

**Parameters:**
- `upstreamProxyUrl` (string, required) - Upstream proxy URL
  - Format: `protocol://[user:pass@]host:port`
  - Examples: `socks5://user:pass@host:1080`, `http://proxy.com:8080`
- `port` (number, optional) - Local port to use (default: auto-assign from 8888+)
- `verbose` (boolean, optional) - Enable verbose logging (default: false)

**Returns:** Promise resolving to:
```javascript
{
  server: ProxyChain.Server,  // The proxy server instance
  port: number,                // The assigned port
  url: string,                 // Full URL (e.g., 'http://127.0.0.1:9999')
  upstreamProxyUrl: string,    // The upstream proxy URL
  close: async () => {}        // Function to close the bridge
}
```

### `buildProxyUrl(config)`

Builds a proxy URL from a config object.

**Parameters:**
- `config` (object) - Proxy configuration
  - `type` (string) - 'socks5' or 'http'
  - `host` (string) - Proxy host
  - `port` (number) - Proxy port
  - `username` (string, optional) - Username
  - `password` (string, optional) - Password

**Returns:** string or null

## 🔒 Security Notes

- The bridge runs on localhost (127.0.0.1) only
- Not accessible from other machines
- Credentials are only sent to the upstream proxy
- No logging of sensitive data (unless --verbose is used)

## 🆘 Troubleshooting

### Port Already in Use

**Problem**: Error: Port 9999 is already in use

**Solution**:
- Use a different port: `--port 9998`
- Or let it auto-assign: remove `--port` flag

### Connection Refused

**Problem**: Chromax can't connect to bridge

**Solution**:
- Make sure bridge is running
- Check the port number matches
- Try `--verbose` to see connection logs

### Upstream Proxy Error

**Problem**: Bridge can't connect to upstream proxy

**Solution**:
- Verify proxy credentials are correct
- Test proxy with curl or another tool
- Check proxy type (socks5 vs http)

## 📞 Support

- **Chromax Documentation**: [docs/chromax/](../../../docs/chromax/)
- **Examples**: [examples/](../../)
- **Issues**: Open an issue on GitHub

## 📄 License

Proprietary License - Free for personal use
