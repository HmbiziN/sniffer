# Sniffer

In an MITM scenario, an attacker could use such a script to capture unencrypted HTTP packets, including HTTP requests and responses. This could enable the attacker to intercept sensitive information, such as login credentials, cookies, or other confidential data.

## I created this python script to demonstrate the simplicity of such a practice and the importance of using HTTPS encryption, which secures communications between the browser and the website. 



## How it works?
this code uses the scapy library to analyze network traffic in real time
the packet function is called each time a new packet is captured by scapy
The haslayer function is used to check whether the packet has both IP and TCP layers. This check is important to ensure that the packet contains the necessary information.
If the above conditions are met, information about the packet is displayed. This includes the source address (packet[IP].src), destination address (packet[IP].dst), destination port (packet[IP].dport), and TCP packet payload data (packet[TCP].payload).

## How to protect?
- Use HTTPS: When browsing websites, make sure the connection is secure by using the HTTPS protocol. Secure websites encrypt data between the browser and the server, making it more difficult to intercept.
- Regular updates: Keep your operating system, browser and applications up to date. Regular updates often include security patches for known vulnerabilities.
- Secure Wi-Fi network: Avoid connecting to unsecured public Wi-Fi networks. If you must use a public network, be sure to use a VPN (Virtual Private Network) to encrypt your traffic.