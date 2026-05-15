Date: 2026-01-05
Topics: #acl #cybersecurity 
Purpose:
Link: 
Class: [[]]

---

An access control list is a security mechanism that is used to control data and resources in a network. Its a set of rules that determines which users are allowed access to certain specific network resources.
This is okay for small organisations however for larger organizations Role based Access control is required.
Types of access controls
1. **ACL**
2. **Role Based Access Control (RBAC)**: The users are divided into roles like admin, editor, viewer
	1. Advantage
		1. Easy to manage for large teams
	2. Disadvantage
		1. If detailed permissions are required then too many roles can complicate things
3. **Attribute Based Access Control (ABAC)**: Uses attributes such as time, location, device type, etc to provide permissions
	1. Advantage
		1. Very flexible and specific policies can be made
	2. Disadvantage
		1. Hard to setup and requires detailed planning
4. **Discretionary Access Control (DAC)**: The owner can grant access to others
	1. Advantage
		1. High flexibility and control for the owner
	2. Disadvantage
		1. If not monitored properly it can quickly become inconsistent and faces the same problem as ACL which is its harder to manage in larger organisations

