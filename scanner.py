import requests
import sys

def scan_website(url):
    print(f"\n[*] Scanning target: {url}\n")
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[-] Error connecting to {url}: {e}")
        return

    # Check Security Headers
    print("--- Security Headers Audit ---")
    security_headers = [
        'Content-Security-Policy',
        'X-Frame-Options',
        'X-Content-Type-Options',
        'Strict-Transport-Security'
    ]
    
    for header in security_headers:
        if header in response.headers:
            print(f"[+] [PASS] {header} is present.")
        else:
            print(f"[-] [WARN] {header} is missing.")

    # Check CORS Configuration
    print("\n--- CORS Misconfiguration Check ---")
    cors_header = response.headers.get('Access-Control-Allow-Origin')
    if cors_header:
        print(f"[!] Access-Control-Allow-Origin found: {cors_header}")
        if cors_header == '*':
            print("[-] [WARN] Wildcard '*' detected.")
    else:
        print("[+] [PASS] No permissive CORS header found.")

if __name__ == "__main__":
    target_url = input("Enter target URL (e.g., https://example.com): ").strip()
    scan_website(target_url)