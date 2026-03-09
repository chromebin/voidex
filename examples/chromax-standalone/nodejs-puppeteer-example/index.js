/**
 * Chromax Puppeteer Example
 * 
 * This example demonstrates how to use Puppeteer with Chromax browser
 * for automated testing and scraping with native fingerprint protection.
 * 
 * Installation:
 *   npm install
 * 
 * Usage:
 *   node index.js
 */

const puppeteer = require('puppeteer-core');
const path = require('path');
const os = require('os');
const fs = require('fs');

/**
 * Configuration
 */
const config = {
  // Path to Chromax executable (auto-detects installed location)
  chromiumPath: process.env.CHROMIUM_PATH || 
    path.join(os.homedir(), 'AppData', 'Local', 'Chromax', 'chrome.exe'),
  
  // Fingerprint settings
  fingerprint: {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    platform: 'Win32',
    screenResolution: '1920x1080',
    timezone: 'America/New_York',
    acceptLanguage: 'en-US,en;q=0.9',
    cpuCores: 8,
    deviceMemory: 8,
    
    webgl: {
      mode: 'mask',
      vendor: 'Intel Inc.',
      renderer: 'Intel(R) Iris(R) Xe Graphics'
    },
    
    webglImage: {
      mode: 'noise',
      seed: 'my-unique-seed-123'
    },
    
    canvas: {
      mode: 'noise',
      seed: 'my-canvas-seed-456'
    },
    
    geolocation: {
      mode: 'prompt',
      latitude: 40.7128,
      longitude: -74.0060,
      accuracy: 50
    },
    
    uaClientHints: {
      brands: [
        { brand: 'Not A(Brand', version: '8' },
        { brand: 'Chromium', version: '132' },
        { brand: 'Google Chrome', version: '132' }
      ],
      fullVersionList: [
        { brand: 'Not A(Brand', version: '8.0.0.0' },
        { brand: 'Chromium', version: '132.0.6834.13' },
        { brand: 'Google Chrome', version: '132.0.6834.13' }
      ],
      fullVersion: '132.0.6834.13',
      platform: 'Windows',
      platformVersion: '10.0.0',
      architecture: 'x86',
      model: '',
      mobile: false,
      bitness: '64',
      wow64: false
    }
  },
  
  // Proxy settings (optional) - see ../nodejs-proxy-bridge/ for authentication support
  proxy: {
    enabled: false,
    server: ''  // e.g., 'http://127.0.0.1:9999' (use proxy bridge for auth)
  },
  
  // Browser options
  headless: false,
  viewport: {
    width: 1366,
    height: 768
  }
};

/**
 * Build Chromium launch arguments
 */
function buildChromiumArgs(config) {
  const args = [];
  
  args.push('--no-first-run');
  args.push('--no-default-browser-check');
  args.push('--disable-blink-features=AutomationControlled');
  
  const fp = config.fingerprint;
  
  if (fp.userAgent) args.push(`--user-agent=${fp.userAgent}`);
  if (fp.uaClientHints) args.push(`--fingerprint-ua-ch-json=${JSON.stringify(fp.uaClientHints)}`);
  if (fp.platform) args.push(`--fingerprint-platform=${fp.platform}`);
  if (fp.screenResolution) args.push(`--fingerprint-screen-resolution=${fp.screenResolution}`);
  if (fp.timezone) args.push(`--fingerprint-timezone=${fp.timezone}`);
  if (fp.acceptLanguage) args.push(`--fingerprint-accept-language=${fp.acceptLanguage}`);
  if (fp.cpuCores) args.push(`--fingerprint-cpu-cores=${fp.cpuCores}`);
  if (fp.deviceMemory) args.push(`--fingerprint-device-memory=${fp.deviceMemory}`);
  
  if (fp.webgl) {
    args.push(`--fingerprint-webgl-meta-mode=${fp.webgl.mode}`);
    if (fp.webgl.mode === 'mask') {
      if (fp.webgl.vendor) args.push(`--fingerprint-webgl-vendor=${fp.webgl.vendor}`);
      if (fp.webgl.renderer) args.push(`--fingerprint-webgl-renderer=${fp.webgl.renderer}`);
    }
  }
  
  if (fp.webglImage) {
    args.push(`--fingerprint-webgl-image-mode=${fp.webglImage.mode}`);
    if (fp.webglImage.mode === 'noise' && fp.webglImage.seed) {
      args.push(`--fingerprint-webgl-image-seed=${fp.webglImage.seed}`);
    }
  }
  
  if (fp.canvas) {
    args.push(`--fingerprint-canvas-mode=${fp.canvas.mode}`);
    if (fp.canvas.mode === 'noise' && fp.canvas.seed) {
      args.push(`--fingerprint-canvas-seed=${fp.canvas.seed}`);
    }
  }
  
  if (fp.geolocation) {
    args.push(`--fingerprint-geolocation-mode=${fp.geolocation.mode}`);
    if (fp.geolocation.accuracy) args.push(`--fingerprint-geolocation-accuracy=${fp.geolocation.accuracy}`);
    if (fp.geolocation.latitude && fp.geolocation.longitude) {
      args.push(`--fingerprint-geolocation-lat=${fp.geolocation.latitude}`);
      args.push(`--fingerprint-geolocation-lon=${fp.geolocation.longitude}`);
    }
  }
  
  if (config.proxy && config.proxy.enabled && config.proxy.server) {
    args.push(`--proxy-server=${config.proxy.server}`);
  }
  
  return args;
}

