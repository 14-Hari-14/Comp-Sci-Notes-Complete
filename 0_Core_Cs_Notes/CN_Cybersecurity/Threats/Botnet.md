Date: 2026-01-05
Topics: #botnet #cybersecurity #threat 
Link: 
Class: [[]]

---

Botnet: group of computers which have been infected by malware and have come under the control of a malicious actor.
This makes them very useful for
1. [[Ransomware]]
2. [DOS(Denial of service) & DDOS (Distributed DOS)](DOS(Denial%20of%20service)%20&%20DDOS%20(Distributed%20DOS).md)

Due to their flexibility they can have different levels of visibility some ddos botnet malware is designed to take control of the device while other wait for the **bot herder** to provide them with instructions

Self propogating botnet infect other devices and recruit them as bots using various strategy
1. [[Trojan]]
2. Cracking weak authentication
3. Exploitation of other vulnerabilities

Examples are:
1. [Mirai Botnet](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/)
2. [Meris Botnet](https://blog.cloudflare.com/meris-botnet/)


## Types of Botnet
1. Client/Server
	1. Star topology
	2. Multiserver topology
	3. Hierarchical topology
2. Peer-to-peer 


### Client Server Architecture
Mimics the traditional workstation models where the botnets connect to 1 or a small number of Command-and-control (cnc) center like a web domain or an IRC channel^[internet relay chat] (text based real time chatroom)
![[../../../2_Images/botnet topology.png|botnet topology.png]]
Disadvantages
1. A single / few points of disruption depending on the topology used can cause the botnet removal

### Peer-to-Peer Architecture
To make the system more robust the botnets have now begun to mimic the architecture of peer-to-peer file sharing applications, like torrent
P2P botnets have a list of devices which are safe to take instructions from and send to aswell to update their malware
To protect against loss of control these botnets are typically encrypted so that access is limited

### How to recruit botnets
The power of IoT devices coupled with weak or poorly configured security creates an opening for botnet malware to recruit new bots into the collective. An uptick in IoT devices has resulted in a new landscape for DDoS attacks, as many devices are poorly configured and vulnerable.

### How to protect from becoming botnet
Other more advanced strategies include filtering practices at network routers and [firewalls](https://www.cloudflare.com/learning/security/what-is-a-firewall/). A principle of secure network design is layering: you have the least restriction around publicly accessible resources, while continually beefing up security for things you deem sensitive. Additionally, anything that crosses these boundaries has to be scrutinized: network traffic, usb drives, etc. Quality filtering practices increase the likelihood that DDoS malware and their methods of propagation and communication will be caught before entering or leaving the network.