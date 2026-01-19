# Scan-Max 
**30-40 minutes**
Hi! I created this script to make Nmap scanning easier. Personally, I found it boring to type different Nmap commands again and again for stealth, vulns, and discovery. So, I put all 50 essential Nmap commands into this one Python script.

It’s basically an "All-in-One" Nmap automator.

## Why use this?
When you're doing a CTF or a real penetration test, you need to try different things—stealth scans, OS detection, script scanning, etc. Scan-Max does this for you in 4 phases:
1. **Stealth Mode:** To bypass firewalls (FIN, Xmas, Null, etc.).
2. **Aggressive Mode:** For versions and OS detection.
3. **Vuln Scan:** Uses Nmap NSE scripts to find Heartbleed, SMB bugs, and more.
4. **Network Discovery:** ARP, DNS, and other advanced stuff.

## Scan-Max vs Scan-Mini
* **Scan-Max:** This is the full version with 50 scans. It takes about **30-40 minutes** to finish because it goes very deep.
* **Scan-Mini:** (Coming soon/In repo) If you are in a hurry, use this one. It’s a faster version that takes only **2-7 minutes**.

## How to setup
Make sure you have Nmap installed on your Linux.
1. Download the script:
   `git clone `
2. Go to the folder:
   `cd Scan-Max`
3. Run it:
   `sudo python3 scan-max.py`

## Warning (Disclaimer)
Don't use this on any website or network you don't own. I'm not responsible if you get into trouble. Use it only for learning or ethical hacking.

**License:** MIT  
**Created by:** Syed Baijid