/**
 * Launch browser
 */
async function launchBrowser(config) {
  console.log('🚀 Launching Chromax with Puppeteer...\n');
  
  if (!fs.existsSync(config.chromiumPath)) {
    throw new Error(
      `Chromax not found at: ${config.chromiumPath}\n` +
      'Please install Chromax from: https://github.com/chromebin/voidex/releases\n' +
      'Or set CHROMIUM_PATH environment variable.'
    );
  }
  
  const userDataDir = path.join(os.tmpdir(), `chromax-puppeteer-${Date.now()}`);
  fs.mkdirSync(userDataDir, { recursive: true });
  
  const args = buildChromiumArgs(config);
  
  console.log('🔧 Chromax Path:', config.chromiumPath);
  console.log('📁 User Data:', userDataDir);
  console.log('\n🎭 Fingerprint Settings:');
  console.log('   User-Agent:', config.fingerprint.userAgent);
  console.log('   Platform:', config.fingerprint.platform);
  console.log('   Screen:', config.fingerprint.screenResolution);
  console.log('   Timezone:', config.fingerprint.timezone);
  console.log('   WebGL Mode:', config.fingerprint.webgl.mode);
  console.log('   Canvas Mode:', config.fingerprint.canvas.mode);
  console.log('\n✅ Launching browser...\n');
  
  const browser = await puppeteer.launch({
    executablePath: config.chromiumPath,
    userDataDir: userDataDir,
    headless: config.headless,
    args: args,
    defaultViewport: config.viewport,
    ignoreDefaultArgs: ['--enable-automation'],
    dumpio: false
  });
  
  console.log('✅ Browser launched!\n');
  
  return { browser, userDataDir };
}

/**
 * Test fingerprint
 */
async function testFingerprint(page) {
  console.log('🧪 Testing fingerprint...\n');
  
  const navigatorInfo = await page.evaluate(() => ({
    userAgent: navigator.userAgent,
    platform: navigator.platform,
    hardwareConcurrency: navigator.hardwareConcurrency,
    deviceMemory: navigator.deviceMemory,
    webdriver: navigator.webdriver,
    languages: navigator.languages
  }));
  
  console.log('📊 Navigator Properties:');
  console.log('   User-Agent:', navigatorInfo.userAgent);
  console.log('   Platform:', navigatorInfo.platform);
  console.log('   CPU Cores:', navigatorInfo.hardwareConcurrency);
  console.log('   Device Memory:', navigatorInfo.deviceMemory, 'GB');
  console.log('   navigator.webdriver:', navigatorInfo.webdriver);
  
  const webglInfo = await page.evaluate(() => {
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl');
    if (!gl) return { error: 'WebGL not supported' };
    
    const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    return {
      vendor: debugInfo ? gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL) : 'N/A',
      renderer: debugInfo ? gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) : 'N/A'
    };
  });
  
  console.log('\n📊 WebGL Properties:');
  console.log('   Vendor:', webglInfo.vendor);
  console.log('   Renderer:', webglInfo.renderer);
  
  const functionCheck = await page.evaluate(() => ({
    toDataURL: HTMLCanvasElement.prototype.toDataURL.toString().includes('[native code]'),
    getParameter: WebGLRenderingContext.prototype.getParameter.toString().includes('[native code]')
  }));
  
  console.log('\n📊 Native Code Check:');
  console.log('   Canvas.toDataURL:', functionCheck.toDataURL ? '✅ Native' : '❌ Modified');
  console.log('   WebGL.getParameter:', functionCheck.getParameter ? '✅ Native' : '❌ Modified');
  
  console.log('\n✅ Fingerprint test complete!\n');
}

/**
 * Main function
 */
async function main() {
  let browser = null;
  
  try {
    const { browser: launchedBrowser } = await launchBrowser(config);
    browser = launchedBrowser;
    
    const page = await browser.newPage();
    
    await testFingerprint(page);
    
    console.log('🌐 Opening fingerprint test site...\n');
    await page.goto('https://browserleaks.com/canvas', { waitUntil: 'networkidle2' });
    
    console.log('✅ Browser is ready!');
    console.log('\n📝 Test your fingerprint at:');
    console.log('   - https://browserleaks.com/canvas');
    console.log('   - https://browserleaks.com/webgl');
    console.log('\n⚠️  Browser will stay open. Press Ctrl+C to exit.\n');
    
    await new Promise(() => {});
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
  
  process.on('SIGINT', async () => {
    console.log('\n\n⚠️  Shutting down...');
    if (browser) {
      await browser.close();
    }
    process.exit(0);
  });
}

if (require.main === module) {
  main();
}

module.exports = { launchBrowser, buildChromiumArgs, testFingerprint, config };
