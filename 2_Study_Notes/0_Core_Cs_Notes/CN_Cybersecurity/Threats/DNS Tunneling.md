Date: 2026-01-05
Topics: #dns_tunneling #cybersecurity #threat 
Purpose:
Link: 
Class: [[]]

---

# DNS Tunneling

It is a technique where attackers hide data or commands inside regular DNS queries and responses.

## How it works

- Normal DNS is used to look up website addresses
- Attackers add extra data to these DNS requests that shouldn't be there
- This data travels through the network without being noticed
- It can be used to steal information or send commands to hacked computers

## Why it's dangerous

- **Hard to detect**: DNS traffic looks normal to security systems
- **Bypasses filters**: Many networks allow DNS traffic
- **Hidden communication**: Hackers can talk to infected computers secretly

## How to prevent it

- Monitor unusual DNS activity and patterns
- Block DNS queries going to suspicious domains
- Use deep packet inspection to analyze DNS content
- See [Packet Sniffing](../Packet%20Sniffing.md) for detection methods

## Related

- [DOS(Denial of service) & DDOS (Distributed DOS)](DOS(Denial%20of%20service)%20&%20DDOS%20(Distributed%20DOS).md)
- [Phishing](Phishing.md)
