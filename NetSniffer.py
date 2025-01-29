from scapy.all import sniff
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP, UDP
import pandas as pd

# List to hold all packets
all_packets = []
protocol_counts = {"TCP": 0, "UDP": 0, "Other": 0}


# Function to analyze traffic and update traffic data
def analyze_traffic(packets):
    data = []
    for packet in packets:
        if IP in packet:
            protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
            protocol_counts[protocol] += 1
            data.append({
                "Source": packet[IP].src,
                "Destination": packet[IP].dst,
                "Protocol": protocol,
                "Length": len(packet)
            })
    df = pd.DataFrame(data)
    print(df.describe())


# Function to display packet details and traffic data
def display_packet(packet, traffic_data):
    if Ether in packet:
        print(f"Ethernet Frame: {packet[Ether].src} -> {packet[Ether].dst}")
    if IP in packet:
        print(f"IP Packet: {packet[IP].src} -> {packet[IP].dst}")
    if TCP in packet:
        print(f"TCP Segment: {packet[TCP].sport} -> {packet[TCP].dport}")
    if UDP in packet:
        print(f"UDP Datagram: {packet[UDP].sport} -> {packet[UDP].dport}")

    # Display the traffic data summary
    print(f"\nTotal Packets Captured: {traffic_data['total_packets']}")
    print(f"TCP Packets: {traffic_data['TCP']}")
    print(f"UDP Packets: {traffic_data['UDP']}")
    print(f"Other Protocols: {traffic_data['Other']}")
    print("-" * 50)


# Callback function for sniffing all traffic
def packet_callback(packet, packets, traffic_data):
    packets.append(packet)

    # Update traffic data
    if IP in packet:
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        traffic_data[protocol] += 1
        traffic_data['total_packets'] += 1

    # Print the packet and traffic data immediately
    display_packet(packet, traffic_data)


# Sniffing function to capture packets
def sniff_packets(packets, traffic_data):
    # Capture all packets without protocol filtering
    sniff(prn=lambda x: packet_callback(x, packets, traffic_data), store=0)


# Main function to start sniffing and display packet data
def main():
    packets = []
    traffic_data = {"total_packets": 0, "TCP": 0, "UDP": 0, "Other": 0}

    # Start sniffing packets and print data immediately
    sniff_packets(packets, traffic_data)


if __name__ == "__main__":
    main()
