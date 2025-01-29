# CodeAlpha_Basic_Network_Sniffer
# Network Sniffer Script

This Python script captures and analyzes network traffic using `scapy`. It captures packets, analyzes them, and immediately prints the details of each packet along with traffic statistics in the terminal.

### Requirements:
- Python 3.x
- Scapy library (for packet sniffing)
- pandas (for data analysis)
- WinPcap or Npcap (for Windows users to capture packets)

### Script Overview:

This script does the following:
- Captures all network packets.
- Displays detailed information about each packet (Ethernet, IP, TCP/UDP).
- Displays a summary of the traffic captured, including counts of TCP, UDP, and other protocols.
- Updates the packet and traffic data immediately in the terminal.

### Running the Script:
To run the script, ensure that you have scapy, pandas, and matplotlib installed. You can install them using pip:

pip install scapy pandas matplotlib

Run the script using Python:

python network_sniffer.py
