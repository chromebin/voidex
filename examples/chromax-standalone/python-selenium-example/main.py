#!/usr/bin/env python3
"""
Chromax Selenium Example

This example demonstrates how to use Selenium with Chromax browser
for automated testing and scraping with native fingerprint protection.

Installation:
    pip install -r requirements.txt

Proxy Support:
    For proxies with authentication, use the Node.js proxy bridge:
    
    1. In a separate terminal:
       cd ../nodejs-proxy-bridge
       node proxy-bridge-cli.js --upstream socks5://user:pass@host:1080 --port 9999
    
    2. Then set proxy config in this script:
       'proxy': {
           'enabled': True,
           'server': 'http://127.0.0.1:9999'
       }

Usage:
    python main.py
"""

import os
import sys
import json
import time
import tempfile
from pathlib import Path
from typing import Dict

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configuration
CONFIG = {
    # Path to Chromax executable (auto-detects installed location)
    'chromium_path': os.environ.get('CHROMIUM_PATH', 
        os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Chromax', 'chrome.exe')),
    
    # Fingerprint settings
    'fingerprint': {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'platform': 'Win32',
        'screen_resolution': '1920x1080',
        'timezone': 'America/New_York',
        'accept_language': 'en-US,en;q=0.9',
        'cpu_cores': 8,
        'device_memory': 8,
        
        'webgl': {
            'mode': 'mask',
            'vendor': 'Intel Inc.',
            'renderer': 'Intel(R) Iris(R) Xe Graphics'
        },
        
        'webgl_image': {
            'mode': 'noise',
            'seed': 'my-unique-seed-123'
        },
        
        'canvas': {
            'mode': 'noise',
            'seed': 'my-canvas-seed-456'
        },
        
        'geolocation': {
            'mode': 'prompt',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'accuracy': 50
        },
        
        'ua_client_hints': {
            'brands': [
                {'brand': 'Not A(Brand', 'version': '8'},
                {'brand': 'Chromium', 'version': '132'},
                {'brand': 'Google Chrome', 'version': '132'}
            ],
            'fullVersionList': [
                {'brand': 'Not A(Brand', 'version': '8.0.0.0'},
                {'brand': 'Chromium', 'version': '132.0.6834.13'},
                {'brand': 'Google Chrome', 'version': '132.0.6834.13'}
            ],
            'fullVersion': '132.0.6834.13',
            'platform': 'Windows',
            'platformVersion': '10.0.0',
            'architecture': 'x86',
            'model': '',
            'mobile': False,
            'bitness': '64',
            'wow64': False
        }
    },
    
    # Proxy settings (optional)
    'proxy': {
        'enabled': False,
        'server': ''  # e.g., 'http://127.0.0.1:9999' (use proxy bridge for auth)
    },
    
    # Browser options
    'headless': False
}


def build_chrome_options(config: Dict) -> Options:
    """Build Chrome options with fingerprint flags"""
    options = Options()
    
    chromium_path = Path(config['chromium_path'])
    if not chromium_path.exists():
        raise FileNotFoundError(
            f"Chromax not found at: {chromium_path}\n"
            "Please install Chromax from: https://github.com/chromebin/voidex/releases\n"
            "Or set CHROMIUM_PATH environment variable."
        )
    
    options.binary_location = str(chromium_path)
    
    user_data_dir = tempfile.mkdtemp(prefix='chromax-selenium-')
    options.add_argument(f'--user-data-dir={user_data_dir}')
    
    options.add_argument('--no-first-run')
    options.add_argument('--no-default-browser-check')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    fp = config['fingerprint']
    
    if fp.get('user_agent'):
        options.add_argument(f'--user-agent={fp["user_agent"]}')
    
    if fp.get('ua_client_hints'):
        ua_ch_json = json.dumps(fp['ua_client_hints'])
        options.add_argument(f'--fingerprint-ua-ch-json={ua_ch_json}')
    
    if fp.get('platform'):
        options.add_argument(f'--fingerprint-platform={fp["platform"]}')
    
    if fp.get('screen_resolution'):
        options.add_argument(f'--fingerprint-screen-resolution={fp["screen_resolution"]}')
    
    if fp.get('timezone'):
        options.add_argument(f'--fingerprint-timezone={fp["timezone"]}')
    
    if fp.get('accept_language'):
        options.add_argument(f'--fingerprint-accept-language={fp["accept_language"]}')
    
    if fp.get('cpu_cores'):
        options.add_argument(f'--fingerprint-cpu-cores={fp["cpu_cores"]}')
    
    if fp.get('device_memory'):
        options.add_argument(f'--fingerprint-device-memory={fp["device_memory"]}')
    
    if fp.get('webgl'):
        webgl = fp['webgl']
        options.add_argument(f'--fingerprint-webgl-meta-mode={webgl["mode"]}')
        if webgl['mode'] == 'mask':
            if webgl.get('vendor'):
                options.add_argument(f'--fingerprint-webgl-vendor={webgl["vendor"]}')
            if webgl.get('renderer'):
                options.add_argument(f'--fingerprint-webgl-renderer={webgl["renderer"]}')
    
    if fp.get('webgl_image'):
        webgl_img = fp['webgl_image']
        options.add_argument(f'--fingerprint-webgl-image-mode={webgl_img["mode"]}')
        if webgl_img['mode'] == 'noise' and webgl_img.get('seed'):
            options.add_argument(f'--fingerprint-webgl-image-seed={webgl_img["seed"]}')
    
    if fp.get('canvas'):
        canvas = fp['canvas']
        options.add_argument(f'--fingerprint-canvas-mode={canvas["mode"]}')
        if canvas['mode'] == 'noise' and canvas.get('seed'):
            options.add_argument(f'--fingerprint-canvas-seed={canvas["seed"]}')
    
    if fp.get('geolocation'):
        geo = fp['geolocation']
        options.add_argument(f'--fingerprint-geolocation-mode={geo["mode"]}')
        if geo.get('accuracy'):
            options.add_argument(f'--fingerprint-geolocation-accuracy={geo["accuracy"]}')
        if geo.get('latitude') and geo.get('longitude'):
            options.add_argument(f'--fingerprint-geolocation-lat={geo["latitude"]}')
            options.add_argument(f'--fingerprint-geolocation-lon={geo["longitude"]}')
    
    if config.get('proxy', {}).get('enabled') and config['proxy'].get('server'):
        options.add_argument(f'--proxy-server={config["proxy"]["server"]}')
    
    if config.get('headless'):
        options.add_argument('--headless=new')
    
    return options


def test_fingerprint(driver: webdriver.Chrome):
    """Test fingerprint settings"""
    print('🧪 Testing fingerprint...\n')
    
    print('📊 Navigator Properties:')
    nav_info = driver.execute_script("""
        return {
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            hardwareConcurrency: navigator.hardwareConcurrency,
            deviceMemory: navigator.deviceMemory,
            webdriver: navigator.webdriver
        };
    """)
    print(f'   User-Agent: {nav_info["userAgent"]}')
    print(f'   Platform: {nav_info["platform"]}')
    print(f'   CPU Cores: {nav_info["hardwareConcurrency"]}')
    print(f'   Device Memory: {nav_info["deviceMemory"]} GB')
    print(f'   navigator.webdriver: {nav_info["webdriver"]}')
    
    print('\n📊 WebGL Properties:')
    webgl_info = driver.execute_script("""
        const canvas = document.createElement('canvas');
        const gl = canvas.getContext('webgl');
        if (!gl) return { error: 'WebGL not supported' };
        
        const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
        return {
            vendor: debugInfo ? gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL) : 'N/A',
            renderer: debugInfo ? gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) : 'N/A'
        };
    """)
    print(f'   Vendor: {webgl_info["vendor"]}')
    print(f'   Renderer: {webgl_info["renderer"]}')
    
    print('\n📊 Native Code Check:')
    func_check = driver.execute_script("""
        return {
            toDataURL: HTMLCanvasElement.prototype.toDataURL.toString().includes('[native code]'),
            getParameter: WebGLRenderingContext.prototype.getParameter.toString().includes('[native code]')
        };
    """)
    print(f'   Canvas.toDataURL: {"✅ Native" if func_check["toDataURL"] else "❌ Modified"}')
    print(f'   WebGL.getParameter: {"✅ Native" if func_check["getParameter"] else "❌ Modified"}')
    
    print('\n✅ Fingerprint test complete!\n')


def main():
    """Main function"""
    driver = None
    
    try:
        print('🚀 Launching Chromax with Selenium...\n')
        
        options = build_chrome_options(CONFIG)
        
        print(f'🔧 Chromax Path: {CONFIG["chromium_path"]}')
        print('\n🎭 Fingerprint Settings:')
        print(f'   User-Agent: {CONFIG["fingerprint"]["user_agent"]}')
        print(f'   Platform: {CONFIG["fingerprint"]["platform"]}')
        print(f'   Screen: {CONFIG["fingerprint"]["screen_resolution"]}')
        print(f'   Timezone: {CONFIG["fingerprint"]["timezone"]}')
        print(f'   WebGL Mode: {CONFIG["fingerprint"]["webgl"]["mode"]}')
        print(f'   Canvas Mode: {CONFIG["fingerprint"]["canvas"]["mode"]}')
        print('\n✅ Launching browser...\n')
        
        driver = webdriver.Chrome(options=options)
        
        print('✅ Browser launched!\n')
        
        test_fingerprint(driver)
        
        print('🌐 Opening fingerprint test site...\n')
        driver.get('https://browserleaks.com/canvas')
        
        print('✅ Browser is ready!')
        print('\n📝 Test your fingerprint at:')
        print('   - https://browserleaks.com/canvas')
        print('   - https://browserleaks.com/webgl')
        print('\n⚠️  Browser will stay open. Press Enter to close...\n')
        
        input()
        
    except FileNotFoundError as e:
        print(f'❌ Error: {e}', file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print('\n\n⚠️  Interrupted by user')
    except Exception as e:
        print(f'❌ Error: {e}', file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        if driver:
            driver.quit()
            print('\n✅ Browser closed. Done!')


if __name__ == '__main__':
    main()
