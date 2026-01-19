#!/usr/bin/env python3
import os
import sys

# ---------------------------------------------------------
# Tool: Scan-Max
# Author: Syed Baijid
# Description: Automates 50 deep Nmap scans. Takes 30-40 min.
# ---------------------------------------------------------

def run_ultimate_scan(target):
    # Banner - simple and clean
    print("\n" + "="*70)
    print(f"  SCAN-MAX: STARTING DEEP RECONNAISSANCE ON: {target}")
    print("="*70)
    print("[*] Note: This is the full version. It will take 30-40 minutes.")
    print("[*] Syed Baijid's Scan-Mini is faster (2-7 min) if you are in a rush.\n")

    # The 50 commands grouped by phases
    scan_phases = {
        "Discovery & Stealth": [
            f"nmap -sn -Pn {target}",                        # 1. Ping Sweep
            f"nmap -sS -Pn -T2 {target}",                    # 2. Stealth SYN
            f"nmap -sF -Pn {target}",                        # 3. FIN Scan
            f"nmap -sX -Pn {target}",                        # 4. Xmas Scan
            f"nmap -sN -Pn {target}",                        # 5. Null Scan
            f"nmap -sA -Pn {target}",                        # 6. ACK Scan
            f"nmap -sM -Pn {target}",                        # 7. Maimon Scan
            f"nmap --reason -Pn {target}",                   # 8. Show Reason
            f"nmap -f -sS -Pn {target}",                     # 9. Packet Fragmentation
            f"nmap --mtu 8 -sS -Pn {target}",                # 10. Tiny MTU
            f"nmap -D RND:20 -sS -Pn {target}",              # 11. 20 Random Decoys
            f"nmap -S 192.168.1.1 -e wlan0 -Pn {target}",    # 12. IP Spoofing
            f"nmap --source-port 88 -Pn {target}",           # 13. Spoof Kerberos Port
            f"nmap --source-port 445 -Pn {target}",          # 14. Spoof SMB Port
            f"nmap --data-length 100 -Pn {target}",          # 15. Pad packets
            f"nmap --spoof-mac 0 -Pn {target}",              # 16. Randomize MAC
            f"nmap --badsum -Pn {target}",                   # 17. Bad Checksum Scan
            f"nmap -sS -T1 -Pn {target}",                    # 18. Paranoid Timing
            f"nmap -sS --scan-delay 5s -Pn {target}",        # 19. Custom Delay
            f"nmap -6 {target}"                              # 20. IPv6 Scan
        ],
        "Aggressive Intelligence": [
            f"nmap -sV --version-intensity 9 -Pn {target}",  # 21. Max Version Detection
            f"nmap -O --osscan-guess -Pn {target}",          # 22. Aggressive OS Fingerprint
            f"nmap -A -Pn {target}",                         # 23. Full Aggressive
            f"nmap -p 1-65535 -T4 -Pn {target}",             # 24. Full Port Range
            f"nmap -sU --top-ports 100 -Pn {target}",        # 25. Top 100 UDP Ports
            f"nmap -sS -sV --script banner -Pn {target}"     # 26. Banner Grabbing
        ],
        "NSE Vulnerability Analysis": [
            f"nmap --script vuln -Pn {target}",              # 27. General Vuln Scan
            f"nmap --script exploit -Pn {target}",           # 28. Exploit Checks
            f"nmap --script auth -Pn {target}",              # 29. Auth checks
            f"nmap --script malware -Pn {target}",           # 30. Check Infections
            f"nmap --script brute -Pn {target}",             # 31. Brute Force
            f"nmap --script broadcast -Pn {target}",         # 32. Broadcast discovery
            f"nmap --script default,safe -Pn {target}",      # 33. Safe/Default scripts
            f"nmap --script smb-vuln* -p 445 {target}",      # 34. SMB Vuln check
            f"nmap --script http-vuln* -p 80,443 {target}",  # 35. Web Vuln check
            f"nmap --script ftp-anon -p 21 {target}",        # 36. FTP Anon
            f"nmap --script ssl-heartbleed -p 443 {target}", # 37. Heartbleed Test
            f"nmap --script rdp-vuln-ms12-020 {target}",     # 38. RDP Vuln
            f"nmap --script ssh-run -Pn {target}",           # 39. SSH Check
            f"nmap --script mysql-info -p 3306 {target}"     # 40. MySQL Info
        ],
        "Advanced Network Discovery": [
            f"nmap -PR -sn {target}",                        # 41. ARP Discovery
            f"nmap --script dns-brute {target}",             # 42. DNS Brute
            f"nmap --script traceroute-geoloc {target}",     # 43. Traceroute Geo-IP
            f"nmap --script snmp-info -p 161 {target}",      # 44. SNMP Enumeration
            f"nmap --script nfs-ls -p 111 {target}",         # 45. NFS Share listing
            f"nmap --script vnc-info -p 5900 {target}",      # 46. VNC Info
            f"nmap --script ldap-search -p 389 {target}",    # 47. LDAP Enumeration
            f"nmap --script postgres-query -p 5432 {target}",# 48. PostgreSQL check
            f"nmap --script upnp-info {target}",             # 49. UPnP Discovery
            f"nmap --packet-trace -Pn {target}"              # 50. Full Packet Trace
        ]
    }

    count = 1
    try:
        for phase, cmds in scan_phases.items():
            print(f"\n>>> CURRENT PHASE: {phase}")
            print("-" * 40)
            for cmd in cmds:
                print(f"[{count}/50] Running: {cmd}")
                os.system(cmd)
                count += 1
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting...")
        sys.exit()

    print("\n" + "="*70)
    print("[!] DONE! Scan-Max has finished the reconnaissance.")
    print("="*70)

if __name__ == "__main__":
    # Check if target is provided
    target_ip = input("Enter Target IP or Domain: ").strip()
    
    if target_ip:
        run_ultimate_scan(target_ip)
    else:
        print("[!] No target entered. Please try again.")
