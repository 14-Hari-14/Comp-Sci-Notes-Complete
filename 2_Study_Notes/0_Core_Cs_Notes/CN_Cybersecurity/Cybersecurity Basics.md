Date: 2026-01-05
Topics: #cybersecurity_basics 
Purpose:
Link: 
Class: [[]]

---

### CIA Triad
1. Confidentiality: information only to those who are authorized for it
	1. How to break
		1. Social Engineering
		2. [Packet Sniffing](Packet%20Sniffing.md)
	2. How to protect
		1. [[Encryption]] both at transit and rest
		2. Strict [Access Control List (ACL)](Access%20Control%20List%20(ACL).md)
2. Integrity: maintaining the accuracy and trustworthiness of data
	1. How to break
		1. SQL Injection
		2. Man-in-the-middle
	2. How to protect
		1. Hashing Algorithms (SHA-26)
3. Availability: Maintaining the service when required
	1. How to break
		1. [DOS(Denial of service) & DDOS (Distributed DOS)](Threats/DOS(Denial%20of%20service)%20&%20DDOS%20(Distributed%20DOS).md)
		2. Ransomware
	2. How to protect
		1. Redundancy
		2. Fail over clusters
		3. backups


## Common Attack Patterns
1. Malware
	1. [Ransomware_Notes](Threats/Ransomware_Notes.md)
	2. Fileless malware
	3. Spyware
	4. Trojan
	5. Worms
	6. [Botnet](Threats/Botnet.md)
2. [DOS(Denial of service) & DDOS (Distributed DOS)](Threats/DOS(Denial%20of%20service)%20&%20DDOS%20(Distributed%20DOS).md)
3. Phishing
4. Spoofing
5. Identity
6. Code Injection
7. Supply chain attack
8. Social Engineering